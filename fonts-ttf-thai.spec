Summary:	Thai TrueType fonts
Name:		fonts-ttf-thai
Version:	0.4.13
Release:	%mkrel 6
# Waree font is licensed under Bitstream license
License:	GPLv2+ and Bitstream Vera Fonts Copyright
Group:		System/Fonts/True type

Source0:	ftp://linux.thai.net/pub/ThaiLinux/software/thai-ttf/thai-ttf-%{version}.tar.gz
URL:		http://linux.thai.net/projects/thaifonts-scalable
BuildArch:	noarch
BuildRequires: fontconfig
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



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.4.13-6mdv2011.0
+ Revision: 675429
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.4.13-5
+ Revision: 675189
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.13-4
+ Revision: 664338
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 0.4.13-3mdv2011.0
+ Revision: 605799
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.4.13-2mdv2010.1
+ Revision: 494156
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Funda Wang <fwang@mandriva.org> 0.4.13-1mdv2010.0
+ Revision: 428325
- New verison 0.4.13

* Mon Mar 23 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.4.11-1mdv2009.1
+ Revision: 360569
- Updated to version 0.4.11

* Sun Jul 20 2008 Funda Wang <fwang@mandriva.org> 0.4.10-1mdv2009.0
+ Revision: 238860
- clearify the license
- New version 0.4.10

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.9-3mdv2009.0
+ Revision: 220955
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.9-2mdv2008.1
+ Revision: 170839
- rebuild

* Tue Jan 29 2008 Funda Wang <fwang@mandriva.org> 0.4.9-1mdv2008.1
+ Revision: 159638
- New version 0.4.9

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.1-13mdv2008.1
+ Revision: 149941
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.1-12mdv2008.0
+ Revision: 48747
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:12:16 (52895)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 20:58:07 (52789)
- import fonts-ttf-thai-0.1-10mdk

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.1-10mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)
- Remove dependency on freetype, this is old stuff

