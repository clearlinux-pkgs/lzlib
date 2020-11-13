#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8FE99503132D7742 (antonio@gnu.org)
#
Name     : lzlib
Version  : 1.11
Release  : 4
URL      : http://download.savannah.gnu.org/releases/lzip/lzlib/lzlib-1.11.tar.gz
Source0  : http://download.savannah.gnu.org/releases/lzip/lzlib/lzlib-1.11.tar.gz
Source1  : http://download.savannah.gnu.org/releases/lzip/lzlib/lzlib-1.11.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: lzlib-info = %{version}-%{release}
Requires: lzlib-lib = %{version}-%{release}
Requires: lzlib-license = %{version}-%{release}

%description
Description
Lzlib is a data compression library providing in-memory LZMA compression
and decompression functions, including integrity checking of the
decompressed data. The compressed data format used by the library is the
lzip format. Lzlib is written in C.

%package dev
Summary: dev components for the lzlib package.
Group: Development
Requires: lzlib-lib = %{version}-%{release}
Provides: lzlib-devel = %{version}-%{release}
Requires: lzlib = %{version}-%{release}

%description dev
dev components for the lzlib package.


%package info
Summary: info components for the lzlib package.
Group: Default

%description info
info components for the lzlib package.


%package lib
Summary: lib components for the lzlib package.
Group: Libraries
Requires: lzlib-license = %{version}-%{release}

%description lib
lib components for the lzlib package.


%package license
Summary: license components for the lzlib package.
Group: Default

%description license
license components for the lzlib package.


%prep
%setup -q -n lzlib-1.11
cd %{_builddir}/lzlib-1.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605244468
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1605244468
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lzlib
cp %{_builddir}/lzlib-1.11/COPYING %{buildroot}/usr/share/package-licenses/lzlib/d72a41edbb9850eb64165417b87b04b1a27fcf2e
cp %{_builddir}/lzlib-1.11/COPYING.GPL %{buildroot}/usr/share/package-licenses/lzlib/244611d3ffa10dc67244ec317e7235aa5779f42a
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/lzlib.h
/usr/lib64/liblz.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/lzlib.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblz.so.1
/usr/lib64/liblz.so.1.11

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lzlib/244611d3ffa10dc67244ec317e7235aa5779f42a
/usr/share/package-licenses/lzlib/d72a41edbb9850eb64165417b87b04b1a27fcf2e
