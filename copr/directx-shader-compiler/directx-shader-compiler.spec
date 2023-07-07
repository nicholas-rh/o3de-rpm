%global		toolchain clang

Name:		directx-shader-compiler
Version:	1.6.2112
Release:	1%{?dist}
Summary:	Compiler and tools to compile High-Level Shader Language (HLSL)
URL:		https://github.com/microsoft/DirectXShaderCompiler
License:	Apache-2.0 and MIT and NCSA

# generated using generate_tarball.sh
Source0:	directx-shader-compiler.tar.gz

Patch0:         clang_uint32_t.patch

BuildRequires:	g++
BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	python3-devel

# git submodules
Provides:	bundled(directx-headers)
Provides:	bundled(effcee)
Provides:	bundled(spirv-headers-devel)
Provides:	bundled(spirv-tools)
Provides:	bundled(re2)

%description
The DirectX Shader Compiler project includes a compiler and related tools used
to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate
Language (DXIL) representation. Applications that make use of DirectX for
graphics, games, and computation can use it to generate shader programs.

%prep
%setup -n directx-shader-compiler

pushd %{_builddir}/directx-shader-compiler
%patch 0
popd

%build
# Pulled from the o3de package build config
%cmake  -GNinja                                         \
        -DCMAKE_BUILD_TYPE=Release                      \
        -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON         \
        -DLLVM_APPEND_VC_REV:BOOL=ON                    \
        -DLLVM_DEFAULT_TARGET_TRIPLE:STRING=dxil-ms-dx  \
        -DLLVM_ENABLE_EH:BOOL=ON                        \
        -DLLVM_ENABLE_RTTI:BOOL=ON                      \
        -DLLVM_INCLUDE_DOCS:BOOL=OFF                    \
        -DLLVM_INCLUDE_EXAMPLES:BOOL=OFF                \
        -DLLVM_INCLUDE_TESTS:BOOL=OFF                   \
        -DLLVM_OPTIMIZED_TABLEGEN:BOOL=OFF              \
        -DLLVM_REQUIRES_EH:BOOL=ON                      \
        -DLLVM_REQUIRES_RTTI:BOOL=ON                    \
        -DLLVM_TARGETS_TO_BUILD:STRING=None             \
        -DLIBCLANG_BUILD_STATIC:BOOL=ON                 \
        -DCLANG_BUILD_EXAMPLES:BOOL=OFF                 \
        -DCLANG_CL:BOOL=OFF                             \
        -DCLANG_ENABLE_ARCMT:BOOL=OFF                   \
        -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=OFF         \
        -DCLANG_INCLUDE_TESTS:BOOL=OFF                  \
        -DHLSL_INCLUDE_TESTS:BOOL=OFF                   \
        -DENABLE_SPIRV_CODEGEN:BOOL=ON                  \
        -DSPIRV_BUILD_TESTS:BOOL=OFF                    \
        -DBUILD_SHARED_LIBS:BOOL=OFF                    \
        -DSPIRV_WERROR:BOOL=OFF                         \
        -DCMAKE_C_COMPILER=clang                        \
        -DCMAKE_CXX_COMPILER=clang++

%cmake_build --target all

%install
%cmake_install

mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}/usr/src
rm -rf %{buildroot}%{_datadir}/llvm
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_bindir}/llvm-tblgen
rm -rf %{buildroot}%{_bindir}/opt

%files
%license LICENSE.TXT
%doc README.md
%{_bindir}/dx*
%{_libdir}/libdxcompiler.so*

%changelog
* Fri Jun 30 2023 Nicholas Frizzell <nfrizzel@redhat.com> 1.6.2112-0
- Update version, other misc. changes to get it building

* Wed Jul  7 2021 Tom Callaway <spot@fedoraproject.org> 1.6.2104-2
- BR: git

* Tue Jun 22 2021 Tom Callaway <spot@fedoraproject.org> 1.6.2104-1
- initial package
