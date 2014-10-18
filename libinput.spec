Summary:	Generic input device handling library
Name:		libinput
Version:	0.6.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/libinput/%{name}-%{version}.tar.xz
# Source0-md5:	3afaf9f66d8796323a79edb879c10ba3
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
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
%attr(755,root,root) %ghost %{_libdir}/libinput.so.5
%attr(755,root,root) %{_libdir}/libinput.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinput.so
%{_includedir}/libinput.h
%{_pkgconfigdir}/libinput.pc

