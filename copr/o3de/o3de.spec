%global		BUNDLED_PACKAGE_URL	https://d3t6xeg4fgfoum.cloudfront.net
%global		THIRD_PARTY_PATH	%{_builddir}/3rdParty
%global		INSTALL_PATH		%{_libdir}/o3de
# Longer compilation times but smaller storage footprint
%global 	SAVE_DISK_SPACE		1

# Have to change this to appease the O3DE build system
%global		_vpath_builddir		%{_builddir}/%{name}-%{version}/build/linux_ninja

# Have to disable this check, I think this will be fixed when we stop importing prebuilt binaries
%global		_missing_build_ids_terminate_build 0
%global 	debug_package %{nil}

%global		toolchain clang

Name:		o3de
Version:	2305.0
Release:	1%{?dist}
Summary:	Open 3D Engine
License:	ASL 2.0 or MIT
URL:		https://o3de.org
ExclusiveArch:	x86_64

# The O3DE release URL
Source0:	https://github.com/o3de/o3de/releases/download/%{version}/%{name}-%{version}-lfs.tar.gz
# Vendored/bundled dependencies
Source1:	%{BUNDLED_PACKAGE_URL}/assimp-5.2.5-rev1-linux.tar.xz
Source2:	%{BUNDLED_PACKAGE_URL}/astc-encoder-3.2-rev2-linux.tar.xz
Source3:	%{BUNDLED_PACKAGE_URL}/AWSGameLiftServerSDK-3.4.2-rev1-linux.tar.xz
Source4:	%{BUNDLED_PACKAGE_URL}/AWSGameLiftServerSDK-5.0.0-rev2-linux.tar.xz
Source5:	%{BUNDLED_PACKAGE_URL}/AWSNativeSDK-1.9.50-rev2-linux-openssl-3.tar.xz
Source6:	%{BUNDLED_PACKAGE_URL}/AWSNativeSDK-1.9.50-rev3-linux.tar.xz
Source7:	%{BUNDLED_PACKAGE_URL}/azslc-1.8.15-rev2-linux.tar.xz
Source8:	%{BUNDLED_PACKAGE_URL}/cityhash-1.1-multiplatform.tar.xz
#Source9:	https://github.com/nicholas-rh/o3de-rpm/raw/master/copr/o3de/DirectXShaderCompilerDxc-1.6.2112-o3de-rev1-linux.tar.xz
Source10:	%{BUNDLED_PACKAGE_URL}/expat-2.4.2-rev2-linux.tar.xz
Source11:	%{BUNDLED_PACKAGE_URL}/freetype-2.11.1-rev1-linux.tar.xz
Source12:	%{BUNDLED_PACKAGE_URL}/googlebenchmark-1.7.0-rev1-linux.tar.xz
Source13:	%{BUNDLED_PACKAGE_URL}/googletest-1.8.1-rev4-linux.tar.xz
Source14:	%{BUNDLED_PACKAGE_URL}/ISPCTexComp-36b80aa-rev1-linux.tar.xz
Source15:	%{BUNDLED_PACKAGE_URL}/libsamplerate-0.2.1-rev2-linux.tar.xz
Source16:	%{BUNDLED_PACKAGE_URL}/Lua-5.4.4-rev1-linux.tar.xz
Source17:	%{BUNDLED_PACKAGE_URL}/lz4-1.9.4-rev2-linux.tar.xz
Source18:	%{BUNDLED_PACKAGE_URL}/mcpp-2.7.2_az.2-rev1-linux.tar.xz
Source19:	%{BUNDLED_PACKAGE_URL}/mikkelsen-1.0.0.4-linux.tar.xz
# The NvCloth license is not approved by Fedora
#Source20:	%{BUNDLED_PACKAGE_URL}/NvCloth-v1.1.6-4-gd243404-pr58-rev1-linux.tar.xz
Source21:	%{BUNDLED_PACKAGE_URL}/OpenEXR-3.1.3-rev4-linux.tar.xz
Source22:	%{BUNDLED_PACKAGE_URL}/openimageio-opencolorio-2.3.17-rev2-linux.tar.xz
Source23:	%{BUNDLED_PACKAGE_URL}/OpenMesh-8.1-rev3-linux.tar.xz
Source24:	%{BUNDLED_PACKAGE_URL}/PhysX-4.1.2.29882248-rev5-linux.tar.xz
Source25:	%{BUNDLED_PACKAGE_URL}/png-1.6.37-rev2-linux.tar.xz
Source26:	%{BUNDLED_PACKAGE_URL}/poly2tri-7f0487a-rev1-linux.tar.xz
Source27:	%{BUNDLED_PACKAGE_URL}/pybind11-2.10.0-rev1-multiplatform.tar.xz
Source28:	%{BUNDLED_PACKAGE_URL}/pyside2-5.15.2.1-py3.10-rev6-linux.tar.xz
Source29:	%{BUNDLED_PACKAGE_URL}/python-3.10.5-rev2-linux.tar.xz
Source30:	%{BUNDLED_PACKAGE_URL}/qt-5.15.2-rev8-linux.tar.xz
Source31:	%{BUNDLED_PACKAGE_URL}/RapidJSON-1.1.0-rev1-multiplatform.tar.xz
Source32:	%{BUNDLED_PACKAGE_URL}/RapidXML-1.13-rev1-multiplatform.tar.xz
Source33:	%{BUNDLED_PACKAGE_URL}/SPIRVCross-2021.04.29-rev1-linux.tar.xz
Source34:	%{BUNDLED_PACKAGE_URL}/SQLite-3.37.2-rev1-linux.tar.xz
Source35:	%{BUNDLED_PACKAGE_URL}/squish-ccr-deb557d-rev1-linux.tar.xz
Source36:	%{BUNDLED_PACKAGE_URL}/tiff-4.2.0.15-rev3-linux.tar.xz
Source37:	%{BUNDLED_PACKAGE_URL}/v-hacd-2.3-1a49edf-rev1-linux.tar.xz
Source38:	%{BUNDLED_PACKAGE_URL}/vulkan-validationlayers-1.2.198-rev1-linux.tar.xz
Source39:	%{BUNDLED_PACKAGE_URL}/xxhash-0.7.4-rev1-multiplatform.tar.xz
Source40:	%{BUNDLED_PACKAGE_URL}/zlib-1.2.11-rev5-linux.tar.xz
Source41:	%{BUNDLED_PACKAGE_URL}/zstd-1.35-multiplatform.tar.xz

