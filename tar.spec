Summary: A GNU file archiving program
Name: tar
Version: 1.31
Release: 1%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/tar/
Source0: ftp://ftp.gnu.org/pub/gnu/tar/tar-%{version}.tar.bz2
Source1: ftp://ftp.gnu.org/pub/gnu/tar/tar-%{version}.tar.bz2.sig
%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.
If you want to use tar for remote backups, you also need to install
the rmt package on the remote box.

%prep
%setup -q
%build
./configure --prefix=%_prefix --libexecdir=%_libdir/tar
make %{?_smp_mflags}
%check
make check %{?_smp_mflags}
%install
%files
make -C doc install-html docdir=%_datadir/doc/tar-1.31