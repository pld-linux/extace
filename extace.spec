Summary:	
Name:		extace
Version:	1.10
Release:	1
Group:		-
Copyright:	GPL
Source:		http://techdev.buffalostate.edu/~dave/extace/archives/%{name}-%{version}.tar.gz
URL:		http://techdev.buffalostate.edu/~dave/extace/
BuildReqiires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xtace is a Audio Visualization plugin for the Gnome Desktop Environment. It
connects to ESD (Enlightened Sound Daemon) and displays the audio data as
either a 3D textured landscape, 3d pointed landscape, 16-128 channel graphic
EQ, or a colored Oscilloscope. eXtace is based on the original eXtace
written by Michael Fulbright and The Rasterman.

%description -l pl
eXtace jest wtyczk± do wizualizacji d¼wiêku dla desktopu GNOME. £±czy siê z ESD
(Enlightened Sound Daemon) i wy¶wietla dane audio jako trójwymiarowy krajobraz
z teksturami, zwyk³y krajobraz trojwymiarowy, 16-128 kana³owy equalizer
graficzny lub kolorowy oscyloskop. eXtace opiera siê na oryginalnym programi
napisanym przez Michaela Fulbrighta oraz The Rasterman.

%prep
%setup  -q

%build
LDFLAGS="-s" ; export LDFLAGS
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
