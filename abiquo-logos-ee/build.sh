CHROOT=centos-5.5-x86_64
CHROOT_DIR=/var/lib/mock/$CHROOT/root
MOCK_CMD="/usr/bin/mock --disable-plugin ccache"

rm -rf tmp rpms
mkdir tmp
mkdir -p rpms/SRPMS

$MOCK_CMD --init -r  $CHROOT
$MOCK_CMD -r $CHROOT --copyin *.tar.bz2 /builddir/build/SOURCES/
$MOCK_CMD -r $CHROOT --copyin *.png /builddir/build/SOURCES/
$MOCK_CMD -r $CHROOT --copyin *.patch /builddir/build/SOURCES/
$MOCK_CMD -r $CHROOT --copyin redhat-logos.spec /root
$MOCK_CMD -r $CHROOT --shell 'rpmbuild -ba /root/redhat-logos.spec'

cp $CHROOT_DIR/builddir/build/RPMS/*.rpm rpms
cp $CHROOT_DIR/builddir/build/SRPMS/*.rpm rpms/SRPMS/
rm -rf tmp
