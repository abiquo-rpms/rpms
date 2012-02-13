%define abiquo_basedir /opt/abiquo

Name:     abiquo-client-premium
Version:  2.0
Release:  1%{?dist}%{?buildstamp}
Summary:  Abiquo Flex Client
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{?abiquo_binaries_url}client-premium.war
Source1:  index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
Obsoletes: abiquo-client
BuildRequires: /usr/bin/unzip
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the enterprise client component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/client-premium/ %{SOURCE0}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/client-premium
%{abiquo_basedir}/tomcat/webapps/ROOT

%changelog
* Mon Dec 19 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- bumped version to 2.0

* Fri Sep 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-1
- bumped version to 1.8.5

* Mon May 23 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7.6-1
- bumped version

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump 

* Wed Feb 16 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- fix release string

* Thu Feb 03 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5.GA
- upstream fixes 

* Tue Feb 01 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4.GA.4
- fixed GA.3 build 

* Tue Feb 01 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4.GA.3
- GA.3 build 
- Updated release version

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4.GA.2
- GA.2 build 

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4.GA.1
- GA.1 build 

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- GA build

* Mon Jan 10 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- Obsoletes abiquo-client

* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- use the new build system
- rename package to abiquo-client-premium

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Wed Oct 27 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-2
- Added ROOT context with redirection to /client-premium

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Upstream 1.6

* Wed May 26 2010 Sergio Rubio srubio@abiquo.com 1.5.1
- Initial Release
