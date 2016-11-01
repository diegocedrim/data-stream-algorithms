import stream
import sys


def surprise_number(stream_file):
    occurrences = {}
    for (bow, doc_id) in stream.bow_stream(stream_file):
        sys.stdout.write("\rDocument: %s" % doc_id)
        sys.stdout.flush()
        for word_id in bow:
            occurrences[word_id] = occurrences.get(word_id, 0) + 1
    print ""
    # computing surprise number
    surprise = 0.0
    for appearances in occurrences.values():
        surprise += appearances ** 2
    return surprise
