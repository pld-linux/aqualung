#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
%define	_beta	beta6
%define	_rel	1
Summary:	Aqualung - music player for Linux
Summary(pl):	Aqualung - odtwarzacz muzyki dla Linuksa
Name:		aqualung
Version:	0.9
Release:	0.%{_beta}.%{_rel}
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/aqualung/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	4a019e923316615ad117548a87d4792e
URL:		http://aqualung.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblrdf-devel >= 0.3.7
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aqualung is a new music player for the GNU/Linux operating system. It
plays audio files from your filesystem and has the feature of
inserting no gaps between adjacent tracks.

%description -l pl
Aqualung to nowy odtwarzacz muzyki dla systemu operacyjnego GNU/Linux.
Odtwarza pliki d¼wiêkowe z systemu plików i ma mo¿liwo¶æ nie
wstawiania przerw miêdzy ¶cie¿kami.

%prep
%setup -q -n %{name}-%{version}%{_beta}

%{__perl} -pi -e 's/CFLAGS="-O3/CFLAGS="\$CFLAGS/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_alsa:--without-alsa}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
