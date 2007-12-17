%define name	wmwifi
%define version	0.6
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Wireless network monitor for Window Maker
Version: 	%{version}
Release: 	%{release}

Source:		http://digitalssg.net/debian/%{name}-%{version}.tar.bz2
URL:		http://wmwifi.digitalssg.net/
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRequires:	pkgconfig ImageMagick X11-devel

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
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="WMWifi" longtitle="Wireless network docklet" section="System/Monitoring"
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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

