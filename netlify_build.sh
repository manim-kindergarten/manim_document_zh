cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim
cd manim
git clone https://github.com/manim-kindergarten/manim_sandbox.git
cd ../repo

# mkdir /usr/lib/python3.5/site-packages/

# wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
# tar -zxvf setuptools-19.6.tar.gz
# cd setuptools-19.6
# python3 setup.py build
# python3 setup.py install
# cd ..

# wget --no-check-certificate https://pypi.python.org/packages/source/p/pip/pip-18.1.tar.gz
# tar -zxvf pip-18.1.tar.gz 
# cd pip-18.1
# python3 setup.py build
# python3 setup.py install
# cd ..
# python3 -m pip --version

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

make html