Summary:    A GNU set of database routines which use extensible hashing
Name:       gdbm
Version:    1.18.1
Release:    3%{?dist}
Epoch:      1
License:    GPLv3+
URL:        http://www.gnu.org/software/gdbm/
Group:      core
Source0:     http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz
Source1:     http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz.sig
%description
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

If you're a C developer and your programs need access to simple
database routines, you should install gdbm.  You'll also need to
install gdbm-devel.
%prep
%setup -q

%build
%configure --prefix=%{_prefix} --disable-rpath --enable-libgdbm-compat

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gdbm 
ln -sf ../gdbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/gdbm.h
ln -sf ../ndbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/ndbm.h
ln -sf ../dbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/dbm.h
# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%check
export LD_LIBRARY_PATH=`pwd`/src/.libs/:`pwd`/compat/.libs/
make check
%files
%license COPYING
%doc NEWS README THANKS AUTHORS NOTE-WARNING
%{_bindir}/gdbm*
%{_mandir}/man1/gdbm*
%{_libdir}/libgdbm.so.6*
%{_libdir}/libgdbm_compat.so.4*
%{_libdir}/libgdbm.so
%{_libdir}/libgdbm_compat.so
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man3/*
%{_datadir}/locale/*/LC_MESSAGES/gdbm.mo
%{_libdir}/libgdbm.a
%{_libdir}/libgdbm_compat.a