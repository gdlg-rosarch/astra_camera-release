Name:           ros-kinetic-astra-camera
Version:        0.2.2
Release:        1%{?dist}
Summary:        ROS astra_camera package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-camera-info-manager
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  git
BuildRequires:  libudev-devel
BuildRequires:  libusbx-devel
BuildRequires:  ros-kinetic-camera-info-manager
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs

%description
Drivers for Orbbec Astra Devices.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 23 2018 Tim Liu <liuhua@orbbec.com> - 0.2.2-1
- Autogenerated by Bloom

* Fri Mar 23 2018 Tim Liu <liuhua@orbbec.com> - 0.2.2-0
- Autogenerated by Bloom

* Mon Feb 12 2018 Tim Liu <liuhua@orbbec.com> - 0.2.1-0
- Autogenerated by Bloom

* Thu Feb 08 2018 Tim Liu <liuhua@orbbec.com> - 0.2.0-0
- Autogenerated by Bloom

* Fri May 27 2016 Tim Liu <liuhua@orbbec.com> - 0.1.5-0
- Autogenerated by Bloom

* Fri May 27 2016 Tim Liu <liuhua@orbbec.com> - 0.1.4-0
- Autogenerated by Bloom

* Thu May 26 2016 Tim Liu <liuhua@orbbec.com> - 0.1.3-0
- Autogenerated by Bloom

* Thu May 26 2016 Tim Liu <liuhua@orbbec.com> - 0.1.2-0
- Autogenerated by Bloom

* Thu May 26 2016 Tim Liu <liuhua@orbbec.com> - 0.1.1-0
- Autogenerated by Bloom

