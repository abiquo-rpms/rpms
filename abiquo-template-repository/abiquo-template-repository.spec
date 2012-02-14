%define abiquo_basedir /opt/abiquo

Name:     abiquo-template-repository
Version:  0.1
Release:  1%{?dist}%{?buildstamp}
Summary:  Abiquo Template Repository Application
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  https://github.com/downloads/abiquo/template-repository/template-repository.war
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the Abiquo Template Repository application.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/template-repository/ %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/template-repository

%changelog
* Thu Aug 04 2011 Sergio Rubio <srubio@abiquo.com> - 0.1-1
- initial release

