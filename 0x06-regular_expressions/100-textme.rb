#!/usr/bin/env ruby
#matches sender, receiver and flags 
#from a message log
my_string = ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/).join(" ")
my_string = my_string.squeeze(' ')
my_list = my_string.split
puts my_list.join(',')
