from functools import reduce
import operator as op

from manimlib.constants import *
from manimlib.mobject.geometry import Line
from manimlib.mobject.svg.svg_mobject import SVGMobject
from manimlib.mobject.svg.svg_mobject import VMobjectFromSVGPathstring
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VectorizedPoint
from manimlib.utils.config_ops import digest_config
from manimlib.utils.strings import split_string_list_to_isolate_substrings
from manimlib.utils.tex_file_writing import tex_to_svg_file


TEX_MOB_SCALE_FACTOR = 0.05


class TexSymbol(VMobjectFromSVGPathstring):
    """VMobjectFromSVGPathstring的别名，每个路径都是一个TexSymbol"""
    pass


class SingleStringTexMobject(SVGMobject):
    """单个字符串渲染出的SVGMobject"""
    CONFIG = {
        "template_tex_file_body": TEMPLATE_TEX_FILE_BODY,
        "stroke_width": 0,
        "fill_opacity": 1.0,
        "background_stroke_width": 1,
        "background_stroke_color": BLACK,
        # "color": BLACK,
        "should_center": True,
        "height": None,
        "organize_left_to_right": False,
        "alignment": "",
    }

    def __init__(self, tex_string, **kwargs):
        """只传入一个字符串 ``tex_string``"""
        digest_config(self, kwargs)
        assert(isinstance(tex_string, str))
        self.tex_string = tex_string
        file_name = tex_to_svg_file(
            self.get_modified_expression(tex_string),
            self.template_tex_file_body
        )
        SVGMobject.__init__(self, file_name=file_name, **kwargs)
        if self.height is None:
            self.scale(TEX_MOB_SCALE_FACTOR)
        if self.organize_left_to_right:
            self.organize_submobjects_left_to_right()

    def get_modified_expression(self, tex_string):
        """将对齐参数与传入的字符串拼接，并且处理特殊的字符串"""
        result = self.alignment + " " + tex_string
        result = result.strip()
        result = self.modify_special_strings(result)
        return result

    def modify_special_strings(self, tex):
        """处理特殊不合法的字符串"""
        tex = self.remove_stray_braces(tex)
        should_add_filler = reduce(op.or_, [
            # Fraction line needs something to be over
            tex == "\\over",
            tex == "\\overline",
            # Makesure sqrt has overbar
            tex == "\\sqrt",
            # Need to add blank subscript or superscript
            tex.endswith("_"),
            tex.endswith("^"),
            tex.endswith("dot"),
        ])
        if should_add_filler:
            filler = "{\\quad}"
            tex += filler

        if tex == "\\substack":
            tex = "\\quad"

        if tex == "":
            tex = "\\quad"

        # To keep files from starting with a line break
        if tex.startswith("\\\\"):
            tex = tex.replace("\\\\", "\\quad\\\\")

        # Handle imbalanced \left and \right
        num_lefts, num_rights = [
            len([
                s for s in tex.split(substr)[1:]
                if s and s[0] in "(){}[]|.\\"
            ])
            for substr in ("\\left", "\\right")
        ]
        if num_lefts != num_rights:
            tex = tex.replace("\\left", "\\big")
            tex = tex.replace("\\right", "\\big")

        for context in ["array"]:
            begin_in = ("\\begin{%s}" % context) in tex
            end_in = ("\\end{%s}" % context) in tex
            if begin_in ^ end_in:
                # Just turn this into a blank string,
                # which means caller should leave a
                # stray \\begin{...} with other symbols
                tex = ""
        return tex

    def remove_stray_braces(self, tex):
        """匹配大括号"""
        if tex.find("\\{"):
            return tex
        if tex == "\\{" or tex == "\\}":
            return tex
        num_lefts, num_rights = [
            tex.count(char)
            for char in "{}"
        ]
        while num_rights > num_lefts:
            tex = "{" + tex
            num_lefts += 1
        while num_lefts > num_rights:
            tex = tex + "}"
            num_rights += 1
        left_need = 0
        for i in range(len(tex)):
            if tex[i] == "}":
                left_need += 1
            if tex[i] == "{":
                break
        right_need = 0
        for i in range(len(tex) - 1, 0, -1):
            if tex[i] == "{":
                right_need += 1
            if tex[i] == "}":
                break
        tex = "{" * left_need + tex + "}" * right_need

        if tex.find("\\frac{}") != -1:
            tex = tex + "{}"
        # if tex.find("prod_") != -1:
        #     tex = "{" + tex + "}"
        return tex

    def get_tex_string(self):
        return self.tex_string

    def path_string_to_mobject(self, path_string):
        # Overwrite superclass default to use
        # specialized path_string mobject
        return TexSymbol(path_string)

    def organize_submobjects_left_to_right(self):
        self.sort(lambda p: p[0])
        return self


