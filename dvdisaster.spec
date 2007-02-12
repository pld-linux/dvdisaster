Summary:	dvdisaster - Additional error correction for CD and DVD media
Summary(pl.UTF-8):   dvdisaster - dodatkowa korekcja błędów dla nośników CD i DVD
Name:		dvdisaster
Version:	0.70.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/dvdisaster/%{name}-%{version}.tar.bz2
# Source0-md5:	350b76ccaf2c8f08dcd26643ec359614
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-configure.patch
URL:		http://www.dvdisaster.com/
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvdisaster provides a margin of safety against data loss on CD and DVD
media caused by aging or scratches.

 - dvdisaster creates error correction codes to compensate read errors
   which are not correctable in the CD/DVD drive.

 - dvdisaster tries to read as much data as possible from defective
   media. Afterwards unreadable sectors are recovered using the
   previously created error correction code. The maximum error correction
   capacity is user-selectable.

If you create the error correction code file in time and keep it at a
safe place, you have a good chance of recovering the medium contents
from typical read errors and to transfer your complete data onto a new
medium.

%description -l pl.UTF-8
dvdisaster zapewnia margines bezpieczeństwa przed utratą danych na
nośnikach CD i DVD spowodowaną wiekem lub rysami.

- dvdisaster tworzy kody korekcji błędów równoważące błędy odczytu
  niemożliwe do poprawienia przez napęd CD/DVD.

- dvdisaster próbuje odczytać tyle danych ile to tylko możliwe z
  uszkodzonego nośnika. Następnie odzyskuje nieczytelne sektory przy
  użyciu poprzednio utworzonego kodu korekcji błędów. Maksymalna
  możliwość korekcji błędów jest wybierana przez użytkownika.

Jeśli w porę utworzymy plik z kodem korekcji błędów i będziemy trzymać
go w bezpiecznym miejscu, mamy duże szanse odzyskania zawartości
nośnika przy typowych błędach odczytu i przeniesienia całych danych na
nowy nośnik.

%prep
%setup -q -n %{name}-0.70
%patch0 -p0
%patch1 -p1

%build
%{__sed} -i 's,gawk,awk,g' locale/create-makefile
%configure2_13 \
	--buildroot=$RPM_BUILD_ROOT \
	--docdir=%{_docdir} \
	--localedir=%{_datadir}/locale
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install

install contrib/dvdisaster48.png $RPM_BUILD_ROOT%{_pixmapsdir}
install contrib/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS.en README TODO TRANSLATION.HOWTO
%doc documentation/en documentation/images
%lang(cs) %doc CREDITS.cs documentation/cs
%lang(de) %doc CREDITS.de documentation/de
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(it) %{_mandir}/it/man1/*
%{_pixmapsdir}/*
