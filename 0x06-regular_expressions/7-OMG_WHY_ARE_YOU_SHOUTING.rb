#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method
# This regular expression must be only matching: capital letters
puts ARGV[0].scan(/[A-Z]+/).join