from datetime import datetime
from streams.surprise_ams import AmsAlgorithm
import streams.surprise_exact as se


stream_file = "data/docword.nytimes.txt"
print "... Surprise Number ..."
print "Executing the exact method..."
start = datetime.now()
exact_result = se.surprise_number(stream_file)
print "Exact result:", exact_result
print "Exact method execution time:", datetime.now() - start

print "Executing the AMS method..."
start = datetime.now()
ams = AmsAlgorithm(100, stream_file)
ams.start_stream()
result = ams.surprise_number()
print "AMS result:", result
print "Exact method execution time:", datetime.now() - start
