%define		_snap	051113
Summary:	A library for doing full-text indexing
Name:		akode
Version:	2.0.89.%{_snap}
Release:	1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	a0a6ea32e79be8971c2358ed64dad8f5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for doing full-text indexing.

%package devel
Summary:        Header files for akode libraries
Summary(pl):    Pliki nagłówkowe bibliotek akode
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for akode libraries.

%description devel -l pl
Pliki nagłówkowe bibliotek akode.

%prep
%setup -q -n %{name}-%{_snap}

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akodeplay
%attr(755,root,root) %{_libdir}/libakode.la
%attr(755,root,root) %{_libdir}/libakode.so.*.*.*
%{_libdir}/libakode_*.la
%attr(755,root,root) %{_libdir}/libakode_*.so
%{_libdir}/mcop/akode*PlayObject.mcopclass

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akode-config
#{_includedir}/*.h
%{_includedir}/akode
%{_libdir}/libakode.so
