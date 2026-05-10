%global modname numpy

# To prepare for the future changes in RPM macro support
%if ! %{defined python3_sitearch}
%define python3_sitearch /%{_libdir}/python3.?/site-packages
%endif

%if ! %{defined python3_sitelib}
%define python3_sitelib %{python3_sitearch}
%endif

Name:           numpy
Version:        2.4.4
Release:        1
Summary:        A fast multidimensional array facility for Python

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:        BSD and Python and ASL 2.0
URL:            http://www.numpy.org/
Source0:        %{name}-%{version}.tar.gz

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.


%package -n python3-numpy
Summary:        A fast multidimensional array facility for Python

License:        BSD
%{?python_provide:%python_provide python3-numpy}
Provides:       libnpymath-static = %{version}-%{release}
Provides:       libnpymath-static%{?_isa} = %{version}-%{release}

BuildRequires:  python3-devel >= 3.11
BuildRequires:  python3-setuptools
BuildRequires:  python3-cython
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(toml)
BuildRequires:  meson
#BuildRequires:  python3-pytest
#BuildRequires:  gcc-gfortran gcc
#BuildRequires:  openblas-devel

%description -n python3-numpy
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.

%package -n python3-numpy-f2py
Summary:        f2py for numpy
Requires:       python3-numpy%{?_isa} = %{version}-%{release}
Requires:       python3-devel
Provides:       python3-f2py = %{version}-%{release}

%description -n python3-numpy-f2py
This package includes a version of f2py that works properly with NumPy.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%pyproject_wheel

%install
%pyproject_install

pushd %{buildroot}%{_bindir} &> /dev/null
ln -s f2py3 f2py.numpy
popd &> /dev/null

#symlink for includes, BZ 185079
mkdir -p %{buildroot}%{_includedir}
ln -s %{python3_sitearch}/%{name}/core/include/numpy/ %{buildroot}%{_includedir}/numpy


%files -n python3-numpy
%license LICENSE.txt
%doc THANKS.txt site.cfg.example
%{python3_sitearch}/%{name}/__pycache__
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/*.py*
%{python3_sitearch}/%{name}/core
%{python3_sitearch}/%{name}/distutils
%{python3_sitearch}/%{name}/doc
%{python3_sitearch}/%{name}/fft
%{python3_sitearch}/%{name}/lib
%{python3_sitearch}/%{name}/linalg
%{python3_sitearch}/%{name}/ma
%{python3_sitearch}/%{name}/random
%{python3_sitearch}/%{name}/testing
%{python3_sitearch}/%{name}/tests
%{python3_sitearch}/%{name}/compat
%{python3_sitearch}/%{name}/matrixlib
%{python3_sitearch}/%{name}/polynomial
%{python3_sitearch}/%{name}-*.egg-info
%exclude %{python3_sitearch}/%{name}/LICENSE.txt
%{_includedir}/numpy

%files -n python3-numpy-f2py
%{_bindir}/f2py*
%{python3_sitearch}/%{name}/f2py
