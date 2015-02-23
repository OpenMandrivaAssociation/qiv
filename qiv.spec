Name:		qiv
Version:	2.3.1
Release:	1
Summary:	Gdk/imlib image viewer
Group:		Graphics
License:	GPL+
Url:		http://spiegl.de/qiv/
Source0:	http://spiegl.de/qiv/download/%{name}-%{version}.tgz
Patch0:		qiv-2.2.4-no-strip.patch
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(xinerama)

%description
qiv is a fast image viewer for X based on gdk and imlib.

%prep
%setup -q
%patch0 -p1

%build
%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}

#don't change this to %_mandir, since Makefile is not BM

mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
perl -pi -e 's!PREFIX\)/man/man1!PREFIX\)/share/man/man1!g' Makefile
DISPLAY="" make PREFIX=%{buildroot}%{_prefix} install
cp contrib/%{name}-command.example %{buildroot}%{_bindir}/%{name}-command

%files
%doc README Changelog README.COPYING README.INSTALL
%{_bindir}/qiv
%{_bindir}/qiv-command
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/qiv.1*
