Summary:	A library for doing full-text indexing
Name:		akode
Version:	2.0
%define	_rc	b3
Release:	0.%{_rc}.1
License:	LGPL
Group:		Libraries
Source0:	http://www.kde-apps.org/content/files/30375-%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	b78b747e87811726ab336334038c64d8
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkg-config
BuildRequires:	polypaudio-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	speex-devel
URL:		http://www.carewolf.com/akode
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
%setup -q -n %{name}-%{version}%{_rc}

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
