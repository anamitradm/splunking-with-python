import splunklib.client as client
import sys

if len(sys.argv) != 5:
	print "Syntax: login.py username password hostname port"
	sys.exit()
	
uid  = sys.argv[1];
pwd  = sys.argv[2];
host = sys.argv[3];
port = sys.argv[4];

try: 
	service = #LAB: connect and pass the username, password, host and port

	
	print 'Authenticated, token = [%s]' % #LAB: get the service token 

except Exception, err:
	sys.stderr.write('Error: %s\n' % str(err))

