Summary:	Thai TrueType fonts
Name:		fonts-ttf-thai
Version:	0.4.17
Release:	9
# Waree font is licensed under Bitstream license
License:	GPLv2+ and Bitstream Vera Fonts Copyright
Group:		System/Fonts/True type
Url:		http://linux.thai.net/projects/thaifonts-scalable
Source0:	ftp://linux.thai.net/pub/ThaiLinux/software/thai-ttf/thai-ttf-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	ttmkfdir

%description
This Package provides Free Thai TrueType fonts.

%prep
%setup -qn thai-ttf-%{version}

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/TTF/thai/
cp *.ttf %{buildroot}/%{_datadir}/fonts/TTF/thai/

(
cd %{buildroot}/%{_datadir}/fonts/TTF/thai/
%_bindir/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/thai \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-thai:pri=50


%files
%dir %{_datadir}/fonts/TTF/
%dir %{_datadir}/fonts/TTF/thai/
%{_datadir}/fonts/TTF/thai/*
%{_sysconfdir}/X11/fontpath.d/ttf-thai:pri=50

