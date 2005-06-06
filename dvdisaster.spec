Summary:	dvdisaster - Additional error correction for CD and DVD media
Name:		dvdisaster
Version:	0.55
Release:	1
License:	GPL v2
Group:		Development
Source0:	http://download.berlios.de/dvdisaster/%{name}-%{version}.tgz
# Source0-md5:	4641d8f569f387f2f85ff4bf17b453ac
URL:		http://dvdisaster.berlios.de
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

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D dvdisaster  $RPM_BUILD_ROOT%{_bindir}/dvdisaster

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TRANSLATION.HOWTO CREDITS documentation/*
%attr(755,root,root) %{_bindir}/*
