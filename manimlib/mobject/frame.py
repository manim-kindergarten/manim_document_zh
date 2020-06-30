from manimlib.constants import *
from manimlib.mobject.geometry import Rectangle
from manimlib.utils.config_ops import digest_config


class ScreenRectangle(Rectangle):
    """和画面宽高比相同的矩形"""
    CONFIG = {
        "aspect_ratio": 16.0 / 9.0,
        "height": 4
    }

    def __init__(self, **kwargs):
        """- 宽高比为 ``aspect_ratio`` ，默认为16/9
        - 高度为 ``height``
        """
        Rectangle.__init__(self, **kwargs)
        self.set_width(
            self.aspect_ratio * self.get_height(),
            stretch=True
        )


class FullScreenRectangle(ScreenRectangle):
    CONFIG = {
        "height": FRAME_HEIGHT,
    }

    def __init__(self, **kwargs):
        """全屏幕大小的矩形"""
        super().__init__(**kwargs)


class FullScreenFadeRectangle(FullScreenRectangle):
    CONFIG = {
        "stroke_width": 0,
        "fill_color": BLACK,
        "fill_opacity": 0.7,
    }

    def __init__(self, **kwargs):
        """全屏幕大小的矩形（默认无线条，填充黑色，不透明度0.7）"""
        super().__init__(**kwargs)


class PictureInPictureFrame(Rectangle):
    CONFIG = {
        "height": 3,
        "aspect_ratio": 16.0 / 9.0
    }

    def __init__(self, **kwargs):
        """和 ``ScreenRectangle`` 类似"""
        digest_config(self, kwargs)
        Rectangle.__init__(
            self,
            width=self.aspect_ratio * self.height,
            height=self.height,
            **kwargs
        )
