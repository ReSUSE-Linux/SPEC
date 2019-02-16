Name: bzip2
Version:1.0.6
Release:43.5
Summary:A Program for Compressing Files
License:BSD-3-Clause
URL:https://pilotfiber.dl.sourceforge.net/project/bzip2/%{name}-%{version}.tar.gz
Source: %{name}-%{version}.tar.gz
Patch0: bzip2-1.0.4-bzip2recover.patch
Patch1: https://gitweb.gentoo.org/repo/gentoo.git/plain/app-arch/bzip2/files/bzip2-1.0.6-CVE-2016-3189.patch
%define  srcdir %(pwd)
%description
The bzip2 program is a very powerful program for compressing files.
%prep
%setup -q
sed -e 's/^CFLAGS=\(.*\)$/CFLAGS=\1 \$(BIGFILES)/' -i ./Makefile-libbz2_so
sed -i "s|-O2|${CFLAGS}|g" Makefile
sed -i "s|-O2|${CFLAGS}|g" Makefile-libbz2_so
%patch0 -p1
%patch1 -p1
%build
make -f Makefile-libbz2_so %{?_smp_mflags}
make bzip2 bzip2recover %{?_smp_mflags}
%check
make %{?_smp_mflags} test
%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/pkgconfig,%{_includedir}}
install -dm755 $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/pkgconfig,%{_includedir}}
install -m755 bzip2-shared %{buildroot}%{_bindir}/bzip2
install -m755 bzip2recover bzdiff bzgrep bzmore %{buildroot}%{_bindir}
ln -sf bzip2 %{buildroot}%{_bindir}/bunzip2
ln -sf bzip2 %{buildroot}%{_bindir}/bzcat
install -m755 libbz2.so.1.0.6 %{buildroot}%{_libdir}
ln -s libbz2.so.%{library_version} $RPM_BUILD_ROOT%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 $RPM_BUILD_ROOT%{_libdir}/libbz2.so
ln -s libbz2.so.1.0.6 %{buildroot}%{_libdir}/libbz2.so.1.0
install -m644 bzlib.h %{buildroot}%{_includedir}
install -m644 bzip2.1 %{buildroot}%{_mandir}/man1/
ln -sf bzip2.1 %{buildroot}%{_mandir}/man1/bunzip2.1
ln -sf bzip2.1 %{buildroot}%{_mandir}/man1/bzcat.1
ln -sf bzip2.1 %{buildroot}%{_mandir}/man1/bzip2recover.1
%files
%{_bindir}/bunzip2
%{_bindir}/bzcat
%{_bindir}/bzdiff
%{_bindir}/bzgrep
%{_bindir}/bzip2
%{_bindir}/bzip2recover
%{_bindir}/bzmore
%{_libdir}/libbz2.so.*
%license LICENSE
%doc CHANGES README
%{_includedir}/bzlib.h
%{_libdir}/libbz2.so
%{_mandir}/*/*