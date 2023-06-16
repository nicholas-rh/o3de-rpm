%global		BUNDLED_PACKAGE_URL https://d3t6xeg4fgfoum.cloudfront.net
%global		BUNDLED_PACKAGE_DIR o3de-packages

%global		toolchain clang

Name:		o3de
Version:	2305.0
Release:	1%{?dist}
Summary:	Open 3D Engine
License:	ASL 2.0 or MIT
URL:		https://o3de.org
BuildArch:	x86_64

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
Source9:	%{BUNDLED_PACKAGE_URL}/DirectXShaderCompilerDxc-1.6.2112-o3de-rev1-linux.tar.xz
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
Source20:	%{BUNDLED_PACKAGE_URL}/NvCloth-v1.1.6-4-gd243404-pr58-rev1-linux.tar.xz
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

# Remove -Werror to prevent extraneous compile errors
Patch0:		Configurations_clang.patch 
Patch1:		RenderPass.patch 
Patch2:		RecastNavigationCMakeLists.patch
Patch3:		Configurations_linux.patch

BuildRequires:	clang
BuildRequires:	cmake
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
BuildRequires:	patchelf
BuildRequires:	qt5-qtbase-devel
BuildRequires:	zlib
BuildRequires:	zlib-devel

%description
Open 3D Engine (O3DE) is an Apache 2.0-licensed multi-platform 3D engine that enables developers and content creators to build AAA games, cinema-quality 3D worlds, and high-fidelity simulations without any fees or commercial obligations. 

%prep
%setup -c -n %{name}
mkdir 3rdParty
%setup -T -D -n %{name}/3rdParty -a 1
%setup -T -D -n %{name}/3rdParty -a 2
%setup -T -D -n %{name}/3rdParty -a 3
%setup -T -D -n %{name}/3rdParty -a 4
%setup -T -D -n %{name}/3rdParty -a 5
%setup -T -D -n %{name}/3rdParty -a 6
%setup -T -D -n %{name}/3rdParty -a 7
%setup -T -D -n %{name}/3rdParty -a 8
%setup -T -D -n %{name}/3rdParty -a 9
%setup -T -D -n %{name}/3rdParty -a 10
%setup -T -D -n %{name}/3rdParty -a 11
%setup -T -D -n %{name}/3rdParty -a 12
%setup -T -D -n %{name}/3rdParty -a 13
%setup -T -D -n %{name}/3rdParty -a 14
%setup -T -D -n %{name}/3rdParty -a 15
%setup -T -D -n %{name}/3rdParty -a 16
%setup -T -D -n %{name}/3rdParty -a 17
%setup -T -D -n %{name}/3rdParty -a 18
%setup -T -D -n %{name}/3rdParty -a 19
%setup -T -D -n %{name}/3rdParty -a 20
%setup -T -D -n %{name}/3rdParty -a 21
%setup -T -D -n %{name}/3rdParty -a 22
%setup -T -D -n %{name}/3rdParty -a 23
%setup -T -D -n %{name}/3rdParty -a 24
%setup -T -D -n %{name}/3rdParty -a 25
%setup -T -D -n %{name}/3rdParty -a 26
%setup -T -D -n %{name}/3rdParty -a 27
%setup -T -D -n %{name}/3rdParty -a 28
%setup -T -D -n %{name}/3rdParty -a 29
%setup -T -D -n %{name}/3rdParty -a 30
%setup -T -D -n %{name}/3rdParty -a 31
%setup -T -D -n %{name}/3rdParty -a 32
%setup -T -D -n %{name}/3rdParty -a 33
%setup -T -D -n %{name}/3rdParty -a 34
%setup -T -D -n %{name}/3rdParty -a 35
%setup -T -D -n %{name}/3rdParty -a 36
%setup -T -D -n %{name}/3rdParty -a 37
%setup -T -D -n %{name}/3rdParty -a 38
%setup -T -D -n %{name}/3rdParty -a 39
%setup -T -D -n %{name}/3rdParty -a 40
%setup -T -D -n %{name}/3rdParty -a 41

cd %{_builddir}/%{name}
%patch 0
%patch 1
%patch 2
python/get_python.sh

%build
cd %{_builddir}/o3de
export LY_PACKAGE_SERVER_URLS="${LY_PACKAGE_SERVER_URLS};file://%{_builddir}/%{name}/3rdParty"
%cmake	-G "Ninja Multi-Config" \
	-DCMAKE_INSTALL_PREFIX=/opt/o3de \
	-DLY_3RDPARTY_PATH=%{_builddir}/%{name}/3rdParty \
	-DLY_DISABLE_TEST_MODULES=ON \
	-DO3DE_INSTALL_ENGINE_NAME=o3de-redist

%cmake_build --config profile

%install
%global debug_package %{nil}
# Fix rpath for PhysX binaries
patchelf --set-rpath '$ORIGIN' %{_builddir}/o3de/3rdParty/PhysX/shared/bin/*
patchelf --set-rpath '$ORIGIN' %{_builddir}/o3de/redhat-linux-build/bin/profile/libPhysXCooking_64.so
patchelf --set-rpath '$ORIGIN' %{_builddir}/o3de/redhat-linux-build/bin/profile/libPhysXCommon_64.so
patchelf --set-rpath '$ORIGIN' %{_builddir}/o3de/redhat-linux-build/bin/profile/libPhysX_64.so
mkdir -p %{buildroot}/opt/o3de
cp -r %{_builddir}/o3de/redhat-linux-build/* %{buildroot}/opt/o3de
%py3_shebang_fix %{buildroot}/opt/o3de/*

%files
/opt/o3de/

%changelog
%autochangelog
