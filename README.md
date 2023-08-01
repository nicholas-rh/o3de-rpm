O3DE RPM
-
This is a (work-in-progress) project developed as part of my internship with the aim of working towards an O3DE RPM package which is able to be included in the official Fedora/RHEL/etc. repositories. It targets the O3DE 23.05 release.

Builds are currently hosted at https://copr.fedorainfracloud.org/coprs/nfrizzel/o3de/

Based off of the work of https://github.com/spotrh/o3de-fedora

Spec files, patches, and other packaging related files are licensed under the MIT license, tarballs are licensed under their respective project license(s).

Screenshots
-
<p align="center">
    <image src=https://github.com/nicholas-rh/o3de-rpm/assets/133678776/5fd8ebe7-72ba-465c-9898-cef16f5ad84f>
    Multiplayer sample project https://github.com/o3de/o3de-multiplayersample
</p>

<p align="center">
    <image src=https://github.com/nicholas-rh/o3de-rpm/assets/133678776/93e9cc3a-1c32-46ab-a8d1-714107ec4cc3>
    Multiplayer game
</p>

<p align="center">
    <image src=https://github.com/nicholas-rh/o3de-rpm/assets/133678776/e41a5e8b-64d4-4806-8a50-de0873ae0c2d>
    ArchVis Loft sample https://github.com/o3de/loft-arch-vis-sample
</p>

<p align="center">
    <image src=https://github.com/nicholas-rh/o3de-rpm/assets/133678776/c2c2435b-52fe-4b59-a020-cce80de7b17a>
    Game jam project by Loherangrin https://github.com/loherangrin/games.o3de.o3de-jam-2305
</p>

Build from Source
-
There are a number of O3DE tasks which require a source engine build as opposed to the engine SDK/installer build that this package provides. The forked source tree with distro-specific patches preapplied can be found at https://github.com/nicholas-rh/o3de/tree/rpm

Third-Party Dependency Tracker
-
[A spreadsheet with a list of each O3DE third-party package dependency and information about it that is relevant for packagers can be found here](https://docs.google.com/spreadsheets/d/12raQfOtQBYHzXoYKdYUy6ZCOCCsmuhHCbc-730HVKJ8/edit?usp=sharing)

RPM Build Instructions (Local)
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

A.) An RPM package can be generated either locally using rpmbuild, mock, etc. or through a build using the copr build system infrastructure. This package can be installed and run normally on a Fedora 37, 38, or Rawhide installation (as of the date of writing).

**Q.) What remaining obstacles are there to producing a Fedora-worthy package?**

A.) Most of the remaining issues with regards to submitting the package for review are related to the various dependencies O3DE pulls in. There are a large number of bundled dependencies that O3DE manages through its own package management system separate from that of the OS or other traditional package management tools (see details on the O3DE packaging system below). Applications with bundled dependencies are tricky to handle using traditional packaging managers, and usually require manual patching of build scripts.

Many of these dependencies are O3DE-specific forks of their upstream software, do not match the major number version present in the Fedora official repos (and so probably have ABI-breaking changes), or are otherwise unpackaged for Fedora.

The biggest obstacle is that the prebuilt dependencies which are provided through the custom O3DE package manager are built in an Ubuntu environment. Anyone familiar with application development on Linux will recognize the various pitfalls associated with attempting to port binaries between different distros, such as missing shared libraries, ABI incompatability, etc. These problems seem to be partially mitigated by the fact that O3DE largely provides a ground-up set of bundled dependencies in binary form. This means that many of the dependencies are "self-contained", even including the usual core system libraries such as openssl, zlib, etc.

At least one of these licenses is not approved for Fedora and by extension Copr (NvCloth with the Nvidia 1-Way Commercial License, which is not in the license approved/rejected list but seems similar to the Amazon Source License, which is not allowed). Then, each third-party dependency also may include it's own bundled dependencies, which need to be handled as well.

