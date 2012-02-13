Name:     vboxmanage
Version:  3.1.8
Release:  1.abiquo
Summary:  VirtualBox VBoxManage Command
Group:    Development/System 
License:  Multiple 
URL:      http://www.virtualbox.org
Source:   http://mirror.abiquo.com/sources/VirtualBox-%{version}-OSE.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: iasl dev86 libxml2-devel libxslt-devel libIDL-devel hal-devel curl-devel dev86 libcap-devel glibc-devel libstdc++-devel libpng-devel libXmu-devel libX11-devel mesa-libGL-devel libXrandr-devel
Patch1:  no-curl-detect.diff
Source1: VBoxManage

%description
VirtualBox VBoxManage Command

%prep
cd $RPM_BUILD_DIR
rm -rf VirtualBox-%{version}_OSE
tar -xjf $RPM_SOURCE_DIR/VirtualBox-%{version}-OSE.tar.bz2 
if [ $? -ne 0 ]; then
  exit $?
fi
cd VirtualBox-%{version}_OSE
chmod -R a+rX,g-w,o-w .

%patch1 -p1


%build
cd VirtualBox-%{version}_OSE
./configure --disable-python --disable-sdl-ttf --disable-alsa --disable-pulse --disable-dbus --disable-kmods --disable-opengl --disable-hardening --build-headless
source env.sh
kmk all


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -r $RPM_BUILD_DIR/VirtualBox-%{version}_OSE/out/linux.amd64/release/bin $RPM_BUILD_ROOT/opt/vboxmanage
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/VBoxManage

%post
/bin/chmod +x %{_bindir}/VBoxManage
/usr/bin/chcon -t texrel_shlib_t /opt/vboxmanage/*.so /opt/vboxmanage/components/*.so
/bin/chmod 4511 /opt/vboxmanage/VBoxManage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/opt/vboxmanage
%{_bindir}/VBoxManage

%changelog
* Tue Sep 14 2010 Sergio Rubio srubio@abiquo.com 3.1.8-1.abiquo
- Initial Release
