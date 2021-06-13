# Clone pre repositries and Install python requirements
cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim_with_doc
cd manim_with_doc
git clone https://github.com/manim-kindergarten/manim_sandbox.git
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cd ../repo

# Build doc
make html

# Build doc for shaders
cd shaders
make html
mv build/html ../build/html/shaders
cd ..