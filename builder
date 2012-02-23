#!/usr/bin/env ruby
require 'rubygems'
require 'term/ansicolor'
require 'thor'

ENV['LANG'] = 'en_US.UTF-8'

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

  desc "clean_buildbot", "Clean remote buildbot"
  method_options :host => :string, :port => :string
  def clean_buildbot
    host = options[:host] || 'builder6'
    port = options[:port] || 4567
    puts "Cleaning remote buildbot #{host}:#{port}"
    `curl --silent -X POST http://#{host}:4567/job/clean `
  end

  desc "tag_build", "Tag current buildbot packages"
  method_options :host => :string, :port => :string, :tag => :string
  def tag_build
    host = options[:host] || 'builder6'
    port = options[:port] || 4567
    tag = options[:tag]
    if tag and not tag.strip.chomp.empty?
      tag = tag.gsub(/\s/, '_')
      puts "Tagging current buildbot packages at #{host}:#{port} with tag #{tag}"
      `curl --silent -X POST http://#{host}:4567/tag/#{tag}`
    else
      $stderr.puts "Invalid tag"
    end
  end
end

class String
  include Term::ANSIColor
end

def main(selected=nil)
  packages = %w{
    abiquo-v2v
    abiquo-virtualfactory
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
      puts ">> Skipping package #{p}".yellow
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
    puts "\n\nThe following packages failed to build:\n\n"
    failed_packages.each do |p|
      puts p.bold.red
    end
  end
end

CLI.start

