Summary:	Thai TrueType fonts
Name:		fonts-ttf-thai
Version:	0.4.13
Release:	%mkrel 3
# Waree font is licensed under Bitstream license
License:	GPLv2+ and Bitstream Vera Fonts Copyright
Group:		System/Fonts/True type

Source0:	ftp://linux.thai.net/pub/ThaiLinux/software/thai-ttf/thai-ttf-%{version}.tar.gz
URL:		http://linux.thai.net/projects/thaifonts-scalable
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	ttmkfdir
Obsoletes:	thai-ttf
Provides:	thai-ttf

%description
This Package provides Free Thai TrueType fonts.

%prep
%setup -q -n thai-ttf-%{version}

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/thai/
cp *.ttf %buildroot/%_datadir/fonts/TTF/thai/

(
cd %buildroot/%_datadir/fonts/TTF/thai/
%_bindir/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/thai \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-thai:pri=50


%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/thai/
%_datadir/fonts/TTF/thai/*
%_sysconfdir/X11/fontpath.d/ttf-thai:pri=50

