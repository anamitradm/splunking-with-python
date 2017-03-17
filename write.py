
import splunklib.client as client
import utils
import sys
import datetime

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
if len(sys.argv) != 3:
    print "Syntax: write.py index \"data\""
    sys.exit()
    
try: 
    service = client.connect(**opts.kwargs)
 
    index = service.indexes[sys.argv[1]]
    timestamp = str(datetime.datetime.now()) 
    index.submit(timestamp + ": " + sys.argv[2], sourcetype="mysourcetype", host="myhost")    
except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
