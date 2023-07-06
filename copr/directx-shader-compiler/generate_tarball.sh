git clone https://github.com/microsoft/DirectXShaderCompiler directx-shader-compiler
pushd directx-shader-compiler
git checkout e09a454eb67c21ef8d196ef7319df06028f8fe52 # 1.7.2212 tag
git submodule update --init --recursive
popd
tar -czvf directx-shader-compiler.tar.gz directx-shader-compiler
rm -rf directx-shader-compiler
