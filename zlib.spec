Name:           zlib
Version:        1.2.11
Release:        5.5
Summary:        Library implementing the DEFLATE compression algorithm
License:        Zlib
Group:          core
Url:            http://www.zlib.net/
Source0:        http://zlib.net/zlib-%{version}.tar.xz
Source1:        http://zlib.net/zlib-%{version}.tar.xz.asc
%description
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.
%prep
%setup -q
%build
./configure --prefix=%_prefix
make %{?_smp_mflags}
%check
make check %{?_smp_mflags}
%install
%files
%license README
%doc ChangeLog FAQ
%doc doc/algorithm.txt test/example.c
