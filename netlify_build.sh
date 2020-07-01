cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim
cd manim
git clone https://github.com/manim-kindergarten/manim_sandbox.git

cd ..
python -m pip uninstall sphinx -y
git clone https://github.com/sphinx-doc/sphinx
cd sphinx
python -m pip install .
cd ../repo

make html