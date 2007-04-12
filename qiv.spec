%define pre pre10
%define rel 0.%pre.4
Name:		qiv
Version:	2.1
Release:	%mkrel %rel
Summary:	Gdk/imlib image viewer
Source0:	http://www.klografx.net/qiv/devel/%{name}-%{version}-%pre.tar.bz2
# (fc) 2.0-2mdk fix dither on 15bpp display
Patch0:		qiv-2.0-dither.patch
# (gb) 2.0-3mdk varargs fixes, though harmless here (ia32, x86_64)
Patch1:		qiv-2.0-varargs.patch
# (boiko) 2.1-0.pre10.4 set the wmclass_class which is used by gdk_window_new
Patch2:		qiv-wmclass_fix.patch
License:	GPL
Url:    	http://www.klografx.net/qiv/index2.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgtk+-devel libgdkimlib-devel 
Group:		Graphics

%description
qiv is a fast image viewer for X based on gdk and imlib.

%prep
%setup -q
%patch0 -p1 -b .dither
%patch1 -p1 -b .varargs
%patch2 -p1 -b .wmclass

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
%doc README README.CHANGES README.COPYING README.INSTALL
%{_bindir}/qiv
%{_bindir}/qiv-command
%{_mandir}/man1/qiv.1*


