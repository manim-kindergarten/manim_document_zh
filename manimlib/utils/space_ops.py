from functools import reduce

import numpy as np

from manimlib.constants import OUT
from manimlib.constants import PI
from manimlib.constants import RIGHT
from manimlib.constants import TAU
from manimlib.utils.iterables import adjacent_pairs
from manimlib.utils.simple_functions import fdiv


def get_norm(vect):
    """模长"""
    return sum([x**2 for x in vect])**0.5


# Quaternions
# TODO, implement quaternion type


def quaternion_mult(q1, q2):
    """四元数相乘"""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2,
        w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2,
    ])


def quaternion_from_angle_axis(angle, axis):
    """
    根据轴-角确定的用于旋转的四元数
    [cos(θ/2), sin(θ/2)u]
    """
    return np.append(
        np.cos(angle / 2),
        np.sin(angle / 2) * normalize(axis)
    )


def angle_axis_from_quaternion(quaternion):
    """从四元数确定旋转轴-角"""
    axis = normalize(
        quaternion[1:],
        fall_back=np.array([1, 0, 0])
    )
    angle = 2 * np.arccos(quaternion[0])
    if angle > TAU / 2:
        angle = TAU - angle
    return angle, axis


def quaternion_conjugate(quaternion):
    """共轭四元数"""
    result = np.array(quaternion)
    result[1:] *= -1
    return result


def rotate_vector(vector, angle, axis=OUT):
    """旋转向量 2D-复数运算 3D-四元数qvq_inv"""
    if len(vector) == 2:
        # Use complex numbers...because why not
        z = complex(*vector) * np.exp(complex(0, angle))
        return np.array([z.real, z.imag])
    elif len(vector) == 3:
        # Use quaternions...because why not
        quat = quaternion_from_angle_axis(angle, axis)   # 从角-轴确定旋转四元数
        quat_inv = quaternion_conjugate(quat)            # 共轭四元数
        product = reduce(  # qvq_inv
            quaternion_mult,
            [quat, np.append(0, vector), quat_inv]
        )
        return product[1:]
    else:
        raise Exception("vector must be of dimension 2 or 3")


def thick_diagonal(dim, thickness=2):
    """
    对角线为1 其余为0，对角线宽度由thickness决定

        >>> thick_diagonal(3, 1)
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]  
        >>> thick_diagonal(3, 2)
        [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]

    """
    row_indices = np.arange(dim).repeat(dim).reshape((dim, dim))  # [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
    col_indices = np.transpose(row_indices)                       # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    return (np.abs(row_indices - col_indices) < thickness).astype('uint8')


def rotation_matrix(angle, axis):
    """
    通过轴-角确定旋转矩阵
    """
    about_z = rotation_about_z(angle)       # 沿z轴的旋转
    z_to_axis = z_to_vector(axis)           # 把z轴转到axis的矩阵
    axis_to_z = np.linalg.inv(z_to_axis)    # 把axis转到z轴
    return reduce(np.dot, [z_to_axis, about_z, axis_to_z])  # 先把axis转到z轴再沿z旋转后将z轴转到axis


def rotation_about_z(angle):
    """沿z轴旋转angle角(右手螺旋)"""
    return [
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ]


def z_to_vector(vector):
    """
    返回能使z轴变换到vector的矩阵
    """
    norm = get_norm(vector)
    if norm == 0:
        return np.identity(3)
    v = np.array(vector) / norm  # 化为单位向量
    phi = np.arccos(v[2])        # 需要沿y轴旋转的角度
    if any(v[:2]): # v不与z轴重合
        axis_proj = v[:2] / get_norm(v[:2]) # 投影到xy平面单位圆上
        theta = np.arccos(axis_proj[0])     # 需要沿z轴旋转的角度
        if axis_proj[1] < 0: # 转换为正数
            theta = -theta
    else: # v与z轴重合
        theta = 0
    phi_down = np.array([    # 沿y轴旋转phi
        [np.cos(phi), 0, np.sin(phi)],
        [0, 1, 0],
        [-np.sin(phi), 0, np.cos(phi)]
    ])
    return np.dot(rotation_about_z(theta), phi_down) # 先沿y轴旋转phi，再沿z轴旋转theta


def angle_between(v1, v2):
    """返回两向量夹角"""
    return np.arccos(np.dot(
        v1 / get_norm(v1),
        v2 / get_norm(v2)
    ))


def angle_of_vector(vector):
    """在xy平面上投影的极坐标θ"""
    z = complex(*vector[:2])
    if z == 0:
        return 0
    return np.angle(complex(*vector[:2]))


def angle_between_vectors(v1, v2):
    """返回两向量夹角"""
    return np.arccos(fdiv(
        np.dot(v1, v2),
        get_norm(v1) * get_norm(v2)
    ))


def project_along_vector(point, vector):
    matrix = np.identity(3) - np.outer(vector, vector)
    return np.dot(point, matrix.T)


def normalize(vect, fall_back=None):
    norm = get_norm(vect)
    if norm > 0:
        return np.array(vect) / norm
    else:
        if fall_back is not None:
            return fall_back
        else:
            return np.zeros(len(vect))


def cross(v1, v2):
    """两向量叉积"""
    return np.array([
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ])


def get_unit_normal(v1, v2):
    """法向量"""
    return normalize(cross(v1, v2))


###


def compass_directions(n=4, start_vect=RIGHT):
    """将TAU分成n份，从start_vect开始返回沿每个方向的单位向量"""
    angle = TAU / n
    return np.array([
        rotate_vector(start_vect, k * angle)
        for k in range(n)
    ])


def complex_to_R3(complex_num):
    """复数转化为坐标（z轴为0）"""
    return np.array((complex_num.real, complex_num.imag, 0))


def R3_to_complex(point):
    """取坐标前两轴为复数"""
    return complex(*point[:2])


def complex_func_to_R3_func(complex_func):
    """将复函数转化为针对坐标的函数"""
    return lambda p: complex_to_R3(complex_func(R3_to_complex(p)))


def center_of_mass(points):
    """获取点集的重心"""
    points = [np.array(point).astype("float") for point in points]
    return sum(points) / len(points)


def midpoint(point1, point2):
    """两点的中点"""
    return center_of_mass([point1, point2])


def line_intersection(line1, line2):
    """
    求两直线交点::

        point=line_intersection(line1.get_start_and_end(), line2.get_start_and_end())
    """
    x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(x_diff, y_diff)
    if div == 0:
        raise Exception("Lines do not intersect")
    d = (det(*line1), det(*line2))
    x = det(d, x_diff) / div
    y = det(d, y_diff) / div
    return np.array([x, y, 0])


def get_winding_number(points):
    """获取卷绕数（所有点一共绕过的角度）"""
    total_angle = 0
    for p1, p2 in adjacent_pairs(points):
        d_angle = angle_of_vector(p2) - angle_of_vector(p1)
        d_angle = ((d_angle + PI) % TAU) - PI
        total_angle += d_angle
    return total_angle / TAU
