Name:           libtool
Version:        2.4.6
Release:        29%{?dist}
Summary:        A Tool to Build Shared Libraries
License:        GPLv2+ and LGPLv2+ and GFDL
Group:          core
Url:            http://www.gnu.org/software/libtool/
Source:         http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf
and GNU Automake).
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --libdir=%{_libdir}
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir
%files
%license COPYING
%doc AUTHORS NEWS README THANKS TODO ChangeLog*
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_includedir}/ltdl.h
%{_includedir}/libltdl
%{_datadir}/libtool
%{_mandir}/man1/libtool.1*
%{_mandir}/man1/libtoolize.1*
%{_datadir}/aclocal/*.m4
%{_infodir}/libtool.info*.gz
%{_libdir}/libltdl.a
%attr(644, root, root) %{_libdir}/libltdl.la
%{_libdir}/libltdl.so*
%{_prefix}/lib/libltdl.a
%attr(644, root, root) %{_prefix}/lib/libltdl.la
%{_prefix}/lib/libltdl.so*