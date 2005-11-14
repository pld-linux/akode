# TODO: split plugins by deps
Summary:	Audio-decoding framework library
Summary(pl):	Biblioteka szkieletu dekodowania d¼wiêku
Name:		akode
Version:	2.0
%define	_rc	b3
Release:	0.%{_rc}.1
License:	LGPL
Group:		Libraries
Source0:	http://www.kde-apps.org/content/files/30375-%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	b78b747e87811726ab336334038c64d8
URL:		http://www.carewolf.com/akode/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	ffmpeg-devel >= 0.4.9	(configure check fails with CVS 0.4.9)
BuildRequires:	flac-devel >= 1.1.1
BuildRequires:	jack-audio-connection-kit-devel >= 0.90
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	pkgconfig
BuildRequires:	polypaudio-devel >= 0.7
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio-decoding framework library.

%description -l pl
Biblioteka szkieletu dekodowania d¼wiêku.

%package devel
Summary:        Header files for akode library
Summary(pl):    Pliki nag³ówkowe biblioteki akode
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	libltdl-devel
Requires:	libstdc++-devel

%description devel
Header files for akode library.

%description devel -l pl
Pliki nag³ówkowe biblioteki akode.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akodeplay
%attr(755,root,root) %{_libdir}/libakode.so.*.*.*
%attr(755,root,root) %{_libdir}/libakode_*.so
%{_libdir}/libakode_*.la
%{_libdir}/mcop/akode*PlayObject.mcopclass

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akode-config
%attr(755,root,root) %{_libdir}/libakode.so
%{_libdir}/libakode.la
%{_includedir}/akode
