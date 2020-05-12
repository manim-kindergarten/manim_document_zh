from manimlib.imports import *
svg_path = 'my_code\\files\\svg\\'


class Show_SVG_test(Scene):

    def construct(self):

        monster = SVGMobject(svg_path + 'monsters\\kidaha-01.svg').scale(2.5)

        st0 = '#C783B7'
        st1 = '#125785'
        st2 = '#8E4C87'
        st3 = '#1B70B6'
        st4 = '#66A0D7'
        st5 = '#1E1F1D'
        st6 = '#A3201B'
        st7 = '#E32D28'
        st8 = BLUE_D
        st9 = '#FFFFFF'

        list_1 = [st0, st1, st0, st1, st2, st3, st1, st0, st2, st3, st3, st2]
        list_2 = [st0, st3, st3, st3, st2, st2, st2, st0, st1, st1, st0, st1]
        list_3 = [st4]
        list_4 = [st5, st6, st7]
        list_5 = [st8, st9, st9, st5, st9]

        color_list = list_1 + list_2 + list_3 + list_4 + list_5

        for i in range(len(color_list)):
            monster[i].set_color(color_list[i])


        self.play(ShowCreation(monster))

        self.wait()

st0 = '#C783B7'
st1 = '#125785'
st2 = '#8E4C87'
st3 = '#1B70B6'
st4 = '#66A0D7'
st5 = '#1E1F1D'
st6 = '#A3201B'
st7 = '#E32D28'
st8 = BLUE_D
st9 = '#FFFFFF'

class Monster(VMobject):

    CONFIG = {
        'scale_factor': 2,
        'body_color': st4,
        'location': ORIGIN,
        # 'file_name': 'monsters\\kidaha-01.svg',

    }

    def create_monster_a(self):

        self.monster = SVGMobject(svg_path + 'monsters\\kidaha-01.svg').scale(self.scale_factor).move_to(self.location)

        list_1 = [st0, st1, st0, st1, st2, st3, st1, st0, st2, st3, st3, st2]
        list_2 = [st0, st3, st3, st3, st2, st2, st2, st0, st1, st1, st0, st1]
        list_3 = [self.body_color]
        list_4 = [st5, st6, st7]
        list_5 = [st8, st9, st9, st5, st9]

        color_list = list_1 + list_2 + list_3 + list_4 + list_5

        for i in range(len(color_list)):
            self.monster[i].set_color(color_list[i])

        return self.monster

    def create_monster_b(self):
        pass

class Show_SVG(Scene):

    def construct(self):

        monster = Monster(body_color=PINK, location=LEFT * 4. + DOWN * 1.8, scale_factor=2).create_monster_a()

        self.play(ShowCreation(monster))
        self.wait()

        bubble = SVGMobject(svg_path + 'Bubbles_speech.svg', fill_opacity=0, stroke_width=4).scale(2.4)\
            .next_to(monster, RIGHT + UP).shift(LEFT * 1 + DOWN * 1.8)
        words = TextMobject('大家好，我是Cigar666！').move_to(bubble).shift(UP * 0.6)

        self.play(ShowCreation(bubble))
        self.play(Write(words))

        self.wait()

