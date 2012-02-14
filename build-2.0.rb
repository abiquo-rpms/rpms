#!/usr/bin/env ruby
require 'term/ansicolor'

class String
  include Term::ANSIColor
end

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
  exit 1
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
packages.each do |p|
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
    end
  ensure 
    Dir.chdir pwd
  end
end
