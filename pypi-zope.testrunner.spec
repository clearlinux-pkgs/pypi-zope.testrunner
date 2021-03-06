#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.testrunner
Version  : 5.5
Release  : 60
URL      : https://files.pythonhosted.org/packages/f7/43/9630657f6f8df660ed46f9a52b4f1b14e837b43c5b1fb4c66d41195a0451/zope.testrunner-5.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/f7/43/9630657f6f8df660ed46f9a52b4f1b14e837b43c5b1fb4c66d41195a0451/zope.testrunner-5.5.tar.gz
Summary  : Zope testrunner script.
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.testrunner-bin = %{version}-%{release}
Requires: pypi-zope.testrunner-license = %{version}-%{release}
Requires: pypi-zope.testrunner-python = %{version}-%{release}
Requires: pypi-zope.testrunner-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(zope.exceptions)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=================
zope.testrunner
=================
.. image:: https://img.shields.io/pypi/v/zope.testrunner.svg
:target: https://pypi.org/project/zope.testrunner/
:alt: Latest release

%package bin
Summary: bin components for the pypi-zope.testrunner package.
Group: Binaries
Requires: pypi-zope.testrunner-license = %{version}-%{release}

%description bin
bin components for the pypi-zope.testrunner package.


%package license
Summary: license components for the pypi-zope.testrunner package.
Group: Default

%description license
license components for the pypi-zope.testrunner package.


%package python
Summary: python components for the pypi-zope.testrunner package.
Group: Default
Requires: pypi-zope.testrunner-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.testrunner package.


%package python3
Summary: python3 components for the pypi-zope.testrunner package.
Group: Default
Requires: python3-core
Provides: pypi(zope.testrunner)
Requires: pypi(setuptools)
Requires: pypi(six)
Requires: pypi(zope.exceptions)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-zope.testrunner package.


%prep
%setup -q -n zope.testrunner-5.5
cd %{_builddir}/zope.testrunner-5.5
pushd ..
cp -a zope.testrunner-5.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656098654
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.testrunner
cp %{_builddir}/zope.testrunner-5.5/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-zope.testrunner/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zope-testrunner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.testrunner/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
