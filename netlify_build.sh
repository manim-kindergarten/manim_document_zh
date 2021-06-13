cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim_with_doc
cd manim_with_doc
git clone https://github.com/manim-kindergarten/manim_sandbox.git
python -m pip --version
python -m pip install -r requirements.txt
pwd
cd ../repo
# export PATH="$PATH:/home/runner/.local/bin:/home/runner/manim_document_zh/manim_with_doc"
make html

cd shaders
make html
mv build/html ../build/html/shaders
cd ..