# Use custom dxc 
Patch0: BuiltInPackages_linux.patch
# Remove -Werror to prevent extraneous compile errors
Patch1: Configurations_clang.patch
# Use lld
Patch2: Configurations_linux.patch
# Use custom dxc 
Patch3: SystemPackages_linux.patch
# Disable non-free gems/modules
Patch4: enginejson.patch
# Use custom dxc
Patch5: PAL_linux.patch
# This gem gives a compile error, need to fix eventually but disabling for now
Patch6: RecastNavigationCMakeLists.patch
# Fix clang-specific compile error
Patch7: RenderPass.patch
# Disable AWSCore gem in default template for now
Patch8: DefaultProjectproject.patch
# Disable AWS tool for now
Patch9: ToolsCMakeLists.patch
# Add bundled licenses
Patch10: NOTICES.patch
# Move zlib fix
Patch11: BuiltInPackages.patch
# Add envvar to allow for running as root user without issue
Patch12: LYPython.patch

BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	directx-shader-compiler
BuildRequires:	fontconfig-devel
BuildRequires:	ninja-build
BuildRequires:	openssl
BuildRequires:	openssl-devel
BuildRequires:	libatomic
BuildRequires:	libcurl-devel
BuildRequires:	libunwind-devel
BuildRequires:	libxcb-devel
BuildRequires:	libxkbcommon-x11-devel
BuildRequires:	libzstd-devel
BuildRequires:	lld
BuildRequires:	mesa-libGLU-devel
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	patchelf
BuildRequires:	qt5-qtbase-devel
BuildRequires:	zlib
BuildRequires:	zlib-devel

