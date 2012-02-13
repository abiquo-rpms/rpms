%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname abiquo-etk
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Abiquo Elite Toolkit
Name: rubygem-%{gemname}
Version: 0.5.8
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/rubiojr/abiquo-etk
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(nokogiri) >= 1.3
Requires: rubygem(term-ansicolor) >= 1.0
Requires: rubygem(iniparse) >= 1.1.4
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Tools to troubleshoot your Abiquo installation


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/abicli
%{_bindir}/ciab-setup
%{_bindir}/abiquo-check-16-install
%{_bindir}/abiquo-check-install
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/TODO
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Feb 09 2012 Sergio Rubio <srubio@abiquo.com> - 0.5.8-1
- upstream update

* Wed Jul 13 2011 Sergio Rubio <srubio@abiquo.com> - 0.5.7-1
- bumped release

* Thu Jun 16 2011 Sergio Rubio <rubiojr@frameos.org> - 0.5.6-1
- updated to 0.5.6

* Thu May 26 2011 Sergio Rubio <srubio@abiquo.com> - 0.5.5-1
- updated to 0.5.5

* Wed Apr 20 2011 Sergio Rubio <srubio@abiquo.com> - 0.5.4-1
- bumped version

* Wed Apr 20 2011 Sergio Rubio <srubio@abiquo.com> - 0.5.3-1
- bumped version

* Mon Mar 23 2011 Sergio Rubio <srubio@abiquo.com> - 0.5.2-1
- upstream update

* Mon Mar 21 2011 Sergio Rubio <srubio@abiquo.com> - 0.5.1-1
- upstream update

* Mon Mar 21 2011 Sergio Rubio <srubio@abiquo.com> - 0.5-1
- upstream update

* Fri Jan 28 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.41-1
- upstream update

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.40-1
- upstream update

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.39-1
- upstream update

* Thu Jan 20 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.38-1
- upstream update

* Wed Jan 19 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.37-2
- add rubygem-iniparse require

* Tue Jan 18 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.37-1
- updated to upstream version 

* Tue Jan 18 2011 Sergio Rubio <srubio@abiquo.com> - 0.4.36-1
- updated to upstream version 

* Wed Dec 15 2010 Sergio Rubio <srubio@abiquo.com> - 0.4.35-3
- rebuilt

* Wed Dec 15 2010 Sergio Rubio <srubio@abiquo.com> - 0.4.35-2
- package renamed to rubygem-abiquo-etk 

* Tue Nov 09 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.34-1
- Updated to upstream 0.4.35-1

* Tue Nov 09 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.34-1
- Updated to upstream 0.4.34-1

* Thu Nov 04 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.33-1
- Updated to upstream 0.4.33-1

* Tue Nov 03 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.32-1
- Updated to upstream 0.4.32-1

* Tue Nov 02 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.31-1
- Updated to upstream 0.4.31

* Tue Nov 02 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.30-1
- Updated to upstream 0.4.30

* Tue Nov 02 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.29-1
- Updated to upstream 0.4.29

* Fri Oct 29 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.28-1
- Updated to upstream 0.4.28

* Thu Oct 28 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.27-1
- Updated to upstream 0.4.27

* Thu Oct 25 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.22-1
- Updated to upstream 0.4.22

* Thu Oct 21 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.20-1
- Updated to upstream 0.4.20

* Wed Oct 20 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.14-1
- Updated to upstream 0.4.14

* Wed Oct 20 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.13-1
- Updated to upstream 0.4.13

* Wed Oct 20 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.12-1
- Updated to upstream 0.4.12

* Thu Oct 07 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.9-1
- Updated to upstream 0.4.9

* Thu Oct 07 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.8-1
- Updated to upstream 0.4.8

* Fri Oct 01 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.7-1
- Updated to upstream 0.4.7

* Fri Oct 01 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.6-1
- Updated to upstream 0.4.6

* Fri Oct 01 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.5-1
- Updated to upstream 0.4.5

* Tue Sep 28 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.3-1
- Updated to upstream 0.4.3

* Mon Sep 27 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.2-1
- Updated to upstream 0.4.2

* Mon Sep 27 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4.1-1
- Updated to upstream 0.4.1

* Mon Sep 27 2010 : Sergio Rubio <srubio@abiquo.com> - 0.4-1
- Updated to upstream 0.4

* Thu Sep 23 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.11-1
- Updated to upstream 0.3.11

* Thu Sep 23 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.10-1
- Updated to upstream 0.3.10

* Thu Sep 23 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.9-1
- Updated to upstream 0.3.9

* Wed Sep 22 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.8-1
- Updated to upstream 0.3.8

* Tue Sep 21 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.7-1
- Updated to upstream 0.3.7

* Thu Sep 16 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.6-1
- Updated to upstream 0.3.6

* Tue Sep 07 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.5-1
- Updated to upstream 0.3.5

* Tue Sep 07 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.4-1
- Updated to upstream 0.3.4

* Mon Sep 06 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.3-1
- Updated to upstream 0.3.3

* Mon Aug 30 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.2-1
- Updated to upstream 0.3.2
* Mon Aug 30 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3.1-1
- Updated to upstream 0.3.1
* Mon Aug 30 2010 : Sergio Rubio <srubio@abiquo.com> - 0.3-1
- Initial package
