Name:		spirv-cross
Version:	1.1.5
Release:	%{autorelease}
URL:		https://github.com/KhronosGroup/SPIRV-Cross/
License:	ASL 2.0
Summary:	Library and tool for working with SPIR-V

BuildRequires:	cmake
BuildRequires:	gcc-c++

Source0:	https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/MoltenVK-%{version}.tar.gz

%description
SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V and disassembling SPIR-V back to high level languages. 

%package devel
Summary:	Development files for SPIRV-Cross
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for SPIRV-Cross.

%prep
%autosetup -n SPIRV-Cross-MoltenVK-%{version}

%build
# The CLI requires the static libs be built
%cmake -DSPIRV_CROSS_SHARED=ON -DSPIRV_CROSS_CLI=ON -DSPIRV_CROSS_STATIC=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSES/*
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
