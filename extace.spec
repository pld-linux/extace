Summary:	Audio Visualization plugin for GNOME
Summary(pl.UTF-8):   Wtyczka do wizualizacji dźwięku dla desktopu GNOME
Name:		extace
Version:	1.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/extace/%{name}-%{version}.tar.gz
# Source0-md5:	6d430b91241460f900bf01f82920295a
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

%description
Xtace is a Audio Visualization plugin for the GNOME Desktop
Environment. It connects to ESD (Enlightened Sound Daemon) and
displays the audio data as either a 3D textured landscape, 3d pointed
landscape, 16-128 channel graphic EQ, or a colored Oscilloscope.
eXtace is based on the original eXtace written by Michael Fulbright
and The Rasterman.

%description -l pl.UTF-8
eXtace jest wtyczką do wizualizacji dźwięku dla desktopu GNOME. Łączy
się z ESD (Enlightened Sound Daemon) i wyświetla dane audio jako
trójwymiarowy krajobraz z teksturami, zwykły krajobraz trójwymiarowy,
16-128 kanałowy equalizer graficzny lub kolorowy oscyloskop. eXtace
opiera się na oryginalnym programie napisanym przez Michaela Fulbrighta
oraz The Rasterman.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
