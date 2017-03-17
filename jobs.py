
import splunklib.client as client
import utils, sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
try: 
    if len(sys.argv) == 1:
        print "syntax: jobs.py [list | show jobid | results jobid | delete jobid]"
        sys.exit()
    
    service = client.connect(**opts.kwargs)

    if sys.argv[1] == "list":
        for job in service.jobs:
            print 'Job id : %s' % job.sid
            print 'Original Search Request : %s' % job.eventSearch
        
    elif sys.argv[1] == "show":
        job = service.jobs[sys.argv[2]]
        for key in sorted(job.state.keys()):
            print ' ' +key
            for sub in job[key]:
                print "    %s: %s" % (sub, job[key][sub])
  
    elif sys.argv[1] == "results":
        job = service.jobs[sys.argv[2]] 
        if not job.is_done():
            raise Exception("Job not complete")
        response = job.results() 
        print response
        
    elif sys.argv[1] == "delete":
        job = service.jobs[sys.argv[2]] 
        job.delete() 
        print "  job %s deleted" % job.sid
 
    else:
        raise Exception("unknown command \"%s\"" % sys.argv[1])

except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
