InstallationProblems安装问题
===============================

.. _installationProblem:


**Q1:**\ 使用 anaconda，命令行输入 python 


无反应或报错 考虑 path 环境变量是否填全(安装anaconda时是否勾选添加到path变量)，path 变量里应该有

.. code::

   <your_path>\Anaconda3; <your_path>\Anaconda3\Scripts; <your_path>\Anaconda3\Library\bin;


**Q2:**\ pip install ... 时满屏红字报错，或者安装过慢


更换国内镜像源，使用
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
代替2
pip install -r requirements.txt


**Q3:**\  pip 安装 pycairo 总是失败 

下载 pycairo 对应版本的 whl 包

.. code::

   pycairo-1.18.2-cp37-cp37m-win_amd64.whl


并手动安装

.. code:: 

   pip install pycairo......whl


**Q4:**\  pip 安装过包，但运行时提示没有模块 

考虑电脑上是否有多个 Python，确定 pip 把包装到了哪个 Python 上面



