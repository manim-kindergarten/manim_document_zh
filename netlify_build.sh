# Clone pre repositories
cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim
cd manim
git clone https://github.com/manim-kindergarten/manim_sandbox.git
cd ..
ls
python --version
pip --version
python3 --version
python3 -m pip --version

# Install sphinx
git clone https://github.com/sphinx-doc/sphinx
cd sphinx
pip3 install .
pip3 install sphinx_rtd_theme
pip3 install jieba
cd ..

# Install manim env
cd ../manim
pip3 install -r requirements.txt
cd ../manim_document_zh

# Build document with Sphinx
make html