#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyasn1_modules
Version  : 0.3.0
Release  : 75
URL      : https://files.pythonhosted.org/packages/3b/e4/7dec823b1b5603c5b3c51e942d5d9e65efd6ff946e713a325ed4146d070f/pyasn1_modules-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/e4/7dec823b1b5603c5b3c51e942d5d9e65efd6ff946e713a325ed4146d070f/pyasn1_modules-0.3.0.tar.gz
Summary  : A collection of ASN.1-based protocols modules
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-pyasn1_modules-license = %{version}-%{release}
Requires: pypi-pyasn1_modules-python = %{version}-%{release}
Requires: pypi-pyasn1_modules-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyasn1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ASN.1 modules for Python
------------------------
[![PyPI](https://img.shields.io/pypi/v/pyasn1-modules.svg?maxAge=2592000)](https://pypi.org/project/pyasn1-modules)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyasn1-modules.svg)](https://pypi.org/project/pyasn1-modules/)
[![Build status](https://github.com/pyasn1/pyasn1-modules/actions/workflows/main.yml/badge.svg)](https://github.com/pyasn1/pyasn1-modules/actions/workflows/main.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/pyasn1/pyasn1-modules.svg)](https://codecov.io/github/pyasn1/pyasn1-modules)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/pyasn1/pyasn1-modules/master/LICENSE.txt)

%package license
Summary: license components for the pypi-pyasn1_modules package.
Group: Default

%description license
license components for the pypi-pyasn1_modules package.


%package python
Summary: python components for the pypi-pyasn1_modules package.
Group: Default
Requires: pypi-pyasn1_modules-python3 = %{version}-%{release}

%description python
python components for the pypi-pyasn1_modules package.


%package python3
Summary: python3 components for the pypi-pyasn1_modules package.
Group: Default
Requires: python3-core
Provides: pypi(pyasn1_modules)
Requires: pypi(pyasn1)

%description python3
python3 components for the pypi-pyasn1_modules package.


%prep
%setup -q -n pyasn1_modules-0.3.0
cd %{_builddir}/pyasn1_modules-0.3.0
pushd ..
cp -a pyasn1_modules-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682010711
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyasn1_modules
cp %{_builddir}/pyasn1_modules-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pyasn1_modules/ae92c56eafb6dec8da4a2308a9f5f52d46167789 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyasn1_modules/ae92c56eafb6dec8da4a2308a9f5f52d46167789

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
