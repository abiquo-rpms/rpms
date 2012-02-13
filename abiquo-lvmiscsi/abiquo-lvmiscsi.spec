%define abiquo_basedir /opt/abiquo/lvmiscsi

Name:           abiquo-lvmiscsi
Version:        2.0
Release:        1%{?dist}%{?buildstamp}
Url:            http://www.abiquo.com/
License:        Multiple
Group:          Development/Tools
Summary:        Abiquo LVM iSCSI Storage plugin
Source0:        http://mirror.abiquo.com/sources/%{name}-tomcat-%{version}.tar.gz
Source1:        %{?abiquo_binaries_url}lvmiscsi.war
Source2:        server.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:	scsi-target-utils
BuildRequires:  /usr/bin/unzip
BuildArch:	noarch

%description
Abiquo is the Next Generation Cloud Management Solution

This package includes lvmiscsi storage plugin.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n abiquo-lvmiscsi-tomcat-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
cp -r tomcat $RPM_BUILD_ROOT/%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT
install -m 755 abiquo-lvmiscsi.init $RPM_BUILD_ROOT/%{_initrddir}/abiquo-lvmiscsi
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/conf/
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT/ %{SOURCE1}


%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add abiquo-lvmiscsi

%preun
/sbin/chkconfig --del abiquo-lvmiscsi

%files
%{abiquo_basedir}/tomcat/bin
%{abiquo_basedir}/tomcat/lib
%{abiquo_basedir}/tomcat/logs
%{abiquo_basedir}/tomcat/temp
%{abiquo_basedir}/tomcat/LICENSE
%{abiquo_basedir}/tomcat/RUNNING.txt
%{abiquo_basedir}/tomcat/NOTICE
%{abiquo_basedir}/tomcat/RELEASE-NOTES
%{abiquo_basedir}/tomcat/webapps
%{abiquo_basedir}/tomcat/work
%{_docdir}/%{name}
%config(noreplace) %{abiquo_basedir}/tomcat/conf/*
%{_initrddir}/abiquo-lvmiscsi

%changelog
* Wed Dec 21 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- 2.0 version bump
- Updated tomcat
- Add custom server.xml

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump

* Mon Feb 21 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7-8
- set buildarch to noarch

* Wed Feb 16 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-7
- fix release string

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- GA build

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5
- upstream update

* Tue Jan 25 2011 Sergio Rubio <srubio@abiquo.com> 1.7-4
- upstream update

* Wed Jan 19 2011 Sergio Rubio <srubio@abiquo.com> 1.7-3
- package changes

* Fri Jan 14 2011 Sergio Rubio <srubio@abiquo.com> 1.7.0-2
- Updated to upstream 1.7

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Thu Oct 14 2010 Sergio Rubio <srubio@abiquo.com> 1.6-5.abiquo
- updated lvmiscsi lib

* Thu Oct 08 2010 Sergio Rubio <srubio@abiquo.com> 1.6-4.abiquo
- updated init script

* Thu Oct 07 2010 Sergio Rubio <srubio@abiquo.com> 1.6-3.abiquo
- updated init script

* Thu Oct 07 2010 Sergio Rubio <srubio@abiquo.com> 1.6-2.abiquo
- changed install dir

* Fri Jun 18 2010 Salvador Gironès <salvador.girones@abiquo.com> 1.6-1abiquo
- Initial release
