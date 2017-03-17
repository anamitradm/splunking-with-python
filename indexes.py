
import splunklib.client as client
import utils
import sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
try: 
    if len(sys.argv) == 1:
        print "syntax: indexes.py [list | show indexname | clean indexname | delete indexname | create indexname]"
        sys.exit()
    service = client.connect(**opts.kwargs)

    if sys.argv[1] == "list":
        for index in service.indexes:
          print " %s" % index.name 
    elif sys.argv[1] == "show":
        index = service.indexes[sys.argv[2]]
        for key in sorted(index.state.keys()):
            print ' ' + key
            for sub in index[key]:
                print "    %s: %s" % (sub, index[key][sub])
    elif sys.argv[1] == "create":
        index = service.indexes.create(sys.argv[2])
        print "  created index %s" % index.name
    elif sys.argv[1] == "clean":
        index = service.indexes[sys.argv[2]]
        index.clean() 
        print "  cleaned index %s" % index.name
    elif sys.argv[1] == "delete":
        index = service.indexes[sys.argv[2]] 
        index.delete() 
        print "  index %s deleted" % sys.argv[2]
    else:
        raise Exception("unknown command \"%s\"" % sys.argv[1])

except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
