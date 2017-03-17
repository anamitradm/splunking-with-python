
import splunklib.client as client
import utils
import sys

opts = utils.parse(sys.argv[1:], {}, ".splunkrc")
try: 
    if len(sys.argv) == 1:
        print "syntax: inputs.py [list | show inputname | delete inputname | create inputname index]"
        sys.exit()
    service = client.connect(**opts.kwargs)

    if sys.argv[1] == "list":
        for ip in service.inputs:
            print " %s " % ip.name 
    elif sys.argv[1] == "show":
        # need a work-around since service.indexes[path] does not work
        for ip in service.inputs:
            if ip.name == sys.argv[2]:
                for key in sorted(ip.state.keys()):
                    print ' ' +key
                    for sub in ip[key]:
                        print "    %s: %s" % (sub, ip[key][sub])
                break
    elif sys.argv[1] == "create":
        ip = service.inputs.create(sys.argv[2], "monitor", **{"index" : sys.argv[3]})
        print "  created input %s" % ip.name
    elif sys.argv[1] == "delete":
        raise Exception("delete is not currently supported")
        # Indexes.remove() does not work for same reason as given in "list"
    else:
        raise Exception("unknown command \"%s\"" % sys.argv[1])

except Exception, err:
    sys.stderr.write('Error: %s\n' % str(err))
