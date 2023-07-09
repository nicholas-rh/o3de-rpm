git clone https://github.com/aws/aws-sdk-cpp
pushd aws-sdk-cpp
git checkout 78ef64daf78e1c6bc95b1545ee91fbf4659d6536 # 1.9.50 tag
git submodule update --init --recursive
popd
tar -czvf aws-sdk-cpp.tar.gz aws-sdk-cpp
rm -rf aws-sdk-cpp
