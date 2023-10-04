#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method
# This regular expression must match a 10 digit phone number
puts ARGV[0].scan(/\S[0-9]{9}/).join