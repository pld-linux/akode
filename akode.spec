Summary:	A library for doing full-text indexing
Name:		akode
Version:	050926
Release:	1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	0f93efbd6a93253f337efab5ee9043d7
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
Summary(pl):    Pliki nag³ówkowe bibliotek akode
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for akode libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek akode.

%prep
%setup -q

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
