# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../../manim_with_doc/"))

project = 'manim'
copyright = '2020-2021 Manim Kindergarten Team'
author = 'manim-kindergarten'

version = '1.0.0'
release = ''

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'manim_example_ext'
]

autoclass_content = 'both'
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'zh_CN'
html_search_language = 'zh'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'remain']
pygments_style = 'default'

html_static_path = ['assets']
html_css_files = [
    "https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/custom.css", 
    "https://cdn.jsdelivr.net/gh/manim-kindergarten/CDN@master/manim_assets/colors.css"
]
html_theme = 'furo'  # pip install furo==2020.10.5b9
html_favicon = 'mk.png'
html_logo = 'assets/image/Logo_white.png'
html_theme_options = {
    "sidebar_hide_name": True,
}