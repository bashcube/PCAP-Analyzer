import os
import sys

class colors:
	BLUE = '\033[34m'
	STOP = '\033[0m'
	RED = '\033[31m'
	BOLD = '\033[1m'
	
os.system('clear')

print (colors.RED + '    _                _                     ')
print ('   / \   _ __   __ _| |_   _ _______ _ __  ')
print ("  / _ \ | '_ \ / _` | | | | |_  / _ \ '__| ")
print (' / ___ \| | | | (_| | | |_| |/ /  __/ |    ')
print ('/_/   \_\_| |_|\__,_|_|\__, /___\___|_|    ')
print ('                       |___/               ' + colors.STOP)
print 

pcap_file = raw_input(colors.BOLD + "FILE>>>" + colors.STOP)

def top10():
	cmd = 'tshark -T fields -e http.host -r ' + pcap_file + ' | sort | uniq -c | sort -nr | head'
	print (colors.BLUE)
	os.system(cmd)
	print (colors.STOP)
	main()

def user_agent():
	cmd = 'tshark -r ' + pcap_file + ' -Y \'http contains "User-Agent:"\' -T fields -e http.user_agent | sort | uniq -c | sort -nr'
	print (colors.BLUE)
	os.system(cmd)
	print (colors.STOP)
	main()

def connection_details():
	inp = raw_input("Do you wish to continue?{Y/n}" + colors.STOP)
	if inp != 'Y':
		print (colors.BOLD +"RETURNING TO MAIN MENU..." + colors.STOP)
		main()
	cmd1 = 'tshark -o "gui.column.format:\\\"Source\\\",\\\"%us\\\",\\\"src port\\\",\\\"%S\\\",\\\"Protocol\\\",\\\"%p\\\",\\\"Destination\\\",\\\"%ud\\\",\\\"dest port\\\"'
	cmd2 = ',\\\"%D\\\",\\\"Protocol\\\",\\\"%p\\\"" -r '+ pcap_file + ' | column -t'
	print (colors.BLUE)
	os.system(cmd1+cmd2)
	print (colors.STOP)
	main()

def grep():
	string = raw_input(colors.BOLD + "STRING>>>" + colors.STOP)
	cmd = 'tcpdump -r '+ pcap_file +' -A | grep "' + string +'"'
	print (colors.BLUE)
	os.system(cmd)
	print (colors.STOP)
	main()

def ip_list():
	cmd = 'tshark -nr ' + pcap_file + ' -T fields -e ip.src -e ip.dst'
	print (colors.BLUE)
	os.system(cmd)
	print (colors.STOP)
	main()

def port_list():
	cmd = 'tshark -r ' + pcap_file + ' -Y "tcp" -T fields -e tcp.srcport | sort | uniq -c | sort -nr'
	print (colors.BLUE)
	os.system(cmd)
	print (colors.STOP)
	main()

def main():
	print 
	print (colors.BOLD +"1.Top 10 visited websites.\n")
	print ("2.User-Agent.\n")
	print ("3.Connection Details.\n")
	print ("4.Grep String.\n")
	print ("5.List All IP.\n")
	print ("6.List All Ports.\n")
	print ("7.Exit.\n" + colors.STOP)
	choice = int(raw_input(">>>"))
	if choice == 1:
		print (colors.BOLD +"TOP 10 VISITED SITES..." + colors.STOP)
		top10()
	if choice == 2:
		print (colors.BOLD +"USER AGENTS..." + colors.STOP)
		user_agent()
	if choice == 3:
		print (colors.BOLD +"CONNECTION DETAILS..." + colors.STOP)
		connection_details()
	if choice == 4:
		grep()
	if choice == 5:
		print (colors.BOLD +"LISTING ALL IP'S..." + colors.STOP)
		ip_list()
	if choice == 6:
		print (colors.BOLD +"LISTING ALL PORTS..." + colors.STOP)
		port_list()
	if choice == 7:
		print (colors.RED + colors.BOLD +"EXITTING CODE..." + colors.STOP)
		sys.exit()
	else:
		main()

main()
