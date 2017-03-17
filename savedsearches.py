
import splunklib.client as client
import utils
import sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
try: 

    if len(sys.argv) == 1:
        print "syntax: savedsearches.py [list owner app | \"search name\"]"
        sys.exit()
        
    if sys.argv[1] == "list":
        params = {"host"        : opts.kwargs["host"],
                  "port"        : opts.kwargs["port"],
                  "username"    : opts.kwargs["username"],
                  "password"    : opts.kwargs["password"],
                  "owner"       : sys.argv[2],
                  "app"         : sys.argv[3]
                  }
        service = client.connect(**params)
        print 'saved searches in %s/%s namespace:' % (service.namespace.owner, service.namespace.app)
        for s in service.saved_searches: 
            print '  %s (%s/%s)' % (s.name, s.access.owner, s.access.app)
 
    else:
        params = {"host"        : opts.kwargs["host"],
                  "port"        : opts.kwargs["port"],
                  "username"    : opts.kwargs["username"],
                  "password"    : opts.kwargs["password"],
                  "owner"       : "-",
                  "app"         : "-"
                  }
        service = client.connect(**params)
        search =  service.saved_searches[sys.argv[1]]
        for key in sorted(search.state.keys()):
            print ' ' + key
            for sub in search[key]:
                  print "    %s: %s" % (sub, search[key][sub])
                    
      
except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
