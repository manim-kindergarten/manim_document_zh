曲面贴图 Textured surface
===================================

Vertex shader
**********************

参数列表
----------------------

=========  ===============  =========================  =======================
参数类型     数据类型          变量名                       说明
=========  ===============  =========================  =======================
in          ``vec3``        ``point``                   曲面顶点
in          ``vec3``        ``du_point``                u 分量顶点
in          ``vec3``        ``dv_point``                v 分量顶点
in          ``vec2``        ``im_coords``               坐标系
in          ``float``       ``opacity``                 透明度
out         ``vec3``        ``xyz_coords``              传给 frag 的 xyz 坐标系
out         ``vec3``        ``v_normal``                传给 frag 的法向量
out         ``vec2``        ``v_im_coords``             传给 frag 的坐标系
out         ``float``       ``v_opacity``               传给 frag 的透明度
=========  ===============  =========================  =======================


Fragment shader
**********************

参数列表
----------------------

=========  ===============  =========================  =======================
参数类型     数据类型          变量名                       说明
=========  ===============  =========================  =======================
uniform     ``sample2D``    ``LightTexture``            受光面材质
uniform     ``sample2D``    ``DarkTexture``             背光面材质
uniform     ``float``       ``num_textures``            材质数量
uniform     ``vec3``        ``light_source_position``   光源位置
uniform     ``vec3``        ``camera_position``         相机位置
uniform     ``float``       ``reflectiveness``          反光度
uniform     ``float``       ``gloss``                   光泽
uniform     ``float``       ``shadow``                  阴影
uniform     ``float``       ``focal_distance``          焦距
in          ``vec3``        ``xyz_coords``              xyz 坐标系
in          ``vec3``        ``v_normal``                法向量
in          ``vec2``        ``v_im_coords``             坐标系
in          ``float``       ``v_opacity``               透明度
out         ``vec4``        ``frag_color``              片段颜色
=========  ===============  =========================  =======================

程序流程
**********************


