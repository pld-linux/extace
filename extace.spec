Summary:	
Name:		extace
Version:	1.10
Release:	1
Group:		-
Copyright:	GPL
Source:		http://techdev.buffalostate.edu/~dave/extace/archives/%{name}-%{version}.tar.gz
URL:		http://techdev.buffalostate.edu/~dave/extace/
BuildReqiires:	-
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Xtace is a Audio Visualization plugin for the Gnome Desktop Environment. It
connects to ESD (Enlightened Sound Daemon) and displays the audio data as
either a 3D textured landscape, 3d pointed landscape, 16-128 channel graphic
EQ, or a colored Oscilloscope. eXtace is based on the original eXtace
written by Michael Fulbright and The Rasterman.

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
