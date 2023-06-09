%global	commit	1cb38f46977cf3736a3fb1db8191cf4a18c3577b

Name:		mikktspace
Version:	0
Release:	%autorelease
Summary:	A common standard for tangent space used in baking tools to produce normal maps.
License:	Zlib
URL:		http://www.mikktspace.com/

Source:		https://github.com/mmikk/MikkTSpace/archive/%{commit}.tar.gz

BuildRequires:	gcc

%description
A common standard for tangent space used in baking tools to produce normal maps.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for mikktspace

%description devel
Development files for mikktspace

%prep
%autosetup -n MikkTSpace-%{commit}

%build
gcc %{optflags} mikktspace.c -shared -o lib%{name}.so.%{version}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}/

install -m0755 mikktspace.h %{buildroot}%{_includedir}/%{name}/
install -m0755 lib%{name}.so.%{version} %{buildroot}%{_libdir}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so

%files
%doc README.md
%{_libdir}/libmikktspace.so.*

%files devel
%{_includedir}/mikktspace
%{_libdir}/libmikktspace.so

%changelog
%autochangelog
