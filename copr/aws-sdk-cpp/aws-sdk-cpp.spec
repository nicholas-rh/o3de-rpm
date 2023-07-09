%global		toolchain clang

Name:		aws-sdk-cpp
Version:	1.9.50
Release:	1%{?dist}
Summary:	AWS SDK for C++ 
License:	Apache-2.0
URL:		https://github.com/aws/aws-sdk-cpp

# Generated using generate_tarball.sh
Source0:	https://github.com/nicholas-rh/o3de-rpm/releases/download/large_files/aws-sdk-cpp.tar.gz

# Remove -Werror
Patch0: compiler_settings.patch

BuildRequires:	clang
BuildRequires:	cmake

%description
The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface for Amazon Web Services (AWS). It is meant to be performant and fully functioning with low- and high-level SDKs, while minimizing dependencies and providing platform portability (Windows, OSX, Linux, and mobile).

%package core
Summary: AWS C++ SDK core

%description core
AWS SDK C++ core

%package devel
Summary: Development files for AWS C++ SDK

%description devel
Development files for AWS C++ SDK

%prep
%setup -n aws-sdk-cpp

pushd %{_builddir}/aws-sdk-cpp
%patch 0 
popd

%build
# Change this when more components are needed
%cmake -DCMAKE_BUILD_TYPE=Debug -DBUILD_ONLY=core
%cmake_build

%install
%cmake_install
pushd %{buildroot}%{_libdir}
rm -rf *.a
popd

%files
%doc README.md
%license LICENSE.txt NOTICE.txt

%files core
# What is this? Can we exclude it?
%{_bindir}/sha256_profile
# There are some random cmake files in here, I'm not sure what their purpose is
# Also "libtesting-resources.so"
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
%autochangelog
