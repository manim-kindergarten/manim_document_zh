import numpy as np

from PIL import Image

from manimlib.constants import *
from manimlib.mobject.mobject import Mobject
from manimlib.mobject.shape_matchers import SurroundingRectangle
from manimlib.utils.bezier import interpolate
from manimlib.utils.color import color_to_int_rgb
from manimlib.utils.config_ops import digest_config
from manimlib.utils.images import get_full_raster_image_path


class AbstractImageMobject(Mobject):
    """图片的"抽象"类"""
    CONFIG = {
        "height": 2.0,
        "pixel_array_dtype": "uint8",
    }

    def get_pixel_array(self):
        """给子类实现"""
        raise Exception("Not implemented")

    def set_color(self):
        """给子类实现"""
        # Likely to be implemented in subclasses, but no obgligation
        pass

    def reset_points(self):
        """点集为图片左上右上左下三个点，实现了定位"""
        # Corresponding corners of image are fixed to these 3 points
        self.points = np.array([
            UP + LEFT,
            UP + RIGHT,
            DOWN + LEFT,
        ])
        self.center()
        h, w = self.get_pixel_array().shape[:2]
        self.stretch_to_fit_height(self.height)
        self.stretch_to_fit_width(self.height * w / h)

    def copy(self):
        return self.deepcopy()


class ImageMobject(AbstractImageMobject):
    """图片物体"""
    CONFIG = {
        "invert": False,
        "image_mode": "RGBA",
    }

    def __init__(self, filename_or_array, **kwargs):
        """初始化输入的 ``filename_or_array`` 指向了图片文件的位置
        
        ``invert=True`` 表示反色
        """
        digest_config(self, kwargs)
        if isinstance(filename_or_array, str):
            path = get_full_raster_image_path(filename_or_array)
            image = Image.open(path).convert(self.image_mode)
            self.pixel_array = np.array(image)
        else:
            self.pixel_array = np.array(filename_or_array)
        self.change_to_rgba_array()
        if self.invert:
            self.pixel_array[:, :, :3] = 255 - self.pixel_array[:, :, :3]
        AbstractImageMobject.__init__(self, **kwargs)

    def change_to_rgba_array(self):
        """将输入的 ``pixel_array`` 转换为rgba数组"""
        pa = self.pixel_array
        if len(pa.shape) == 2:
            pa = pa.reshape(list(pa.shape) + [1])
        if pa.shape[2] == 1:
            pa = pa.repeat(3, axis=2)
        if pa.shape[2] == 3:
            alphas = 255 * np.ones(
                list(pa.shape[:2]) + [1],
                dtype=self.pixel_array_dtype
            )
            pa = np.append(pa, alphas, axis=2)
        self.pixel_array = pa

    def get_pixel_array(self):
        """获取像素数组 ``pixel_array``"""
        return self.pixel_array

    def set_color(self, color, alpha=None, family=True):
        """将像素全部转化为color颜色"""
        rgb = color_to_int_rgb(color)
        self.pixel_array[:, :, :3] = rgb
        if alpha is not None:
            self.pixel_array[:, :, 3] = int(255 * alpha)
        for submob in self.submobjects:
            submob.set_color(color, alpha, family)
        self.color = color
        return self

    def set_opacity(self, alpha):
        """设置图片不透明度"""
        self.pixel_array[:, :, 3] = int(255 * alpha)
        return self

    def fade(self, darkness=0.5, family=True):
        """利用不透明度来变暗"""
        self.set_opacity(1 - darkness)
        super().fade(darkness, family)
        return self

    def interpolate_color(self, mobject1, mobject2, alpha):
        """两张图片之间插值，``pixel_array`` 必须一样大"""
        assert(mobject1.pixel_array.shape == mobject2.pixel_array.shape)
        self.pixel_array = interpolate(
            mobject1.pixel_array, mobject2.pixel_array, alpha
        ).astype(self.pixel_array_dtype)

# TODO, add the ability to have the dimensions/orientation of this
# mobject more strongly tied to the frame of the camera it contains,
# in the case where that's a MovingCamera


class ImageMobjectFromCamera(AbstractImageMobject):
    """从camera中获取图片的类"""
    CONFIG = {
        "default_display_frame_config": {
            "stroke_width": 3,
            "stroke_color": WHITE,
            "buff": 0,
        }
    }

    def __init__(self, camera, **kwargs):
        """初始化需要传入一个相机，用于获取图像"""
        self.camera = camera
        AbstractImageMobject.__init__(self, **kwargs)

    def get_pixel_array(self):
        """从相机中获取图像"""
        return self.camera.get_pixel_array()

    def add_display_frame(self, **kwargs):
        """在画面中显示当前图像（一个矩形框起来）"""
        config = dict(self.default_display_frame_config)
        config.update(kwargs)
        self.display_frame = SurroundingRectangle(self, **config)
        self.add(self.display_frame)
        return self
