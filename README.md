[![manim_document_zh](source/assets/image/DocumentHeader.png)](https://github.com/manim-kindergarten/manim_document_zh)

![docs](https://github.com/manim-kindergarten/manim_document_zh/workflows/docs/badge.svg)
[![GPL License](https://img.shields.io/github/license/manim-kindergarten/manim_document_zh)](https://choosealicense.com/licenses/gpl-3.0/)
![QQ](https://img.shields.io/badge/QQ-862671480-red.svg?style=flat)
[![manim_sandbox](https://img.shields.io/badge/mk-manim__sandbox-brightgreen.svg)](https://github.com/manim-kindergarten/manim_sandbox/)
[![manim](https://img.shields.io/badge/manim-ver.MK-orange.svg)](https://github.com/manim-kindergarten/manim)
[![tutorial](https://img.shields.io/badge/tutorial-on_bilibili-ff69b4.svg)](https://space.bilibili.com/171431343/favlist?fid=947158443)

[manim-kindergarten](https://github.com/manim-kindergarten/)成员整理的一份manim中文文档教程，目前还在完善当中。如果关于文档内容有问题，可以在这个repo中提出issue。
如果你想要为这个文档做出贡献，可以提交pr。详细内容见[贡献规则及编写指南](https://manim.ml/contribution.html)页面。

[`manim`](https://github.com/manim-kindergarten/manim_document_zh/tree/manim)分支中为带有文档字符串的manim源码，用于文档中自动构建文档字符串。

## 文档地址
https://manim.ml/

还在完善中，目前完成情况：
- [x] 安装指南
- [x] 快速入门
- [x] constants
- [x] container
- [x] animation
- [ ] mobject
- [ ] scene
- [x] camera
- [x] utils

## 关于文档构建
当前这个repo使用了[GitHub Actions](https://github.com/features/actions)和`Sphinx`自动构建文档。当向`master`分支`push`后，会自动触发构建部署在
[GitHub Pages](https://manim.ml/)和[Netlify](https://app.netlify.com/sites/manim-doc/overview)上。向`master`分支提出pr后，会触发构建，并且部署在[Netlify](https://app.netlify.com/sites/manim-doc/overview)上提供预览。

### 手动构建文档

**Step 1.** 安装环境：
- 确保安装了[manim](https://github.com/3b1b/manim/)环境
- `pip install -r requirements.txt` 安装文档环境

**Step 2.** 准备目录结构：
```text
.
├── manim/
│   ├── manimlib/
│   ├── manim_sandbox/
│   ├── ...
│   └── manim.py
└── manim_document_zh/
    ├── source/
    │   ├── ...
    │   └── conf.py
    ├── ...
    ├── make.bat
    └── Makefile 
```

**Step 3.** 构建文档：

在`manim_document_zh`文件夹中执行`make html`构建文档

**附.** 文件格式转换：

sphinx要求使用rst格式(reStructuredText语法)，可以使用pandoc把markdown等文件转换rst，或者JupyterNoteBook把py等文件转换rst。

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
