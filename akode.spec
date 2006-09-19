# TODO: split plugins by deps
Summary:	Audio-decoding framework library
Summary(pl):	Biblioteka szkieletu dekodowania d¼wiêku
Name:		akode
Version:	2.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.kde-apps.org/content/files/30375-%{name}-%{version}.tar.bz2
# Source0-md5:	94a10e7729b20b669bc5c7721f62e162
Patch0:		%{name}-pulseaudio.patch
Patch1:		kde-ac260.patch
Patch2:		kde-ac260-lt.patch
URL:		http://www.carewolf.com/akode/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.4.9-3.20050806.5
BuildRequires:	flac-devel >= 1.1.1
BuildRequires:	jack-audio-connection-kit-devel >= 0.90
BuildRequires:	faad2-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libx264-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio-decoding framework library.

%description -l pl
Biblioteka szkieletu dekodowania d¼wiêku.

%package devel
Summary:	Header files for akode library
Summary(pl):	Pliki nag³ówkowe biblioteki akode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libltdl-devel
Requires:	libstdc++-devel

%description devel
Header files for akode library.

%description devel -l pl
Pliki nag³ówkowe biblioteki akode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

USER_INCLUDES="-I%{_includedir}/speex" \
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-flac \
	--with-speex \
	--with-libmad \
	--with-libsamplerate \
	--with-jack \
	--with-pulseaudio \
	--with-ffmpeg \
	--with-oss \
	--with-alsa \
	--with-vorbis \
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
# plugins
%{_libdir}/libakode_alsa_sink.la
%attr(755,root,root) %{_libdir}/libakode_alsa_sink.so
%{_libdir}/libakode_ffmpeg_decoder.la
%attr(755,root,root) %{_libdir}/libakode_ffmpeg_decoder.so
%{_libdir}/libakode_jack_sink.la
%attr(755,root,root) %{_libdir}/libakode_jack_sink.so
%{_libdir}/libakode_mpc_decoder.la
%attr(755,root,root) %{_libdir}/libakode_mpc_decoder.so
%{_libdir}/libakode_mpeg_decoder.la
%attr(755,root,root) %{_libdir}/libakode_mpeg_decoder.so
%{_libdir}/libakode_oss_sink.la
%attr(755,root,root) %{_libdir}/libakode_oss_sink.so
%{_libdir}/libakode_polyp_sink.la
%attr(755,root,root) %{_libdir}/libakode_polyp_sink.so
%{_libdir}/libakode_src_resampler.la
%attr(755,root,root) %{_libdir}/libakode_src_resampler.so
%{_libdir}/libakode_xiph_decoder.la
%attr(755,root,root) %{_libdir}/libakode_xiph_decoder.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akode-config
%{_includedir}/akode
%{_libdir}/libakode.la
%attr(755,root,root) %{_libdir}/libakode.so
