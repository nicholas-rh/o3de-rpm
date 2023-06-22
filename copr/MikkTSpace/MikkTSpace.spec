%global	commit 	1cb38f46977cf3736a3fb1db8191cf4a18c3577b

Name:		MikkTSpace
Version:	0
Release:	%autorelease
Summary:	A common standard for tangent space used in baking tools to produce normal maps.
License:	Zlib
URL:		http://www.mikktspace.com/
ExclusiveArch:	x86_64

Source:		https://github.com/mmikk/MikkTSpace/archive/%{commit}.tar.gz

BuildRequires:	gcc

%description
A common standard for tangent space used in baking tools to produce normal maps.

%package devel
Summary:	Development files for PhysX

%description devel
Development files for PhysX

%prep
%autosetup -n %{name}-%{commit}

%build
gcc %{optflags} mikktspace.c -shared -o %{name}.so.%{version}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/MikkTSpace

install -m0755 %{name}.so.%{version} %{buildroot}%{_libdir}
cp -a mikktspace.h %{buildroot}%{_includedir}/%{name}

%files
%doc README.md
%{_libdir}/*.so.%{version}

%files devel
%{_includedir}/MikkTSpace/*

%changelog
%autochangelog
