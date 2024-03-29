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
BuildRequires:	libcurl-devel
BuildRequires:	libssh-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel

%description
The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface for Amazon Web Services (AWS). It is meant to be performant and fully functioning with low- and high-level SDKs, while minimizing dependencies and providing platform portability (Windows, OSX, Linux, and mobile).

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
%cmake -DCMAKE_BUILD_TYPE=Debug -DBUILD_ONLY="access-management;cognito-identity;cognito-idp;core;devicefarm;dynamodb;gamelift;identity-management;kinesis;lambda;mobileanalytics;queues;s3;sns;sqs;sts;transfer" -DBUILD_SHARED_LIBS=ON -DENABLE_TESTING=OFF
%cmake_build

%install
%cmake_install
pushd %{buildroot}%{_libdir}
rm -rf *.a
popd

%files
%doc README.md
%license LICENSE.txt NOTICE.txt
# What is this? Can we exclude it?
%{_bindir}/sha256_profile
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
%autochangelog
