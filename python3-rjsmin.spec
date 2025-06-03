#
# Conditional build:
%bcond_without	doc	# don't build doc

%define		module		rjsmin
Summary:	rJSmin is a JavaScript minifier written in Python
Name:		python3-%{module}
Version:	1.2.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	a20ad5596df006d9b94769e0405d5716
URL:		http://opensource.perlig.de/rjsmin/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The minifier is based on the semantics of jsmin.c by Douglas
Crockford.

The module is a re-implementation aiming for speed, so it can be used
at runtime (rather than during a preprocessing step). Usually it
produces the same results as the original jsmin.c.

%package apidocs
Summary:	Javascript Minifier - docs
Group:		Documentation
BuildArch:	noarch

%description apidocs
Docs for rJSmin

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py3_sitedir}/%{module}.py
%{py3_sitedir}/__pycache__/%{module}.*.pyc
%attr(755,root,root) %{py3_sitedir}/_%{module}.*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs
%endif