class TexMobject(SingleStringTexMobject):
    """用于生成LaTeX公式（align环境）"""
    CONFIG = {
        "arg_separator": " ",
        "substrings_to_isolate": [],
        "tex_to_color_map": {},
    }

    def __init__(self, *tex_strings, **kwargs):
        """可传入多个 ``tex_strings``
        
        ``arg_separator`` 表示每两个字符串之间的字符，默认为空格

        ``tex_to_color_map`` 为一个字典，会根据其中的键自动拆开字符串用于上色
        """
        digest_config(self, kwargs)
        tex_strings = self.break_up_tex_strings(tex_strings)
        self.tex_strings = tex_strings
        SingleStringTexMobject.__init__(
            self, self.arg_separator.join(tex_strings), **kwargs
        )
        self.break_up_by_substrings()
        self.set_color_by_tex_to_color_map(self.tex_to_color_map)

        if self.organize_left_to_right:
            self.organize_submobjects_left_to_right()

    def break_up_tex_strings(self, tex_strings):
        """根据传入的tex_to_color_map再次拆开tex_strings"""
        substrings_to_isolate = op.add(
            self.substrings_to_isolate,
            list(self.tex_to_color_map.keys())
        )
        split_list = split_string_list_to_isolate_substrings(
            tex_strings, *substrings_to_isolate
        )
        if self.arg_separator == ' ':
            split_list = [str(x).strip() for x in split_list]
        #split_list = list(map(str.strip, split_list))
        split_list = [s for s in split_list if s != '']
        return split_list

    def break_up_by_substrings(self):
        """重新组织子物体，``tex_string`` 中每个子字符串为一个子物体"""
        new_submobjects = []
        curr_index = 0
        config = dict(self.CONFIG)
        config["alignment"] = ""
        for tex_string in self.tex_strings:
            sub_tex_mob = SingleStringTexMobject(tex_string, **config)
            num_submobs = len(sub_tex_mob.submobjects)
            new_index = curr_index + num_submobs
            if num_submobs == 0:
                # For cases like empty tex_strings, we want the corresponing
                # part of the whole TexMobject to be a VectorizedPoint
                # positioned in the right part of the TexMobject
                sub_tex_mob.submobjects = [VectorizedPoint()]
                last_submob_index = min(curr_index, len(self.submobjects) - 1)
                sub_tex_mob.move_to(self.submobjects[last_submob_index], RIGHT)
            else:
                sub_tex_mob.submobjects = self.submobjects[curr_index:new_index]
            new_submobjects.append(sub_tex_mob)
            curr_index = new_index
        self.submobjects = new_submobjects
        return self

    def get_parts_by_tex(self, tex, substring=True, case_sensitive=True):
        def test(tex1, tex2):
            if not case_sensitive:
                tex1 = tex1.lower()
                tex2 = tex2.lower()
            if substring:
                return tex1 in tex2
            else:
                return tex1 == tex2

        return VGroup(*[m for m in self.submobjects if test(tex, m.get_tex_string())])

    def get_part_by_tex(self, tex, **kwargs):
        all_parts = self.get_parts_by_tex(tex, **kwargs)
        return all_parts[0] if all_parts else None

    def set_color_by_tex(self, tex, color, **kwargs):
        """给 ``tex`` 上颜色为 ``color`` ，注意此时 ``tex`` 要独立存在，否则会给包含 ``tex`` 的也上色"""
        parts_to_color = self.get_parts_by_tex(tex, **kwargs)
        for part in parts_to_color:
            part.set_color(color)
        return self

    def set_color_by_tex_to_color_map(self, texs_to_color_map, **kwargs):
        """根据 ``texs_to_color_map`` 上色，同样，会给包含键的全部上色，不会自动拆分"""
        for texs, color in list(texs_to_color_map.items()):
            try:
                # If the given key behaves like tex_strings
                texs + ''
                self.set_color_by_tex(texs, color, **kwargs)
            except TypeError:
                # If the given key is a tuple
                for tex in texs:
                    self.set_color_by_tex(tex, color, **kwargs)
        return self

    def index_of_part(self, part):
        split_self = self.split()
        if part not in split_self:
            raise Exception("Trying to get index of part not in TexMobject")
        return split_self.index(part)

    def index_of_part_by_tex(self, tex, **kwargs):
        """根据tex获取在子物体中的下标"""
        part = self.get_part_by_tex(tex, **kwargs)
        return self.index_of_part(part)

    def sort_alphabetically(self):
        """根据字典序给子物体排序"""
        self.submobjects.sort(
            key=lambda m: m.get_tex_string()
        )