**Q.) What strategy would you recommend for handling these dependency problems?**

A.) Unfortunately there is no one "silver bullet" solution to this. If the goal is to maintain the software as part of Fedora, then every dependency needs to be built from source, and bundled binaries are very much a no-go. Where possible, these dependencies would ideally be replaced by the Fedora system packages. The O3DE build scripts need to be modified to support this, however. I've done this for a number of packages where possible, and am working on merging these changes into the upstream repo.

Packages which are forks, old versions, or otherwise not present in the official Fedora repos will need to be packaged manually. There are two approaches to this I see. The first which should be preferred is to package the dependencies in the traditional use-case agnostic way, so that the wider Fedora community can use them for unrelated software. Tom Callaway did a great job working on this here https://github.com/spotrh/o3de-fedora and I highly recommend using his work as a reference.

For dependencies which have O3DE-specific patches, or for which it is otherwise not practical to do the above, I recommend making use of the O3DE build scripts https://github.com/o3de/3p-package-source and https://github.com/o3de/3p-package-scripts. These scripts are written with the assumption that they will be ran on Ubuntu, so modifications will need to be made to several in order to use them for building on Fedora. Several also use Ubuntu docker build images, which would need to be changed to the Fedora equivalent.

**Q.) With these dependency problems, why a traditional package rather than a Flatpak/Snap/AppImage/etc.?**

A.) Snap and Flatpak are good candidates for formats to distribute O3DE builds, and this is an opinion shared by the upstream developers. 

There is a snap package produced by the upstream O3DE build system using CPack, which is a tool that generates installation packages from CMake files: https://docs.o3de.org/docs/welcome-guide/setup/installing-linux/ There is no equivalent support for Flatpak using CPack.

**Q.) Why not try to target a stripped-down version of O3DE?**

A.) O3DE is fairly modular, but even when building a minimal version of the engine there is still a fairly significant number of dependencies which need to be included. The smallest useful target which can be distributed is the Editor, which requires all of the core engine components as well as a few extra gems. Targeting the SDK engine/install target for packaging means users don't have to do any building of core components and gems, which is a better user experience.

**Q.) How does the O3DE build system function?**

A.) O3DE is a primarily-C++ project with build scripts written in CMake. It is composed of "Gems" which are modules that include code, assets, etc. There are a number of core gems (required for the engine to function) as well as many optional gems. Users can also specify their own gems, and there are a set of official, extra gems in the o3de-extra repository which can be included https://github.com/o3de/o3de-extras/tree/development

The core engine code as well as each gem has certain dependencies which are satisfied either by bundling & building the source code into the engine/gem itself (e.g. ImGui), pulling the source code using CMake plumbing (RecastNavigation), using system libraries (libunwind, openssl, etc.) or finally by using the O3DE-specific package manager, which pulls prebuilt binaries or other dependencies from an O3DE-hosted server.

CMake targets are speified which correspond to each third-party dependency. These dependencies are resolved differently depending on the type. The first three categories of dependencies mentioned are included through the usual CMake means. O3DE package manager packages, however, are associated with a certain package name and version which the O3DE build system will use to download them at build time as needed (they are cached afterwards).

**Q.) How does the O3DE package manager function?**

A.) Packages are built separately, typically on a build server, and then uploaded to the hardcoded package distribution server. The O3DE package generation scripts are located at https://github.com/o3de/3p-package-source and https://github.com/o3de/3p-package-scripts. The documentation for these tools is fairly good, but as a quick summary each package has its own custom build script that is run which generates a distributable package in the format O3DE expects. These scripts are different for each platform, and some are more complex than others, for example some require a Docker image to be built while others are simple shell scripts.

Resources
-
https://docs.o3de.org/docs/welcome-guide/setup/setup-from-github/

https://rpm.org/documentation.html

https://docs.fedoraproject.org/en-US/packaging-guidelines/

https://docs.fedoraproject.org/en-US/legal/allowed-licenses/
