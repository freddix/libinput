Summary:	Generic input device handling library
Name:		libinput
Version:	0.12.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/libinput/%{name}-%{version}.tar.xz
# Source0-md5:	cc1a8c710a90264d1464c81d657064d2
URL:		http://www.freedesktop.org/wiki/Software/libinput/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libevdev-devel
BuildRequires:	libtool
BuildRequires:	mtdev-devel
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libinput is a generic input device handling library. It
abstracts commonly-used concepts such as keyboard, pointer
and touchpad handling behind an API.

%package devel
Summary:	Header files for libinput library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libevdev library.

%package -n udev-%{name}
Summary:	udev rule for USB input device
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev

%description -n udev-%{name}
udev rule for USB input devices supported by libinput.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-udev-dir=%{_prefix}/lib/udev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %ghost %{_libdir}/libinput.so.10
%attr(755,root,root) %{_libdir}/libinput.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinput.so
%{_includedir}/libinput.h
%{_pkgconfigdir}/libinput.pc

%files -n udev-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/lib/udev/libinput-device-group
%{_prefix}/lib/udev/rules.d/80-libinput-device-groups.rules

