%define builtin_release_version 2.0
%define builtin_release_name RC2 
%define real_release_version %{?release_version}%{!?release_version:%{builtin_release_version}}
%define real_release_name %{?release_name}%{!?release_name:%{builtin_release_name}}
%define current_arch %{_arch}

Summary: Abiquo release notes files
Name: abiquo-release-notes-ee
Version: %{real_release_version}
Release: 2 
License: GPL
Group: System Environment/Base
Source: http://mirror.abiquo.com/sources/%{name}-%{builtin_release_version}.tar.gz
Obsoletes: indexhtml abiquo-release-notes
BuildRoot: %{_tmppath}/abiquo-release-notes-root
Provides: indexhtml abiquo-release-notes
BuildArch: noarch

%description
Abiquo release notes files.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}
cp -rf  $RPM_BUILD_DIR/%{name}-%{builtin_release_version}/HTML $RPM_BUILD_ROOT%{_defaultdocdir}/.

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %{current_arch}/R*
%{_defaultdocdir}/HTML

%changelog
* Wed Feb 08 2012 Sergio Rubio <srubio@abiquo.com> - 2.0-2
- RC2 bump

* Wed Dec 21 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- 2.0 version bump

* Fri Jul 08 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- bump version

* Mon Mar 28 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-3
- bumped release
- 1.7.5 GA

* Tue Mar 22 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7.5-2
- bumped release to RC2

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- changed buildarch to noarch

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- Update release notes and release name

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- obsoletes abiquo-release-notes

* Mon Dec 13 2010 Sergio Rubio <rubiojr@frameos.org> - 1.7-1
-  updated to 1.7

* Mon Nov 08 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Build for 1.6.8 Final

* Mon Sep 27 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-2
- Build for 1.6.5 Beta1

* Thu Sep 02 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-1
- Build for 1.6.5 Alpha1
