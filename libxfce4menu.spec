Summary:	Menu library for the Xfce desktop environment
Summary(pl.UTF-8):	Biblioteka menu dla środowiska Xfce
Name:		libxfce4menu
Version:	4.6.2
Release:	2
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ff10cacb76803ee37159e3a43345f0d1
URL:		http://www.xfce.org/projects/libraries/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libxfce4util-devel >= 4.6.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxfce4menu is a Freedesktop.org compliant menu library written for the Xfce desktop environment.

%description -l pl.UTF-8
libxfce4menu jest biblioteką menu zgodną z Freedesktop.org napisaną dla środowiska Xfce.

%package devel
Summary:	Header files for libxfce4menu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfce4menu
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libxfce4util-devel >= %{version}

%description devel
Header files for libxfce4menu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxfce4menu.

%package static
Summary:	Static libxfce4menu library
Summary(pl.UTF-8):	Statyczna biblioteka libxfce4menu
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4menu library.

%description static -l pl.UTF-8
Statyczna biblioteka libxfce4menu.

%package apidocs
Summary:	libxfce4menu library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libxfce4menu
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4menu library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libxfce4menu.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}-0.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README STATUS TODO
%attr(755,root,root) %{_libdir}/libxfce4menu-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4menu-0.1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4menu-0.1.so
%{_libdir}/libxfce4menu-0.1.la
%{_includedir}/xfce4/libxfce4menu-0.1
%{_pkgconfigdir}/libxfce4menu-0.1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4menu-0.1.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxfce4menu
