# Requirements

* Ruby 1.9
* Rubygems

And the following gems installed:

* pkg-wizard
* thor
* term-ansicolor

# Installing the requirements in Ubuntu

Install the ruby stack:

    sudo apt-get install rubygems ruby1.9.3

Update alternatives to choose ruby 1.9.3

    update-alternatives --config ruby

Update alternatives to choose rubygems for ruby 1.9.3

    update-alternatives --config gem

# Using the build script

Building all the packages from master branch:

    ABI_BRANCH=master ./builder build

Buildding selected packages from master branch:

    ABI_BRANCH=master ./builder build --selected abiquo-v2v,abiquo-aim

