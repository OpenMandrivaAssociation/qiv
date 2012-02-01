Name:		qiv
Version:	2.2.4
Release:	%mkrel 1
Summary:	Gdk/imlib image viewer
Source0:	http://spiegl.de/qiv/download/%{name}-%{version}.tgz
License:	GPL+
Url:    	http://spiegl.de/qiv/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	libimlib2-devel
BuildRequires:	libmagic-devel
BuildRequires:	libxinerama-devel
Group:		Graphics

%description
qiv is a fast image viewer for X based on gdk and imlib.

%prep
%setup -q -n %{name}-%{version}

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}

#don't change this to %_mandir, since Makefile is not BM

mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
perl -pi -e 's!PREFIX\)/man/man1!PREFIX\)/share/man/man1!g' Makefile
DISPLAY="" make PREFIX=$RPM_BUILD_ROOT%{_prefix} install
cp qiv-command.example %buildroot%_bindir/qiv-command

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changelog README.COPYING README.INSTALL
%{_bindir}/qiv
%{_bindir}/qiv-command
%{_mandir}/man1/qiv.1*




%changelog
* Mon May 23 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.4-1mdv2011.0
+ Revision: 677606
- update to new version 2.2.4

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-2mdv2011.0
+ Revision: 614673
- the mass rebuild of 2010.1 packages

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - update build deps
    - update license

* Wed Jan 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.3-1mdv2010.1
+ Revision: 494046
- update to new version 2.2.3

* Mon Jun 01 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.2-1mdv2010.0
+ Revision: 381834
- update to new version 2.2.2

* Sat May 30 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.1-1mdv2010.0
+ Revision: 381195
- Update to new version 2.2.1 (it's now a GTK+2 application)
- Adapt BuildRequires
- Remove old patches
- Use new URL

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.1-0.pre12.1mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 18 2007 Crispin Boylan <crisb@mandriva.org> 2.1-0.pre12.1mdv2008.0
+ Revision: 66472
- BuildRequires libxinerama-devel
- BuildRequires libxinerama
- New version, remove patch1 (merged)


* Wed Mar 07 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2.1-0.pre10.4mdv2007.1
+ Revision: 134775
- qiv should set attr.wmclass_class before calling gdk_window_new. This was
  causing crashed in x86_64 (#21417).
- Re-enabled building for x86_64

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.1-0.pre10.3mdv2007.1
+ Revision: 85963
- Import qiv

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.1-0.pre10.3mdv2007.1
- qiv doesn't work on x86_64 (#21417)

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 2.1-0.pre10.2mdv2007.0
- fix URL
- fix buildrequires

* Tue Mar 28 2006 Götz Waschk <waschk@mandriva.org> 2.1-0.pre10.1mdk
- add qiv-command
- new version

* Wed Aug 24 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.0-3mdk
- varargs fixes

* Thu Sep 16 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-2mdk
- Patch0: fix dithering on 15bpp display

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0-1mdk
- 2.0