class TextMobject(TexMobject):
    """用于生成LaTeX文字，默认每行之间居中
    
    传入的两个字符串之间无分隔(即 ``arg_separator=""`` )
    """
    CONFIG = {
        "template_tex_file_body": TEMPLATE_TEXT_FILE_BODY,
        "alignment": "\\centering",
        "arg_separator": "",
    }


class BulletedList(TextMobject):
    """项目列表"""
    CONFIG = {
        "buff": MED_LARGE_BUFF,
        "dot_scale_factor": 2,
        # Have to include because of handle_multiple_args implementation
        "template_tex_file_body": TEMPLATE_TEXT_FILE_BODY,
        "alignment": "",
    }

    def __init__(self, *items, **kwargs):
        """支持多个字符串，每个一行；也支持一个字符串，使用LaTeX的换行（\\\\）"""
        line_separated_items = [s + "\\\\" for s in items]
        TextMobject.__init__(self, *line_separated_items, **kwargs)
        for part in self:
            dot = TexMobject("\\cdot").scale(self.dot_scale_factor)
            dot.next_to(part[0], LEFT, SMALL_BUFF)
            part.add_to_back(dot)
        self.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=self.buff
        )

    def fade_all_but(self, index_or_string, opacity=0.5):
        """把除了 ``index_or_string`` 之外的不透明度均设为 ``opacity``
        
        ``index_or_string`` 可以传入子物体的下标，也可以传入一个字符串
        """
        arg = index_or_string
        if isinstance(arg, str):
            part = self.get_part_by_tex(arg)
        elif isinstance(arg, int):
            part = self.submobjects[arg]
        else:
            raise Exception("Expected int or string, got {0}".format(arg))
        for other_part in self.submobjects:
            if other_part is part:
                other_part.set_fill(opacity=1)
            else:
                other_part.set_fill(opacity=opacity)


class TexMobjectFromPresetString(TexMobject):
    CONFIG = {
        # To be filled by subclasses
        "tex": None,
        "color": None,
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        TexMobject.__init__(self, self.tex, **kwargs)
        self.set_color(self.color)


class Title(TextMobject):
    """标题"""
    CONFIG = {
        "scale_factor": 1,
        "include_underline": True,
        "underline_width": FRAME_WIDTH - 2,
        # This will override underline_width
        "match_underline_width_to_text": False,
        "underline_buff": MED_SMALL_BUFF,
    }

    def __init__(self, *text_parts, **kwargs):
        """``include_underline=True`` 会添加下划线（默认添加）

        ``underline_width`` 下划线的长度（默认屏幕宽-2个单位）

        ``match_underline_width_to_text=True`` 时将下划线的长度和文字匹配（默认为False）
        """
        TextMobject.__init__(self, *text_parts, **kwargs)
        self.scale(self.scale_factor)
        self.to_edge(UP)
        if self.include_underline:
            underline = Line(LEFT, RIGHT)
            underline.next_to(self, DOWN, buff=self.underline_buff)
            if self.match_underline_width_to_text:
                underline.match_width(self)
            else:
                underline.set_width(self.underline_width)
            self.add(underline)
            self.underline = underline
