#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	GStreamer 0.10 plugin to support Video Acceleration API
Summary(pl.UTF-8):	Wtyczka GStreamera 0.10 obsługująca Video Acceleration API
Name:		gstreamer0.10-vaapi
Version:	0.5.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/vaapi/releases/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.bz2
# Source0-md5:	849825cad1def77ab5199a2b9b1b7bdb
URL:		http://www.freedesktop.org/wiki/Software/vaapi/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gstreamer0.10-devel >= 0.10.36
BuildRequires:	gstreamer0.10-plugins-bad-devel >= 0.10.22
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.31
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	libdrm-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libva-drm-devel >= 1.1.0
BuildRequires:	libva-glx-devel >= 1.0.9
BuildRequires:	libva-wayland-devel >= 1.1.0
BuildRequires:	libva-x11-devel >= 1.0.3
BuildRequires:	pkgconfig
# libva API versions
BuildRequires:	pkgconfig(libva) >= 0.30.4
BuildRequires:	pkgconfig(libva-drm) >= 0.33.0
BuildRequires:	pkgconfig(libva-glx) >= 0.32.0
BuildRequires:	pkgconfig(libva-wayland) >= 0.33.0
BuildRequires:	pkgconfig(libva-x11) >= 0.31.0
BuildRequires:	udev-devel
BuildRequires:	wayland-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires:	glib2 >= 1:2.28.0
Requires:	gstreamer >= 0.10.36
Requires:	gstreamer-plugins-bad >= 0.10.22
Requires:	gstreamer-plugins-base >= 0.10.31
Requires:	libva >= 1.1.0
Requires:	wayland >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gstreamer-vaapi consists in a collection of VA-API based plugins for
GStreamer and helper libraries.

%description -l pl.UTF-8
gstreamer-vaapi zawiera zestaw opartych ma VA-API wtyczek dla
GStreamera i bibliotek pomocniczych.

%package devel
Summary:	Header files for GStreamer 0.10 VA-API libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek VA-API GStreamera 0.10
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer0.10-devel >= 0.10.36
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.31
Requires:	libva-drm-devel >= 1.1.0
Requires:	libva-glx-devel >= 1.0.9
Requires:	libva-wayland-devel >= 1.1.0
Requires:	libva-x11-devel >= 1.0.3

%description devel
Header files for GStreamer 0.10 VA-API helper libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek pomocniczych VA-API GStreamera 0.10.

%package static
Summary:	Static GStreamer 0.10 VA-API libraries
Summary(pl.UTF-8):	Statyczne biblioteki VA-API GStreamera 0.10
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GStreamer 0.10 VA-API libraries.

%description static -l pl.UTF-8
Statyczne biblioteki VA-API GStreamera 0.10.

%prep
%setup -q -n gstreamer-vaapi-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# gstreamer module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgst*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgstvaapi-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgstvaapi-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvaapi-0.10.so.1
%attr(755,root,root) %{_libdir}/libgstvaapi-drm-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvaapi-drm-0.10.so.1
%attr(755,root,root) %{_libdir}/libgstvaapi-glx-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvaapi-glx-0.10.so.1
%attr(755,root,root) %{_libdir}/libgstvaapi-wayland-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvaapi-wayland-0.10.so.1
%attr(755,root,root) %{_libdir}/libgstvaapi-x11-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvaapi-x11-0.10.so.1
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstvaapi.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstvaapi-0.10.so
%attr(755,root,root) %{_libdir}/libgstvaapi-drm-0.10.so
%attr(755,root,root) %{_libdir}/libgstvaapi-glx-0.10.so
%attr(755,root,root) %{_libdir}/libgstvaapi-wayland-0.10.so
%attr(755,root,root) %{_libdir}/libgstvaapi-x11-0.10.so
%{_includedir}/gstreamer-0.10/gst/vaapi
%{_pkgconfigdir}/gstreamer-vaapi-0.10.pc
%{_pkgconfigdir}/gstreamer-vaapi-drm-0.10.pc
%{_pkgconfigdir}/gstreamer-vaapi-glx-0.10.pc
%{_pkgconfigdir}/gstreamer-vaapi-wayland-0.10.pc
%{_pkgconfigdir}/gstreamer-vaapi-x11-0.10.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgstvaapi-0.10.a
%{_libdir}/libgstvaapi-drm-0.10.a
%{_libdir}/libgstvaapi-glx-0.10.a
%{_libdir}/libgstvaapi-wayland-0.10.a
%{_libdir}/libgstvaapi-x11-0.10.a
%endif
