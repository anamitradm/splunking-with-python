
import splunklib.client as client
import utils, sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
if len(sys.argv) != 5:
    print "Syntax: mkuser.py username password role \"real name\""
    sys.exit()
    
try: 
    service = client.connect(**opts.kwargs)
    params ={"realname": sys.argv[4]} 

    user = service.users.create(sys.argv[1], sys.argv[2], sys.argv[3], **params)
    print "User %s created." % user.name

except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
