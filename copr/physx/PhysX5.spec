%define		debug_package %{nil}

%global		toolchain clang

%global		commit 93b6c250e2141f8e87543bc8bb763046f26ffbc5
%global		shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		PhysX5
Version:	5.1.3
Release:	%autorelease
Summary:	NVIDIA PhysX5
License:	BSD-3-Clause and MIT
URL:		https://github.com/NVIDIA-Omniverse/PhysX
ExclusiveArch:	x86_64

Source:		https://github.com/NVIDIA-Omniverse/PhysX/archive/%{commit}/PhysX-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	glew-devel
BuildRequires:	make
BuildRequires:	python3
BuildRequires:	patchelf

Patch0:		fix_compile_error.patch

%description
The NVIDIA PhysX SDK is a scalable multi-platform physics solution supporting a wide range of devices, from smartphones to high-end multicore CPUs and GPUs.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for PhysX

%description devel
Development files for PhysX.

%package samples
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Samples and snippets from PhysX

%description samples
The samples and snippet binaries from PhysX.

%prep
%autosetup -n PhysX-%{commit} -p0
# We aren't interested in these for now
rm -rf blast
rm -rf flow
# Use system glew package
rm physx/snippets/graphics/include/GL/wglew.h

%build
pushd physx
./generate_projects.sh linux
popd

pushd physx/compiler/linux-profile/
%make_build VERBOSE=1
popd

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/PhysX

pushd physx/bin/linux.clang/profile
install -m0755 lib*.so %{buildroot}%{_libdir}
install -m0644 lib*.a %{buildroot}%{_libdir}
for i in Snippet*; do
	install -m0755 $i %{buildroot}%{_bindir}/PhysX-$i
done
popd

cp -a physx/include/* %{buildroot}%{_includedir}/PhysX/

patchelf --remove-rpath %{buildroot}%{_bindir}/PhysX-* 
patchelf --remove-rpath %{buildroot}%{_libdir}/*.so

%files
%doc README.md
%{_libdir}/*.so

%files devel
%{_libdir}/*.a
%{_includedir}/PhysX/

%files samples
%{_bindir}/PhysX-*

%changelog
* Thu Jun 22 2023 Nicholas Frizzell <nfrizzel@redhat.com> - 5.1.3
- Initial package

