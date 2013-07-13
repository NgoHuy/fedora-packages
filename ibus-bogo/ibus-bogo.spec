Name:		ibus-bogo

%global commit 7aeb7bdb0a42d5babc034509e07fce177b4ae5ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version:	0.3
Release:	5%{?dist}
Summary:	Vietnamese engine for IBus input platform

Group:		User Interface/X
License:	GPLv3
URL:		http://github.com/BoGoEngine/ibus-bogo-python

Source0:	http://github.com/BoGoEngine/ibus-bogo-python/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# fix the run scripts folder to /usr/libexec since upstream developers put it in /usr/lib
Patch0:		ibus-bogo-fix-libexec-folder-name.patch

BuildRequires:	desktop-file-utils
BuildRequires:	ibus-devel
BuildRequires:	python3-devel
BuildRequires:	python3-gobject
BuildRequires:	python-pyside-devel
BuildRequires:	qt4-devel
BuildRequires:	pyside-tools
BuildArch:	noarch

Requires:	ibus
Requires:	python3
Requires:	python-pyside
Requires:	qt4
Requires:	python3-gobject
Requires:	libwnck3	


%description
A Vietnamese engine for IBus input platform that uses BoGoEngine.


%prep
%setup -qn %{name}-python-%{version}
%patch0 -p1 -b .ibus-bogo-origin0

%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
desktop-file-install \
--add-category="Settings" \
--delete-original \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}-settings.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc README.md AUTHORS COPYING
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/ibus/component/bogo.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_libexecdir}/%{name}/
%exclude %{_datadir}/%{name}/bogo/*.pyc
%exclude %{_datadir}/%{name}/bogo/*.pyo
%exclude %{_datadir}/%{name}/config-gui/*.pyc
%exclude %{_datadir}/%{name}/config-gui/*.pyo
%exclude %{_datadir}/%{name}/ibus_engine/*.pyc
%exclude %{_datadir}/%{name}/ibus_engine/*.pyo
%exclude %{_datadir}/%{name}/vncharsets/*.pyc
%exclude %{_datadir}/%{name}/vncharsets/*.pyo


%changelog
* Mon May 6 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-5
- Add python3-gobject, libwnck3 as Requires.

* Wed Apr 29 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-4
- Add pyside-tools as a BuildRequires (missing).

* Wed Apr 24 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-3
- Add pyside-tools as a BuildRequires.
- Add BuildArch = noarch
- Add commands to update icon cache
- Add INSTALL="install -p" to preserve timestamps of installed files

* Mon Apr 22 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-2
- Add qt3-devel as a BuildRequires and qt3 as a Requires.

* Sat Mar 30 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-1
- Update to new release 0.3 from upstream.

* Mon Mar 25 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-11.eba2b22
- Update eba2b22 from develop branch (0.3-rc).

* Wed Mar 13 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-10.006cf12
- Remove BuildRoot and defattr and clean tags.
- Add comment for Patch1
- Update 006cf12 from develop branch.

* Wed Mar 13 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-9.a564b30
- Add a patch to fix the python2 version to run GUI settings because of
python3-pyside not available at this moment (obsolete).

* Wed Mar 13 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-8.a564b30
- Update a564b30 from develop branch.
- Update release number to 0.2.x for more suitable with upstream.

* Mon Mar 11 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-7.d5b92ec
- Update d5b92ec from develop branch.

* Sat Mar 2 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-6.6b003a1
- Add a patch to fix the program files location to /usr/libexec.

* Sat Mar 2 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-5.6b003a1
- Update 6b003a1 from develop branch.

* Fri Mar 1 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-4.c65e3f9
- Update c65e3f9 from develop branch.

* Thu Feb 28 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-3.7163ca3
- Update 7163ca3 from develop branch.

* Wed Feb 27 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-2.2b8ffb4
- Update 2b8ffb4 from develop branch.

* Tue Feb 26 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-1.92b2013
- Initial release getting from develop branch.

