#!/usr/bin/env ruby
require 'term/ansicolor'
require 'thor'

class CLI < Thor

  desc "build", "Build the packages (all the packages by default)"
  method_options :selected => :string
  def build
    selected = options[:selected] 
    if selected
      selected = selected.split(",")
    else
      selected = []
    end
    main selected
  end
end

class String
  include Term::ANSIColor
end

def main(selected=nil)
  packages = %w{
    abiquo-v2v
    abiquo-tarantino
    abiquo-ssm
    abiquo-server
    abiquo-remote-services
    abiquo-dhcp-relay
    abiquo-pocsetup
    abiquo-nodecollector
    abiquo-lvmiscsi
    abiquo-core
    abiquo-cloud-node
    abiquo-client-premium
    abiquo-api
    abiquo-am
    abiquo-aim
    abiquo-release-ee
    abiquo-release-notes-ee
    abiquo-vsm
    rubygem-abiquo-etk
    abiquo-logos-ee
  }

  build_host = 'builder6' 
  binaries_url = `rpm --eval "%{abiquo_binaries_url}"`

  if ENV['ABI_BRANCH'].nil? 
    $stderr.puts "ABI_BRANCH env var not defined. Aborting."
    return 1
  end

  puts 
  puts "Build Host:    #{build_host}"
  puts "Binaries URL:  #{binaries_url}"
  puts

  def perror(cmd)
    out = `#{cmd} 2>&1`
    res = $?.exitstatus
    $stderr.puts out unless res.eql? 0
    res
  end

  pwd = Dir.pwd
  failed_packages = []
  packages.each do |p|
    if (not selected.empty? and not selected.include?(p))
      puts "Skipping package #{p}"
      next
    end
    puts "Building #{p}... ".bold
    begin
      Dir.chdir p
      puts "** Fetching sources"
      res1 = perror "spectool -f -g -S #{p}.spec"
      puts "** Sending package to remote build host #{build_host}"
      res2 = perror "pkgwiz remote-build -b #{build_host} -m abiquo-1.7"
      if (res1 == 0) and (res2 == 0)
        puts "** OK".green.bold
      else
        puts "** Failed".red.bold
        failed_packages << p
      end
    ensure 
      Dir.chdir pwd
    end
  end

  if !failed_packages.empty?
    puts "The following packages failed to build:\n\n"
    failed_packages.each do |p|
      puts p.bold.red
    end
  end
end

CLI.start

