%define _empty_manifest_terminate_build 0
# Created by pyp2rpm-3.3.3
%global pypi_name peewee

Name:           python-%{pypi_name}
Version:        3.15.4
Release:        1
Summary:        a little orm
Group:          Development/Python
License:        MIT License
URL:            https://github.com/coleifer/peewee/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
#Patch0:		peewee-linking.patch
BuildRequires:  python-devel
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  python3dist(cython)
# for tests
#BuildRequires:	python3dist(apsw)
BuildRequires:	python3dist(psycopg2)
#BuildRequires:	python3dist(sqlcipher3)

%{?python_provide:%python_provide python-%{pypi_name}}

%description
Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

# generate html docs
#PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%files
%license LICENSE
%doc README.rst playhouse/README.md
#doc html
%{_bindir}/pwiz.py
%{python_sitearch}/%{pypi_name}.py
%{python_sitearch}/pwiz.py
%{python_sitearch}/playhouse
%{python_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
