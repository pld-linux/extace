Summary:	Audio Visualization plugin for GNOME
Summary(pl):	Wtyczka do wizualizacji d¼wiêku dla desktopu GNOME
Name:		extace
Version:	1.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/eXtace/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am-fixes.patch
URL:		http://eXtace.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	fftw-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xtace is a Audio Visualization plugin for the GNOME Desktop
Environment. It connects to ESD (Enlightened Sound Daemon) and
displays the audio data as either a 3D textured landscape, 3d pointed
landscape, 16-128 channel graphic EQ, or a colored Oscilloscope.
eXtace is based on the original eXtace written by Michael Fulbright
and The Rasterman.

%description -l pl
eXtace jest wtyczk± do wizualizacji d¼wiêku dla desktopu GNOME. £±czy
siê z ESD (Enlightened Sound Daemon) i wy¶wietla dane audio jako
trójwymiarowy krajobraz z teksturami, zwyk³y krajobraz trojwymiarowy,
16-128 kana³owy equalizer graficzny lub kolorowy oscyloskop. eXtace
opiera siê na oryginalnym programi napisanym przez Michaela Fulbrighta
oraz The Rasterman.

%prep
%setup -q
%patch -p1

%build
libtoolize --copy --force
aclocal
autoconf
rm -f missing
automake -a -c
%configure \
	--disable-debug \
%ifarch sparc sparc64
	--disable-alsa
%else
	--enable-alsa
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Multimediadir=%{_applnkdir}/Multimedia

gzip -9nf AUTHORS CREDITS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
