# 101636

from datetime import datetime
import streams.distincts_exact as de
import streams.distincts_approximate as da
import math

stream_file = "data/docword.nytimes.txt"

print "Executing the exact method..."
start = datetime.now()
exact_result = de.distinct_words_count(stream_file)
print "\nExact result:", exact_result
print "Exact method execution time:", datetime.now() - start


print "Executing the approximated method..."
start = datetime.now()
countByHashes = da.distinct_words_count(100, stream_file)
print "\nHashes\tResult\tError"
for i in xrange(1, 101):
    result = countByHashes[i]
    error = math.fabs(result - exact_result)
    print "%s\t%d\t%d" % (i, result, error)
print "Approximated method execution time:", datetime.now() - start
