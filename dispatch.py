
import splunklib.client as client
import utils, sys, time

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
try: 

    if len(sys.argv) == 1:
        print "syntax: dispatch.py [list | run \"name of search\"]"
        sys.exit()
        
    params = {"host"        : opts.kwargs["host"],
              "port"        : opts.kwargs["port"],
              "username"    : opts.kwargs["username"],
              "password"    : opts.kwargs["password"],
              "owner"       : "-",
              "app"         : "-"                
              }
    service = client.connect(**params)

    if sys.argv[1] == "list":
        print "List of all saved searches:"
        for search in service.saved_searches:
           print search.name
    elif sys.argv[1] == "run":
        ss = service.saved_searches[sys.argv[2]]
        print "Running " + ss.name
        job = ss.dispatch() 
	print "Job is running"
	while True:
		sys.stdout.write(".")
		sys.stdout.flush()
		time.sleep(1)
		job.refresh()
		if job.is_done(): 
	        	break    
		job.refresh()
		response = job.results() 
		print response
    else:
        raise Exception("unknown command " + sys.argv[1])
    
except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
