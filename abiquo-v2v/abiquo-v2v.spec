%define abiquo_basedir /opt/abiquo

Name:     abiquo-v2v
Version:  2.0
Release:  3%{?dist}%{?buildstamp}
Summary:  Abiquo V2V Conversion Component 
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{?abiquo_binaries_url}bpm-async.war
Source1:  %{?abiquo_binaries_url}v2v-diskmanager
Source2:  %{?abiquo_binaries_url}mechadora
Source3:  abiquo.properties.v2v
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core vboxmanage iscsi-initiator-utils nfs-utils samba qemu-img
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the enterprise V2V conversion component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/scripts
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/bpm-async/ %{SOURCE0}
cp  %{SOURCE1} $RPM_BUILD_ROOT/%{abiquo_basedir}/scripts
cp  %{SOURCE2} $RPM_BUILD_ROOT/%{abiquo_basedir}/scripts
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/bin/
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/bin/
cp %{SOURCE3} $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/

%clean
rm -rf $RPM_BUILD_ROOT

%post
cp /etc/samba/smb.conf /etc/samba/smb.conf.rpmsave

cat > /etc/samba/smb.conf <<EOF

[global]
workgroup = WORKGROUP
server string = %h server
dns proxy = no
log file = /var/log/samba/log.%m
max log size = 1000
syslog = 0
panic action = /usr/share/samba/panic-action %d
security = share
guest account = root
encrypt passwords = true
passdb backend = tdbsam
obey pam restrictions = yes
unix password sync = yes
passwd program = /usr/bin/passwd %u
passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
pam password change = yes

[vm_repository]
path = /opt/vm_repository
guest ok = yes
read only = false
locking = yes

EOF

%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/bpm-async
%{abiquo_basedir}/scripts
/usr/bin/mechadora
/usr/bin/v2v-diskmanager
%{abiquo_basedir}/config/examples/abiquo.properties.v2v


%changelog
* Thu Feb 02 2012 Sergio Rubio <srubio@abiquo.com> - 2.0-3
- Added qemu-img dependency

* Tue Jan 31 2012 Sergio Rubio <srubio@abiquo.com> - 2.0-2
- updated mechadora and v2v-diskmanager sources

* Mon Dec 19 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- bumped version to 2.0
- added v2v sample properties file

* Fri Oct 07 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-2
- updated v2v-diskmanager script

* Fri Sep 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-1
- bumped version to 1.8.5

* Wed Jun 15 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8-2
- updated mechadora

* Mon May 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Apr 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.6-1
- bumped version

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump
- v2v-diskmanager updated

* Mon Feb 28 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7-8
- set buildarch to noarch

* Wed Feb 16 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-7
- fix release string

* Thu Feb 03 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6.GA
- upstream fixes

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5.GA
- GA build

* Mon Jan 10 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- depend on samba and nfs-utils
- override default smb.conf

* Mon Jan 10 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- use WAR as Source0

* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- updated build system

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Thu Sep 16 2010 Sergio Rubio srubio@abiquo.com 1.6.5-2
- replace VirtualBox dep with vboxmanage

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Wed Jul 21 2010 Sergio Rubio srubio@abiquo.com 1.6-3
- Add mechadora and v2v-diskmanager scripts to /usr/bin
- Remove init script

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Wed May 26 2010 Sergio Rubio srubio@abiquo.com 1.5.1
- Initial Release