Requires: cmake%{?_isa}
Requires: clang%{?_isa}
Requires: directx-shader-compiler%{?_isa}
Requires: fontconfig-devel%{?_isa}
Requires: libcurl-devel%{?_isa}
Requires: libunwind-devel%{?_isa}
Requires: libxkbcommon-x11-devel%{?_isa}
Requires: libxcb-devel%{?_isa}
Requires: libzstd-devel%{?_isa}
Requires: mesa-libGLU-devel%{?_isa}
Requires: ninja-build%{?_isa}
Requires: openssl%{?_isa}
Requires: openssl-devel%{?_isa}
Requires: qt5-qtbase-devel%{?_isa}
Requires: zlib-devel%{?_isa}

Provides:	bundled(assimp) = 5.2.5
Provides:	bundled(astc-encoder) = 3.2
Provides:	bundled(AWSGameLiftServer) = 3.4.2
Provides:	bundled(AWSGameLiftServer) = 5.0.0
Provides:	bundled(AWSNativeSDK) = 1.9.50
Provides:	bundled(azslc) = 1.8.15
Provides:	bundled(cityhash) = 1.1
Provides:	bundled(expat) = 2.4.2
Provides:	bundled(freetype) = 2.11.1
Provides:	bundled(googlebenchmark) = 1.7.0
Provides:	bundled(googletest) = 1.8.1
Provides:	bundled(ISPCTexComp) = 36b80aa
Provides:	bundled(libsamplerate) = 0.2.1
Provides:	bundled(lua) = 5.4.4
Provides:	bundled(lz4) = 1.9.4
Provides:	bundled(mcpp) = 2.7.2
Provides:	bundled(mikktspace) = 1.0.0
Provides:	bundled(OpenEXR) = 3.1.3
Provides:	bundled(openimageio) = 2.3.17
Provides:	bundled(opencolorio) = 2.3.17
Provides:	bundled(OpenMesg) = 8.1
Provides:	bundled(PhysX) = 4.1.2
Provides:	bundled(libpng) = 1.6.37
Provides:	bundled(poly2tri) = 7f0487a
Provides:	bundled(python3) = 3.10.5
Provides:	bundled(python3-pybind11) = 2.10.0
Provides:	bundled(python3-pyside2) = 2.10.0
Provides:	bundled(qt5-qtbase) = 5.15.2
Provides:	bundled(RapidJSON) = 1.1.0
Provides:	bundled(RapidXML) = 1.13
Provides:	bundled(SPIRVCross) = 2021.04.29
Provides:	bundled(sqlite) = 3.37.2
Provides:	bundled(squish-ccr) = deb557d
Provides:	bundled(libtiff) = 4.2.0
Provides:	bundled(v-hacd) = 2.3.1
Provides:	bundled(vulkan-validation-layers) = 1.2.198
Provides:	bundled(xxhash) = 0.7.4
Provides:	bundled(zstd) = 1.35

%description
Open 3D Engine (O3DE) is an Apache 2.0-licensed multi-platform 3D engine that enables developers and content creators to build AAA games, cinema-quality 3D worlds, and high-fidelity simulations without any fees or commercial obligations. 

%prep
mkdir -p %{THIRD_PARTY_PATH}

%setup -c -n %{name}-%{version}

