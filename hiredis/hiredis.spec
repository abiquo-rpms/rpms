Summary: hiredis
Name: hiredis
Version: 0.9.2
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://github.com/antirez/hiredis
Source0: http://mirror.abiquo.com/sources/hiredis-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make
Provides: hiredis

%description
Minimalistic C client for Redis 

%prep
%setup

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
%{__install} -Dp -m 0755 libhiredis.so %{buildroot}%{_libdir}/libhiredis.so
%{__install} -Dp -m 0755 hiredis.h %{buildroot}%{_includedir}/hiredis/hiredis.h
%{__install} -Dp -m 0755 sds.h %{buildroot}%{_includedir}/hiredis/sds.h

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/
%{_includedir}/

%changelog
* Wed Dec 22 2010 Sergio Rubio <srubio@abiquo.com> - 0.9.2-1
- updated to upstream 0.9.2

* Fri Dec 10 2010 Sergio Rubio <srubio@abiquo.com> - 0.9.1-1
- updated to hiredis 0.9.1

* Tue Oct 05 2010 - Sergio Rubio <srubio@abiquo.com> 0.0.20101005
- Initial release

