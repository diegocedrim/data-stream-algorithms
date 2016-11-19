from datetime import datetime
from streams.surprise_ams import AmsAlgorithm
import streams.surprise_exact as se
from optparse import OptionParser


usage = "usage: %prog [options] arg1"
parser = OptionParser(usage=usage)
parser.add_option("-e", "--exact",
                  action="store_true", dest="exact", default=False,
                  help="Execute the exact method for computing the surprise number")
parser.add_option("-n", type="int", dest="num_variables",
                  help="Number of variables to compute the AMS method")
(options, args) = parser.parse_args()

stream_file = "data/Norvig.txt"
print "... Surprise Number ..."

if options.exact:
    print "Method: Exact"
    start = datetime.now()
    exact_result = se.surprise_number(stream_file)
    print "Exact result:", exact_result
    print "Execution time (s):", (datetime.now() - start).seconds
else:
    print "Method: AMS"
    print "Variables:", options.num_variables
    start = datetime.now()
    ams = AmsAlgorithm(options.num_variables, stream_file)
    ams.start_stream()
    result = ams.surprise_number()
    print "AMS result:", result
    print "Execution time (s):", (datetime.now() - start).seconds
