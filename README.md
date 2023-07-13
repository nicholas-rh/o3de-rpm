O3DE RPM
-
This is a (work-in-progress) project with the aim of working towards an O3DE RPM package which is able to be included in the official Fedora/RHEL/etc. repositories. It targets the O3DE 23.05 release.

Builds are currently hosted at https://copr.fedorainfracloud.org/coprs/nfrizzel/o3de/

Based off of the work of https://github.com/spotrh/o3de-fedora

Spec files, patches, and other packaging related files are licensed under the MIT license, tarballs are licensed under their respective project license(s).

Build Instructions (Local)
-
1. Install the required build dependencies and build scripts/tools:
```
$ dnf install openssl cmake clang ninja-build git git-lfs openssl-devel libunwind-devel \
  libzstd-devel zlib-devel libxkbcommon-x11-devel libcurl-devel fontconfig-devel libxcb-devel \
  mesa-libGLU-devel qt5-qtbase-devel rpmdevtools rpmspectool rpmlint
```
2. Clone the git repository
```
$ git clone https://github.com/nicholas-rh/o3de-rpm; cd o3de-rpm/copr/o3de
```
3. Setup the build tree
```
$ rpmdev-setuptree
```
4. Acquire the source files using spectool, copy patches into the build tree
```
$ spectool -g o3de.spec --directory ~/rpmbuild/SOURCE; cp *.patch ~/rpmbuild/SOURCE
```
5. Run the build. If successful, the binary RPM will be located in ~/rpmbuild/RPMS. Expect the build to take a while, especially on less-powerful hardware, including the post-build stages such as checking for unpackaged files.
```
$ rpmbuild -bb o3de.spec
```
If you run into any problems during a build following these instructions, please file an issue and I'll look to address it.

Commentary
-
**Q.) What is the status of this project?**

A.) An RPM package can be generated either locally using rpmbuild, mock, etc. or through a build using the copr build system infrastructure. This package can be installed and run normally on a Fedora 38 installation.

**Q.) What remaining obstacles are there to producing a Fedora-worthy package?**

A.) Most of the remaining issues with regards to submitting the package for review are related to the various dependencies O3DE pulls in. There are a large number of bundled dependencies that O3DE manages through its own package management system separate from that of the OS or other traditional package management tools (see details on the O3DE packaging system below). 

Many of these dependencies are O3DE-specific forks of their upstream software, do not match the major number version present in the Fedora official repos (and so probably have ABI-breaking changes), or are otherwise unpackaged for Fedora. To further complicate things, the third-party dependencies which include binaries are built on Ubuntu, and are licensed under different licenses than that of the main O3DE repository. 

At least one of these licenses is not approved for Fedora (NvCloth with the Nvidia 1-Way Commercial License, which is not in the license approved/rejected list but seems similar to the Amazon Source License, which is not allowed). Then, each third-party dependency also may include it's own bundled dependencies, which need to be handled as well.

**Q.) With these dependency problems, why a traditional package rather than a Flatpak/Snap/etc.?**

A.) Snap and Flatpak are good candidates for formats to distribute O3DE builds, and this is an opinion shared by the upstream developers. 

There is a snap package produced by the upstream O3DE build system using CPack, which is a tool that generates installation packages from CMake files: https://docs.o3de.org/docs/welcome-guide/setup/installing-linux/. Currently this is considered "experimental". There is no equivalent support for Flatpak using CPack. I've considered manually putting together one as a test, but haven't yet due to time constraints.
