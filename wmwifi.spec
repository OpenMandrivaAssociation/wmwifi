%define name	wmwifi
%define version	0.6
%define release  12

Name: 	 	%{name}
Summary: 	Wireless network monitor for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		http://digitalssg.net/debian/%{name}-%{version}.tar.bz2
URL:		http://wmwifi.digitalssg.net/
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11)
BuildRequires:	imagemagick

%description
WmWiFi should support any wireless drivers as long as those drivers support
the Linux kernels Wireless Extensions. This means that if you do a cat
/proc/net/wireles, you should see interface statistics there.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=WMWifi
Comment=Wireless network docklet
Categories=System;Monitor;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 src/display_link.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 src/display_link.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 src/display_link.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-11mdv2011.0
+ Revision: 615459
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 0.6-10mdv2010.1
+ Revision: 509136
- bump rel
- bump rel
- bump rel
- patch0 not needed

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 03 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.6-3mdv2008.1
+ Revision: 178127
- more proper fix for build if.h build issue
- fixed license tag
- finer grained X11 build requires

* Mon Mar 03 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.6-2mdv2008.1
+ Revision: 177837
- workaround wireless.h badness, so the package builds

  + Thierry Vignaud <tv@mandriva.org>
    - auto convert menu to XDG
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import wmwifi

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Mar 22 2006 Austin Acton <austin@mandriva.org> 0.6-1mdk
- 0.6
- source URL

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.5-2mdk
- Rebuild

* Sun Sep 26 2004 Austin Acton <austin@mandrake.org> 0.5-1mdk
- 0.5

* Mon Jun 7 2004 Austin Acton <austin@mandrake.org> 0.4-1mdk
- initial package
