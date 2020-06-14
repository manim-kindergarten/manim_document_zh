[![manim_document_zh](source/assets/image/DocumentHeader.png)](https://github.com/manim-kindergarten/manim_document_zh)

[![GPL License](https://img.shields.io/github/license/manim-kindergarten/manim_document_zh)](https://choosealicense.com/licenses/gpl-3.0/)
![QQ](https://img.shields.io/badge/QQ-862671480-red.svg?style=flat)
[![manim_sandbox](https://img.shields.io/badge/mk-manim__sandbox-brightgreen.svg)](https://github.com/manim-kindergarten/manim_sandbox/)
[![manim](https://img.shields.io/badge/manim-ver.MK-orange.svg)](https://github.com/manim-kindergarten/manim)
[![tutorial](https://img.shields.io/badge/tutorial-on_bilibili-ff69b4.svg)](https://space.bilibili.com/171431343/favlist?fid=947158443)


[manim-kindergarten](https://github.com/manim-kindergarten/)成员整理的一份manim中文文档教程

### 文档地址
https://manim.ml/

还在完善中，目前完成情况：
- [x] 安装指南
- [x] 快速入门
- [x] constants
- [x] container
- [x] animation
- [ ] mobject
- [ ] scene
- [ ] camera
- [x] utils

### 关于构建文档

python安装Sphinx之后`make html`，生成网页。
`make pdf`则是生成pdf，配置文件是conf.py，可以修改主题。

html文档支持中文搜索，需要安装sphinx插件要安装```pip install jieba```

不习惯reStructuredText语法的可以pandoc把markdown等文件转换rst，或者JupyterNoteBook把py等文件转换rst。

```bash
pandoc readme.md --from markdown --to rst -s -o readme.rst
```

或者

```bash
pip install pypandoc
```

然后

```python
import pypandoc
output = pypandoc.convert_file('somefile.md', 'rst').replace("\r", "")
with open("outputfile.rst", "w", encoding="utf8") as f:
    f.write(output)
```

