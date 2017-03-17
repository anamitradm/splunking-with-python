
import splunklib.client as client
import utils
import sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
if len(sys.argv) != 3:
    print "Syntax: formats.py \"search query\" output_mode"
    sys.exit()
    
try: 
    service = client.connect(**opts.kwargs)
    response = service.jobs.oneshot(sys.argv[1], **{"output_mode" : sys.argv[2]}) 
    print response

except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
