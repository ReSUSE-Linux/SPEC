Summary:	LZMA compression utilities
Name:		xz
Version:	5.2.4
Release:	5%{?dist}
License:	GPLv2+ and Public Domain
Source0:	http://tukaani.org/%{name}/%{name}-%{version}.tar.xz
%description
The xz command is a program for compressing files.
* Average compression ratio of LZMA is about 30%% better than that of
  gzip, and 15%% better than that of bzip2.
* Decompression speed is only little slower than that of gzip, being
  two to five times faster than bzip2.
* In fast mode, compresses faster than bzip2 with a comparable
  compression ratio.
* Achieving the best compression ratios takes four to even twelve
  times longer than with bzip2. However, this does not affect
  decompressing speed.
* Very similar command line interface to what gzip and bzip2 have.
%prep
%autosetup


%build
export CFLAGS="%optflags"
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%check
LD_LIBRARY_PATH=$PWD/src/liblzma/.libs make check
%files
%doc %_datadir/doc
%{_bindir}/*xz*
%{_mandir}/man1/*xz*
%{_libdir}/lib*.so.5*
%{_libdir}/liblzma.a
%dir %{_includedir}/lzma
%{_includedir}/lzma/*.h
%{_includedir}/lzma.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/liblzma.pc
%{_bindir}/*lz*
%{_mandir}/man1/*lz*
%{_datadir}/locale/*/LC_MESSAGES/xz.mo