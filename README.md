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

**Q.) How does the O3DE build system function?**

A.) O3DE is a primarily-C++ project with build scripts written in CMake. It is composed of "Gems" which are modules that include code, assets, etc. There are a number of core gems (required for the engine to function) as well as many optional gems. Users can also specify their own gems, and there are a set of official, extra gems in the o3de-extra repository which can be included https://github.com/o3de/o3de-extras/tree/development

The core engine code as well as each gem has certain dependencies which are satisfied either by bundling & building the source code into the engine/gem itself (e.g. ImGui), pulling the source code using CMake plumbing (RecastNavigation), using system libraries (libunwind, openssl, etc.) or finally by using the O3DE-specific package manager, which pulls prebuilt binaries or other dependencies from an O3DE-hosted server.

CMake targets are speified which correspond to each third-party dependency. These dependencies are resolved differently depending on the type. The first three categories of dependencies mentioned are included through the usual CMake means. O3DE package manager packages, however, are associated with a certain package name and version which the O3DE build system will use to download them at build time as needed (they are cached afterwards).

**Q.) How does the O3DE package manager function?**

A.) Packages are built separately, typically on a build server, and then uploaded to the hardcoded package distribution server. The O3DE package generation scripts are located at https://github.com/o3de/3p-package-source and https://github.com/o3de/3p-package-scripts. The documentation for these tools is fairly good, but as a quick summary each package has its own custom build script that is run which generates a distributable package in the format O3DE expects. These scripts are different for each platform, and some are more complex than others, for example some require a Docker image to be built while others are simple shell scripts.

**Q.) Why can't we just rebuild the O3DE dependencies using their tooling for Fedora?**

A.) I investigated doing this but I don't think it is the right way forward unless the upstream developers are also interested in getting involved. The reason why is because certain packages which use Docker build setups use an Ubuntu-based Docker image which doesn't get us anywhere, and those that don't still use Ubuntu tools like the apt package manager. It would probably be more effort to rewrite these than to just properly package the dependencies, and when packaging them properly others can make use of them for non-O3DE software as well.

**Q.) What strategy was used for packaging dependencies?**
Tom Callaway did a lot of great work on providing a base of work to go off of for packaging the O3DE dependencies. I decided that it would be more useful to take his work and see what could be done to get it reviewed for inclusion into Fedora where it can be maintained rather than attempt to update and move each dependency into copr. My rationale for this is that it would be better to focus on a few packages and submit them for Fedora where others can benefit from and help to maintain them instead of making superficial changes to his work that will quickly become outdated, since both O3DE and Fedora are fast-moving projects. So, there are still a number of dependencies which use the upstream-built packages rather than distro packages.
