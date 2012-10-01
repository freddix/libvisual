Summary:	Abstraction library that comes between applications and audio visualisation plugins
Name:		libvisual
Version:	0.4.0
Release:	12
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libvisual/%{name}-%{version}.tar.bz2
# Source0-md5:	d0f987abd0845e725743605fd39ef73f
URL:		http://localhost.nl/~synap/libvisual/
Patch0:		%{name}-link.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstraction library that comes between applications and audio
visualisation plugins.

%package devel
Summary:	Header files for libvisual library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvisual library.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}-0.4

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libdir}/libvisual-0.4
%attr(755,root,root) %ghost %{_libdir}/libvisual-*.so.?
%attr(755,root,root) %{_libdir}/libvisual-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*.so
%{_libdir}/libvisual-*.la
%{_includedir}/libvisual-*
%{_pkgconfigdir}/*.pc

