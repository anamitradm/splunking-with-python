
import splunklib.client as client
import utils
import sys
from pprint import pprint

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
try: 

    if len(sys.argv) == 1:
        print "syntax: users.py [list | username]"
        sys.exit()
        
    service = client.connect(**opts.kwargs)

    if sys.argv[1] == "list":
        print "List of all users:" 
        for user in service.users:
            print " %s " % user.name 
    else:
        u = service.users[sys.argv[1]]
        pprint(u.state)         
      
except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
