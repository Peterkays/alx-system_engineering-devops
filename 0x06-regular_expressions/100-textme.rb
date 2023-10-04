#!/usr/bin/env ruby
# This script should output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/[A-Z\s]+/).join