%define abiquo_basedir /opt/abiquo

Name:     abiquo-pocsetup
Version:  2.0
Release:  1%{?dist}%{?buildstamp}
Summary:  Abiquo POC Setup Metapackage
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  README 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: dhcp nfs-utils samba abiquo-server abiquo-remote-services abiquo-v2v abiquo-api 
Obsoletes: abiquo-16-pocsetup
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package installs Abiquo PoC Environment.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d
cp ../SOURCES/README $RPM_BUILD_ROOT/%{_docdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Add dhcpd conf
cp /etc/dhcpd.conf /etc/dhcpd.conf.bak
cat > /etc/dhcpd.conf <<EOF
ddns-update-style interim;

omapi-port 7911;
option classless-static-routes code 121 = array of integer 8;
option ms-classless-static-routes code 249 = array of integer 8;

subnet 0.0.0.0 netmask 0.0.0.0 {
	default-lease-time 60000;
	max-lease-time 720000;
	option subnet-mask 255.255.255.0;
	option domain-name-servers 8.8.8.8;
}

EOF

#  Add samba conf
cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
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

cp /etc/exports /etc/exports.bak
cat > /etc/exports <<EOF
/opt/vm_repository *(rw,no_root_squash,subtree_check,insecure)
EOF

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/README

%changelog
* Mon Dec 19 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- bumped version to 2.0
- Added new dhcpd.conf options
- Remove abiquo-cloud-node dep

* Mon May 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump
- backup system config files before overwriting them
- set buildarch to noarch

* Tue Jan 25 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- remove create-vlans script

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5
- obsoletes abiquo-16-pocsetup

* Wed Jan 19 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- tuned create-vlans script

* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- removed cloud-in-a-box.sql

* Tue Dec 14 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- renamed to abiquo-pocsetup

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Wed Nov 03 2010 Sergio Rubio srubio@abiquo.com 1.6.8-12
- updated cloud-in-a-box.sql

* Wed Nov 03 2010 Sergio Rubio srubio@abiquo.com 1.6.8-11
- updated cloud-in-a-box.sql

* Thu Oct 27 2010 Sergio Rubio srubio@abiquo.com 1.6.8-10
- updated create-vlans script

* Thu Oct 27 2010 Sergio Rubio srubio@abiquo.com 1.6.8-9
- updated cloud-in-a-box.sql

* Thu Oct 27 2010 Sergio Rubio srubio@abiquo.com 1.6.8-8
- include create-vlans script

* Thu Oct 27 2010 Sergio Rubio srubio@abiquo.com 1.6.8-7
- changed default port to 80 in schema

* Wed Oct 27 2010 Sergio Rubio srubio@abiquo.com 1.6.8-6
- updated cloud-in-a-box schema

* Fri Oct 25 2010 Sergio Rubio srubio@abiquo.com 1.6.8-5
- depend on abiquo-cloud-node

* Fri Oct 15 2010 Sergio Rubio srubio@abiquo.com 1.6.8-4
- updated SQL schema

* Thu Oct 07 2010 Sergio Rubio srubio@abiquo.com 1.6.8-3
- updated SQL schema

* Thu Oct 07 2010 Sergio Rubio srubio@abiquo.com 1.6.8-2
- added sql schema for the cloud in a box

* Wed Oct 06 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.8

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Wed Jul 21 2010 Sergio Rubio srubio@abiquo.com 1.6-3
- configure dhcp, samba and nfs exports in %post

* Wed Jul 21 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- depend on abiquo-api

* Tue Jul 20 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Initial release
