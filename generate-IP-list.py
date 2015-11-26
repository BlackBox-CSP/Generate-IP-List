#!/usr/bin/python

import sys, getopt, pprint, random
from netaddr import *

def main(argv):
	# Parse command line args, exit if doesn't include h,s or n or if number of args is wrong
	try:
		opts, args = getopt.getopt(argv,"hs:n:")
	except getopt.GetoptError:
		print 'generate-IP-list.py -s <subnet> -n <number of hosts>'
		sys.exit(2)
	if len(sys.argv) != 5:
		print 'generate-IP-list.py -s <subnet> -n <number of hosts>'
                sys.exit(2)
	# Set arg variables or display help
	for opt, arg in opts:
		if opt == '-h':
			print 'generate-IP-list.py -s <subnet> -n <number of hosts>'
			print 'Use nmap subnet format 10.10.10.0/24'
			sys.exit()
		elif opt in ("-s"):
			s_net = arg
		elif opt in ("-n"):
			num = arg
	print 'Subnet is', s_net 
	print 'Number of hosts is', num

	# using netaddr functions, calculate subnet size, ensure size is less than num
	ip = IPNetwork(s_net)
	if (int(num) > int(ip.size)):
		print 'The number of hosts %s cannot be greater than the subnet size %s' % (num, ip.size)
		sys.exit(2)
	
	# create list of subnet IPs, randomize list, print out num of them
	ip_list = list(IPNetwork(s_net))
	count = 0
	random.shuffle(ip_list)
	for ip in ip_list:
		if (count < int(num)):
			print '%s' % ip
			count = count + 1

if __name__ == "__main__":
	main(sys.argv[1:])
