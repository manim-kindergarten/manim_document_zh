# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath("../../manim/"))

project = 'manim'
copyright = '- This document has been placed in the public domain.'
# author = '2019EulerTour'
# author = '2019elteoremadebeethoven'
author = 'manim-kindergarten'

version = '0.4.0'
release = ''

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme'
]

autoclass_content = 'both'
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'zh_CN'
html_search_language = 'zh'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'remain/']
pygments_style = 'default'

html_static_path = ['assets']
html_theme = 'sphinx_rtd_theme'
html_favicon = 'mk.png'
html_logo = 'assets/image/Logo_black.png'
html_theme_options = {
    'logo_only': True,
    'style_nav_header_background': '#343131',
}
