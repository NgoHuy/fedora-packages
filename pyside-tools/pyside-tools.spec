Name:           pyside-tools
Version:        0.2.14
Release:        4%{?dist}
Summary:        Development tools for PySide

Group:          Development/Tools
# LICENSE-uic file in the source tarball includes BSD and GPL license texts,
# but all the source files appear to have been re-licensed under GPLv2 by now.
License:        GPLv2
URL:            http://www.pyside.org
Source0:        http://www.pyside.org/files/pyside-tools-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-pyside-devel
BuildRequires:  qt4-devel
Requires:       python-pyside

%description
PySide provides Python bindings for the Qt cross-platform application
and UI framework.

This package ships the following accompanying tools:
 * pyside-rcc - PySide resource compiler
 * pyside-uic - Python User Interface Compiler for PySide
 * pyside-lupdate - update Qt Linguist translation files for PySide


%prep
%setup -q

# Remove bundled ElementTree library which is part of Python 2.5 and newer
rm -rf pysideuic/elementtree/


%build
cp pysideuic/port_v2/proxy_base.py pysideuic/port_v3/proxy_base.py
cp pysideuic/port_v3/load_plugin.py pysideuic/port_v2/load_plugin.py
cp pysideuic/port_v3/invoke.py pysideuic/port_v2/invoke.py
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DSHIBOKEN_PYTHON_SUFFIX=-python2.7 -DPYTHON_EXECUTABLE=/usr/bin/python2 -DPYTHON_INCLUDE_DIR=/usr/include/python2.7/ ..

mkdir -p python3
cd python3
%{cmake} -DSHIBOKEN_PYTHON_SUFFIX=.cpython-33m -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.3m/ ../.. 
popd

make -j1 %{?_smp_mflags} -C %{_target_platform}
make -j1 %{?_smp_mflags} -C %{_target_platform}/python3

%install
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}/python3

%files
%doc AUTHORS ChangeLog LICENSE*
%{_bindir}/pyside-rcc
%{_bindir}/pyside-uic
%{_bindir}/pyside-lupdate
%{_mandir}/man1/pyside-rcc.1*
%{_mandir}/man1/pyside-uic.1*
%{_mandir}/man1/pyside-lupdate.1*
%{python_sitearch}/pysideuic/
%{python3_sitearch}/pysideuic/

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Kalev Lember <kalevlember@gmail.com> - 0.2.13-1
- Update to 0.2.13

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 0.2.11-1
- Update to 0.2.11

* Thu Jun 23 2011 Kalev Lember <kalev@smartlink.ee> - 0.2.10-1
- Update to 0.2.10
- Cleaned up the spec file for modern rpmbuild

* Fri May 27 2011 Kalev Lember <kalev@smartlink.ee> - 0.2.9-1
- Update to 0.2.9

* Sun Apr 03 2011 Kalev Lember <kalev@smartlink.ee> - 0.2.8-1
- Update to 0.2.8

* Thu Mar 03 2011 Kalev Lember <kalev@smartlink.ee> - 0.2.7-1
- Update to 0.2.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Kalev Lember <kalev@smartlink.ee> - 0.2.6-1
- Update to 0.2.6
- Added man pages

* Wed Dec 01 2010 Kalev Lember <kalev@smartlink.ee> - 0.2.3-1
- Update to 0.2.3

* Tue Nov 23 2010 Kalev Lember <kalev@smartlink.ee> - 0.2.2-2
- Remove bundled ElementTree library in prep (#655527)
- Updated License tag to reflect bundled ElementTree removal

* Sat Nov 20 2010 Kalev Lember <kalev@smartlink.ee> - 0.2.2-1
- Initial RPM release
