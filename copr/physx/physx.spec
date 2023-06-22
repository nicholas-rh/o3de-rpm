%global         toolchain clang

Name:		physx
Version:	5
Release:	%autorelease
Summary:	NVIDIA PhysX
License:	BSD-3-Clause and MIT
URL:		https://o3de.org
BuildArch:	x86_64

Source:		https://github.com/NVIDIA-Omniverse/PhysX

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	python3

Patch0:		fix_compile_error.patch

%description
The NVIDIA PhysX SDK is a scalable multi-platform physics solution supporting a wide range of devices, from smartphones to high-end multicore CPUs and GPUs.

%package devel
Requires:	glew-devel

%description devel
Development files for PhysX.

%prep
%autosetup

# We aren't interested in these for now
rm -rf blast
rm -rf flow
# Use system glew package
rm ./snippets/graphics/include/GL/wglew.h

%build
pushd physx
./generate_projects.sh linux
popd

pushd physx/compiler/linux-release/
make VERBOSE=1
popd

%install
mkdir -p %{buildroot}%{_libdir}

%files

%files devel

%changelog
%autochangelog
