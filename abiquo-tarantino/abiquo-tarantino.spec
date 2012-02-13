%define abiquo_basedir /opt/abiquo

Name:     abiquo-tarantino
Version:  2.0
Release:  2%{?dist}%{?buildstamp}
Summary:  Abiquo Tarantino
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{?abiquo_binaries_url}tarantino.war
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
Obsoletes: abiquo-virtualfactory
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the enterprise Tarantino component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/tarantino/ %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/tarantino

%changelog
* Thu Jan 26 2012 Sergio Rubio <srubio@abiquo.com> - 2.0-2
- Obsoletes abiquo-virtualfactory

* Mon Dec 19 2011 Sergio Rubio <rubiojr@frameos.org> - 2.0-1
- initial release

