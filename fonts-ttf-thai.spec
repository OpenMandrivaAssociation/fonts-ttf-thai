Summary:	Free Thai TrueType fonts
Name:		fonts-ttf-thai
Version:	0.1
Release:	%mkrel 12
License:	Distributable
Group:		System/Fonts/True type

Source0:	fonts-ttf-thai-norasi.tar.bz2

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

%setup -q -c

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
%doc README
#
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/thai/
%_datadir/fonts/TTF/thai/*
%_sysconfdir/X11/fontpath.d/ttf-thai:pri=50
