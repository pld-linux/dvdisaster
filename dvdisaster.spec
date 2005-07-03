# TODO:
# - make desktop file
#
Summary:	dvdisaster - Additional error correction for CD and DVD media
Summary(pl):	dvdisaster - dodatkowa korekcja b³êdów dla no¶ników CD i DVD
Name:		dvdisaster
Version:	0.62
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/dvdisaster/%{name}-%{version}.tbz
# Source0-md5:	0959193113bd59d043942f7cb4054498
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.dvdisaster.com/
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

%description -l pl
dvdisaster zapewnia margines bezpieczeñstwa przed utrat± danych na
no¶nikach CD i DVD spowodowan± wiekem lub rysami.

- dvdisaster tworzy kody korekcji b³êdów równowa¿±ce b³êdy odczytu
  niemo¿liwe do poprawienia przez napêd CD/DVD.

- dvdisaster próbuje odczytaæ tyle danych ile to tylko mo¿liwe z
  uszkodzonego no¶nika. Nastêpnie odzyskuje nieczytelne sektory przy
  u¿yciu poprzednio utworzonego kodu korekcji b³êdów. Maksymalna
  mo¿liwo¶æ korekcji b³êdów jest wybierana przez u¿ytkownika.

Je¶li w porê utworzymy plik z kodem korekcji b³êdów i bêdziemy trzymaæ
go w bezpiecznym miejscu, mamy du¿e szanse odzyskania zawarto¶ci
no¶nika przy typowych b³êdach odczytu i przeniesienia ca³ych danych na
nowy no¶nik.

%prep
%setup -q
%patch0 -p1

%build
%{__sed} -i 's,gawk,awk,g' locale/create-makefile
%configure2_13
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS DRIVE-NOTES README TODO TRANSLATION.HOWTO
%doc documentation/en documentation/images
%lang(de) %doc documentation/de
%attr(755,root,root) %{_bindir}/*
