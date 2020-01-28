# Created by pyp2rpm-3.3.3
%global pypi_name peewee

Name:           python-%{pypi_name}
Version:        3.13.1
Release:        %mkrel 1
Summary:        a little orm
Group:          Development/Python
License:        MIT License
URL:            https://github.com/coleifer/peewee/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:		peewee-linking.patch
BuildRequires:  python3-devel
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:	pkgconfig(sqlite3)
# for tests
BuildRequires:	python3dist(apsw)
BuildRequires:	python3dist(psycopg2)
BuildRequires:	python3dist(sqlcipher3)

%description
Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst playhouse/README.md
%doc html
%{_bindir}/pwiz.py
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/%{pypi_name}.py
%{python3_sitearch}/pwiz.py
%{python3_sitearch}/playhouse
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
