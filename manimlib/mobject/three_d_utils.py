import numpy as np

from manimlib.constants import ORIGIN
from manimlib.constants import UP
from manimlib.utils.space_ops import get_norm
from manimlib.utils.space_ops import get_unit_normal


def get_3d_vmob_gradient_start_and_end_points(vmob):
    """获取三维物体 ``vmob`` 光照着色梯度开始和结束的点"""
    return (
        get_3d_vmob_start_corner(vmob),
        get_3d_vmob_end_corner(vmob),
    )


def get_3d_vmob_start_corner_index(vmob):
    """获取三维物体 ``vmob`` 光照着色梯度开始的点在点集中的索引"""
    return 0


def get_3d_vmob_end_corner_index(vmob):
    """获取三维物体 ``vmob`` 光照着色梯度结束的点在点集中的索引"""
    return ((len(vmob.points) - 1) // 6) * 3


def get_3d_vmob_start_corner(vmob):
    """获取三维物体 ``vmob`` 光照着色梯度开始的点"""
    if vmob.get_num_points() == 0:
        return np.array(ORIGIN)
    return vmob.points[get_3d_vmob_start_corner_index(vmob)]


def get_3d_vmob_end_corner(vmob):
    """获取三维物体 ``vmob`` 光照着色梯度结束的点"""
    if vmob.get_num_points() == 0:
        return np.array(ORIGIN)
    return vmob.points[get_3d_vmob_end_corner_index(vmob)]


def get_3d_vmob_unit_normal(vmob, point_index):
    """获取三维物体 ``vmob`` 在 ``point_index`` 点处的法线（单位向量）"""
    n_points = vmob.get_num_points()
    if len(vmob.get_anchors()) <= 2:
        return np.array(UP)
    i = point_index
    im3 = i - 3 if i > 2 else (n_points - 4)
    ip3 = i + 3 if i < (n_points - 3) else 3
    unit_normal = get_unit_normal(
        vmob.points[ip3] - vmob.points[i],
        vmob.points[im3] - vmob.points[i],
    )
    if get_norm(unit_normal) == 0:
        return np.array(UP)
    return unit_normal


def get_3d_vmob_start_corner_unit_normal(vmob):
    """获取三维物体 ``vmob`` 在光照着色梯度开始的点处的法线（单位向量）"""
    return get_3d_vmob_unit_normal(
        vmob, get_3d_vmob_start_corner_index(vmob)
    )


def get_3d_vmob_end_corner_unit_normal(vmob):
    """获取三维物体 ``vmob`` 在光照着色梯度结束的点处的法线（单位向量）"""
    return get_3d_vmob_unit_normal(
        vmob, get_3d_vmob_end_corner_index(vmob)
    )
