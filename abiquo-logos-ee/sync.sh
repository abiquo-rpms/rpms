rsync -rtlz . root@rpm-builder:/home/rpmbuilder/redhat-logos/
ssh root@rpm-builder "chown rpmbuilder -R /home/rpmbuilder/redhat-logos/"
