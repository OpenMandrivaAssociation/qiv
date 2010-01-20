Name:		qiv
Version:	2.2.3
Release:	%mkrel 1
Summary:	Gdk/imlib image viewer
Source0:	http://spiegl.de/qiv/download/%{name}-%{version}.tgz
License:	GPL
Url:    	http://spiegl.de/qiv/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	libexif-devel
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


