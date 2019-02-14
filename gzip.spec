Name:           gzip
Version:        1.10
Release:        1.5
Summary:        GNU Zip Compression Utilities
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gzip/
Source:         http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
%description
The gzip package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a
very commonly used data compression program.

%prep
%setup -q
%build
./configure --prefix=%_prefix
make %{?_smp_mflags}
%check
make check %{?_smp_mflags}
%install
make DESTDIR="%{buildroot}" install
%files
%doc NEWS README AUTHORS ChangeLog THANKS TODO
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/gzip.info*
%{_datadir}/info/dir