#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.testrunner
Version  : 5.1
Release  : 38
URL      : https://files.pythonhosted.org/packages/45/1f/ae2e7563ece5d158b4b474fcb1dccf48e84114c79008c6c6793d3e4f285e/zope.testrunner-5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/1f/ae2e7563ece5d158b4b474fcb1dccf48e84114c79008c6c6793d3e4f285e/zope.testrunner-5.1.tar.gz
Summary  : Zope testrunner script.
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.testrunner-bin = %{version}-%{release}
Requires: zope.testrunner-license = %{version}-%{release}
Requires: zope.testrunner-python = %{version}-%{release}
Requires: zope.testrunner-python3 = %{version}-%{release}
Requires: setuptools
Requires: six
Requires: zope.exceptions
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.exceptions
BuildRequires : zope.interface

%description
=================
zope.testrunner
=================
.. image:: https://img.shields.io/pypi/v/zope.testrunner.svg
:target: https://pypi.org/project/zope.testrunner/
:alt: Latest release

%package bin
Summary: bin components for the zope.testrunner package.
Group: Binaries
Requires: zope.testrunner-license = %{version}-%{release}

%description bin
bin components for the zope.testrunner package.


%package license
Summary: license components for the zope.testrunner package.
Group: Default

%description license
license components for the zope.testrunner package.


%package python
Summary: python components for the zope.testrunner package.
Group: Default
Requires: zope.testrunner-python3 = %{version}-%{release}

%description python
python components for the zope.testrunner package.


%package python3
Summary: python3 components for the zope.testrunner package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.testrunner package.


%prep
%setup -q -n zope.testrunner-5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571504767
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.testrunner
cp %{_builddir}/zope.testrunner-5.1/LICENSE.md %{buildroot}/usr/share/package-licenses/zope.testrunner/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zope-testrunner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.testrunner/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
