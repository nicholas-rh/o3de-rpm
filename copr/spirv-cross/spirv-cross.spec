%global commit 72a2ec4c1b56ce233e0da97a36f87af98927256c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		spirv-cross
Version:	20210429
Release:	%{autorelease}
URL:		https://github.com/KhronosGroup/SPIRV-Cross/
License:	ASL 2.0
Summary:	Library and tool for working with SPIR-V

BuildRequires:	cmake
BuildRequires:	gcc-c++

Source0:	https://github.com/KhronosGroup/SPIRV-Cross/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

%description
SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V and disassembling SPIR-V back to high level languages. 

%package devel
Summary:	Development files for spirv-cross
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for spirv-cross.

%prep
%autosetup -n SPIRV-Cross-%{commit}

%build
# The CLI requires the static libs be built
%cmake -DSPIRV_CROSS_SHARED=ON -DSPIRV_CROSS_CLI=ON -DSPIRV_CROSS_STATIC=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/spirv-cross
%{_libdir}/libspirv-cross-c-shared.so.*

%files devel
%{_includedir}/spirv_cross/
%{_libdir}/libspirv-cross-c-shared.so
%{_libdir}/libspirv-cross*.a
%{_libdir}/pkgconfig/spirv-cross-c-shared.pc
%{_datadir}/spirv_cross_*/cmake/

%changelog
* Fri Jun 23 2023 Nicholas Frizzell <nfrizzel@redhat.com> - 1.1.5
- Update version, other changes

* Tue Jul 13 2021 Tom Callaway <spot@fedoraproject.org> - 20210713-1.gitbe3988b
- initial package