pushd %{THIRD_PARTY_PATH}
%setup -T -D -a 1
%setup -T -D -a 2
%setup -T -D -a 3
%setup -T -D -a 4
%setup -T -D -a 5
%setup -T -D -a 6
%setup -T -D -a 7
%setup -T -D -a 8
#%setup -T -D -a 9
%setup -T -D -a 10
%setup -T -D -a 11
%setup -T -D -a 12
%setup -T -D -a 13
%setup -T -D -a 14
%setup -T -D -a 15
%setup -T -D -a 16
%setup -T -D -a 17
%setup -T -D -a 18
%setup -T -D -a 19
# The NvCloth license is not approved for Fedora
#%setup -T -D -a 20
%setup -T -D -a 21
%setup -T -D -a 22
%setup -T -D -a 23
%setup -T -D -a 24
%setup -T -D -a 25
%setup -T -D -a 26
%setup -T -D -a 27
%setup -T -D -a 28
%setup -T -D -a 29
%setup -T -D -a 30
%setup -T -D -a 31
%setup -T -D -a 32
%setup -T -D -a 33
%setup -T -D -a 34
%setup -T -D -a 35
%setup -T -D -a 36
%setup -T -D -a 37
%setup -T -D -a 38
%setup -T -D -a 39
%setup -T -D -a 40
%setup -T -D -a 41
popd

pushd %{_builddir}/%{name}-%{version}
%patch 0
%patch 1
%patch 2
%patch 3
%patch 4
%patch 5
%patch 6
%patch 7
%patch 8
%patch 9
%patch 10
%patch 11
%patch 12
popd

%build
# Tell O3DE where to look for 3rd party packages
export LY_PACKAGE_SERVER_URLS="${LY_PACKAGE_SERVER_URLS};file://%{THIRD_PARTY_PATH}"

%cmake	-G "Ninja Multi-Config" \
	-DO3DE_INSTALL_ENGINE_NAME=o3de-sdk \
	-DLY_3RDPARTY_PATH=%{THIRD_PARTY_PATH} \
	-DCMAKE_INSTALL_PREFIX=%{INSTALL_PATH} \
%if %{SAVE_DISK_SPACE}
	-DLY_DISABLE_TEST_MODULES=ON \
	-DLY_STRIP_DEBUG_SYMBOLS=ON \
	-DLY_UNITY_BUILD=OFF
%endif

%cmake_build --config profile

%install
mkdir -p %{buildroot}%{_bindir}/

%cmake_install --config profile

pushd %{buildroot}%{INSTALL_PATH}/bin/Linux/profile/Default/
patchelf --set-rpath '$ORIGIN' libPhysX*.so*
%py3_shebang_fix pyside_tool.py shiboken_tool.py
popd

#Fix build-id conflicts
pushd %{buildroot}%{INSTALL_PATH}/bin/Linux/profile/Default/Builders/DirectXShaderCompiler
rm bin/dxc-3.7
rm lib/libdxcompiler.so.3.7
ln -s %{_bindir}/dxc-3.7 bin/dxc-3.7
ln -s %{_bindir}/libdxcompiler.so.3.7 lib/libdxcompiler.so.3.7
popd

pushd %{buildroot}%{_bindir}
echo 'pushd %{INSTALL_PATH};O3DE_ROOT_INSTALL=TRUE bin/Linux/profile/Default/o3de; popd' > o3de
popd

%files
%license NOTICES.txt LICENSE.txt
%doc README.md
%{INSTALL_PATH}
%{_bindir}/o3de

%post
pushd %{INSTALL_PATH}
python/get_python.sh
popd

#TODO: move this where it needs to go
pushd %{_bindir}
# Add o3de launcher to the PATH
chmod +x o3de
popd

pushd %{INSTALL_PATH}/bin/Linux/profile/Default/
# Fix file permissions
chmod -R u+rw,go+r .
chmod +x AssetBuilder AssetBundler AssetProcessor Builders/AZSLc/azslc Builders/DirectXShaderCompiler/bin/* \
	Builders/SPIRVCross/spirv-cross o3de 
popd

%postun
# Extra cleanup since the python files aren't recognized after being modified in the post install
rm -rf %{INSTALL_PATH}

%changelog
%autochangelog
