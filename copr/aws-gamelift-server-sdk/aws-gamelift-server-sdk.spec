%global		toolchain clang

Name:		amazon-gamelift-server-sdk
Version:	5.0.0
Release:	1%{?dist}
Summary:	Server SDK for Amazon GameLift
License:	ASL 2.0
URL:		https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-supported.html

Source0: 	https://gamelift-release.s3-us-west-2.amazonaws.com/GameLift-SDK-Release-5.0.0.zip

BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	protobuf-devel 
BuildRequires:	protobuf-lite-devel

# These are all header-only libraries, see the license file for more info
Provides:	bundled(asio)
Provides:	bundled(base64-devel)
Provides:	bundled(md5-devel)
Provides:	bundled(msinttypes)
# Can probably use the system library
Provides:	bundled(rapidjson)
Provides:	bundled(sha1-devel)

%description
The Amazon GameLift Server SDK Version 4.0.2 supports Unity 2020, Unreal 4.25,
and custom C++ and C# engines. It contains components that integrate with your
Windows or Linux game server, including C++ and C# versions of the Amazon
GameLift Server SDK, Amazon GameLift Local, and an Unreal Engine plugin.

%prep
%autosetup -c

%build
pushd %{_builddir}/amazon-gamelift-server-sdk-5.0.0/GameLift-SDK-Release-5.0.0/GameLift-Cpp-ServerSDK-5.0.0/
%cmake .
%cmake_build
popd

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/licenses/amazon-gamelift-server-sdk
mkdir -p %{buildroot}%{_datadir}/doc/amazon-gamelift-server-sdk

pushd %{_builddir}/amazon-gamelift-server-sdk-5.0.0/GameLift-SDK-Release-5.0.0/GameLift-Cpp-ServerSDK-5.0.0/
cp -a NOTICE_C++_AMAZON_GAMELIFT_SDK.TXT %{buildroot}%{_datadir}/licenses/amazon-gamelift-server-sdk/
cp -a LICENSE_AMAZON_GAMELIFT_SDK.TXT %{buildroot}%{_datadir}/licenses/amazon-gamelift-server-sdk/
cp -a README.md %{buildroot}%{_datadir}/doc/amazon-gamelift-server-sdk/
pushd %{_vpath_builddir}/prefix
cp -ra include/aws %{buildroot}%{_includedir}/
cp -ra lib/libaws-cpp-sdk-gamelift-server.so %{buildroot}%{_libdir}/
popd
popd

%files
%{_includedir}
%{_libdir}
%license NOTICE_C++_AMAZON_GAMELIFT_SDK.TXT LICENSE_AMAZON_GAMELIFT_SDK.TXT
%doc README.md

%changelog
* Fri Jul  7 2023 Nicholas Frizzell <nfrizzel@redhat.com> - 5.0.0-1
- Update version

* Tue May  4 2021 Tom Callaway <spot@fedoraproject.org> - 4.0.2-2
- fix missing <thread>

* Thu Mar 25 2021 Tom Callaway <spot@fedoraproject.org> - 4.0.2-1
- initial package
