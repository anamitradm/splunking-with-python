
import splunklib.client as client
import utils
import sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
if len(sys.argv) != 2:
    print "Syntax: export.py \"search query\""
    sys.exit()
    
try: 
    service = client.connect(**opts.kwargs)
    response = service.jobs.export(sys.argv[1])
    print response

except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
