# Clone pre repositries and Install python requirements
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim_with_doc
cd manim_with_doc
git clone https://github.com/manim-kindergarten/manim_sandbox.git
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cd ..

# Build doc
cd cairo-backend
make html
mkdir -p ../build/html/cairo-backend
mv build/html/* ../build/html/cairo-backend/

# Build doc for shaders
cd ..
git clone https://github.com/manim-kindergarten/manim.git manim_cn 
cd manim_cn 
pip install .
pip install -r docs/requirements.txt 
cd docs
make html
mv build/html/* ../../build/html/
cd ..