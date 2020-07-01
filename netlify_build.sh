cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim
cd manim
git clone https://github.com/manim-kindergarten/manim_sandbox.git
cd ../repo

python --version
python -m pip --version

cd ..
git clone https://github.com/sphinx-doc/sphinx
cd sphinx
python -m pip install .
python -m pip install sphinx_rtd_theme
python -m pip install jieba
cd ../repo

cd ../manim
python -m pip install -r requirements.txt
cd ../repo

make html