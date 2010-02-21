%define name	wmwifi
%define version	0.6
%define release %mkrel 10

Name: 	 	%{name}
Summary: 	Wireless network monitor for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		http://digitalssg.net/debian/%{name}-%{version}.tar.bz2
URL:		http://wmwifi.digitalssg.net/
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRequires:	libx11-devel
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

