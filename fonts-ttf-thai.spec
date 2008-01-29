Summary:	Free Thai TrueType fonts
Name:		fonts-ttf-thai
Version:	0.4.9
Release:	%mkrel 1
License:	Distributable
Group:		System/Fonts/True type

Source0:	ftp://linux.thai.net/pub/ThaiLinux/software/thai-ttf/thai-ttf-%{version}.tar.gz
URL:		http://linux.thai.net/projects/thaifonts-scalable
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools

Obsoletes:	thai-ttf
Provides:	thai-ttf
Requires(post): fontconfig
Requires(postun): fontconfig

%description
This Package provides Free Thai TrueType fonts.

%prep

%setup -q -n thai-ttf-%{version}

%build

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/thai/
cp *.ttf %buildroot/%_datadir/fonts/TTF/thai/

(
cd %buildroot/%_datadir/fonts/TTF/thai/
%_sbindir/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/thai \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-thai:pri=50


%post
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/thai/
%_datadir/fonts/TTF/thai/*
%_sysconfdir/X11/fontpath.d/ttf-thai:pri=50

