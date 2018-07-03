#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		rjsmin
%define 	egg_name	rjsmin
%define		pypi_name	rjsmin
Summary:	rJSmin is a JavaScript minifier written in Python
Name:		python-%{pypi_name}
Version:	1.0.12
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	9f67e133c88df5497d3da847603da9bf
URL:		http://opensource.perlig.de/rjsmin/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The minifier is based on the semantics of jsmin.c by Douglas
Crockford.

The module is a re-implementation aiming for speed, so it can be used
at runtime (rather than during a preprocessing step). Usually it
produces the same results as the original jsmin.c.

%package -n python3-%{pypi_name}
Summary:	rJSmin is a JavaScript minifier written in Python
Group:		Libraries/Python

%description -n python3-%{pypi_name}
The minifier is based on the semantics of jsmin.c by Douglas
Crockford.

The module is a re-implementation aiming for speed, so it can be used
at runtime (rather than during a preprocessing step). Usually it
produces the same results as the original jsmin.c.

%package apidocs
Summary:	Javascript Minifier - docs
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Docs for rJSmin

%prep
%setup -q -n %{pypi_name}-%{version}

# strip bang path from rjsmin.py
sed -i '1d' rjsmin.py

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

rm -r $RPM_BUILD_ROOT%{_docdir}/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitedir}/%{module}.py[co]
%attr(755,root,root) %{py_sitedir}/_%{module}.so
%{py_sitedir}/%{pypi_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitedir}/%{module}.py
%{py3_sitedir}/__pycache__/%{module}.*.pyc
%attr(755,root,root) %{py3_sitedir}/_%{module}.*.so
%{py3_sitedir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc README.rst docs
%endif
