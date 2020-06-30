cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim
cd manim
git clone https://github.com/manim-kindergarten/manim_sandbox.git
cd ../repo

apt install python3-pip -y
python3 -m pip --version
wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
tar -zxvf setuptools-19.6.tar.gz
cd setuptools-19.6
python3 setup.py build
python3 setup.py install
cd ..

cd ..
git clone https://github.com/sphinx-doc/sphinx
cd sphinx
python3 -m pip install .
python3 -m pip install sphinx_rtd_theme
python3 -m pip install jieba
cd ../repo

cd ../manim
python3 -m pip install -r requirements.txt

make html