# Requirements

* Ruby 
* Rubygems

And the following gems installed:

* pkg-wizard
* thor
* term-ansicolor

# Installing the requirements in Ubuntu

Install required packages:

    sudo apt-get install rubygems ruby1.9.3 rpm curl

Update alternatives to choose ruby 1.9.3:

    update-alternatives --config ruby

Update alternatives to choose rubygems for ruby 1.9.3

    update-alternatives --config gem

# Add the following rpm macro to $HOME/.rpmmacros

    echo "%abiquo_binaries_url http://hudson/%{getenv:ABI_BRANCH}/premium/" >> ~/.rpmmacros

# Using the build script

Building all the packages from master branch:

    ABI_BRANCH=master ./builder build

Buildding selected packages from master branch:

    ABI_BRANCH=master ./builder build --selected abiquo-v2v,abiquo-aim


# Related

PKG Wizard

[http://pkg-wizard.frameos.org/]

Mock

[https://fedoraproject.org/wiki/Projects/Mock]



