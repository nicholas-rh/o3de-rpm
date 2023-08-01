%global	commit	b7c38164239285ed53cd762650da3b7cc36827d4

Name:		ispc-texture-compressor
Version:	0
Release:	%autorelease
Summary:	A common standard for tangent space used in baking tools to produce normal maps.
License:	MIT
URL:		ispc-texture-compressor

Source:		https://github.com/GameTechDev/ISPCTextureCompressor/archive/%{commit}.tar.gz

Patch:		Makefile.patch

BuildRequires:	gcc-g++
BuildRequires:	ispc-devel

%description
A common standard for tangent space used in baking tools to produce normal maps.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for ispc-texture-compressor

%description devel
Development files for ispc-texture-compressor

%prep
%autosetup -n ISPCTextureCompressor-%{commit}

%build
%make_build -f Makefile.linux

%install
%make_install

%files
%doc readme.md
%license license.txt
%{_libdir}/libmikktspace.so.*

%files devel
%{_includedir}/mikktspace
%{_libdir}/libmikktspace.so

%changelog
* Tue Aug 1 2023 Nicholas Frizzell <nfrizzel@redhat.com> - 0.0.0
- ISPCTextureCompressor init
