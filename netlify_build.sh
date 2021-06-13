cd ..
git clone -b manim https://github.com/manim-kindergarten/manim_document_zh.git manim_with_doc
cd manim_with_doc
git clone https://github.com/manim-kindergarten/manim_sandbox.git

cd repo

make html

cd shaders
make html
mv build/html ../build/html/shaders
cd ..