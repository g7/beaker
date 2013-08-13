Name: python-beaker
Version: 1.6.4
Release: 1
Summary: WSGI middleware layer to provide sessions

Group: Development/Languages
License: BSD and MIT
URL: http://beaker.groovie.org/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%prep
%setup -q -n %{name}-%{version}

%build
cd beaker
%{__python} setup.py build

%install
cd beaker
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build \
	--root $RPM_BUILD_ROOT \
	--install-headers=%{_includedir}/python \
	--install-lib=%{python_sitelib}

rm -rf $RPM_BUILD_ROOT/%{python_sitelib}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc beaker/LICENSE beaker/CHANGELOG
%{python_sitelib}/beaker/
%{python_sitelib}/Beaker*
