Name:		python-bleach-allowlist
Version:	1.0.3
Release:	1
Summary:	Curated lists of tags and attributes for sanitizing html
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/bleach-allowlist/
Source0:	bleach-allowlist-1.0.3.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Curated lists of tags and attributes for sanitizing html.

%files
%{py_sitedir}/*
