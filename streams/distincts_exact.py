import stream
import sys
from memory_profiler import profile


@profile
def distinct_words_count(stream_file):
    words = set()
    for (bow, doc_id) in stream.bow_stream(stream_file):
        sys.stdout.write("\rDocument: %s" % doc_id)
        sys.stdout.flush()
        for word_id in bow:
            words.add(word_id)
    return len(words)
