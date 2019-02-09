Name:less
Version:530
Release:         1%{?dist}
Summary:A terminal based program for viewing text files
License:GPL3
URL:http://www.greenwoodsoftware.com/less
BuildRequires: glibc
Source:http://www.greenwoodsoftware.com/%{name}/%{name}-%{version}.tar.gz
%description
GNU nano is a small and friendly text editor.
%prep
%setup -q
%build
sh configure --prefix=/usr --sysconfdir=/etc --with-regex=pcre
make %{?_smp_mflags}
%install
make DESTDIR="%{buildroot}" install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man*/*