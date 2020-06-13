# Manim-Document-zh

[manim-kindergarten](https://github.com/manim-kindergarten/)成员整理的一份manim中文文档教程

### 文档地址
https://manim-kindergarten.github.io/manim_document_zh/

还在完善中

### 关于构建文档

python安装Sphinx之后`make html`，生成网页，能在本地修改整理自己的manim笔记系统，用以备忘查询。`make pdf`则是生成pdf，配置文件是conf.py，可以修改主题。markdown/latex可以用pandoc转rst，*.py文件可以用jupyter转rst。

第七章用到sphinx自动文档插件，需要在python搜索路径添加manim保存位置变量，方法有很多：

1. ```sys.path.append("c:\\你的本地磁盘manim位置")```

2. 或者manim的本地位置添加到PYTHONPATH环境变量。



```python
import sys
sys.path #查看路径是否添加成功
import manim #不报错说明添加成功
```

html文档支持中文搜索，需要安装sphinx插件要安装```pip install jieba```

不习惯ReStructuredText语法的可以Pandoc把Makrdown等文件转换rst，或者JupyterNoteBook把py等文件转换rst。

其实建议使用Pandoc：

`pandoc readme.md --from markdown --to rst -s -o readme.rst`

或者

`pip install pypandoc`

然后

```
import pypandoc
output = pypandoc.convert('somefile.md', 'rst')
```

