import stream
import sys


def surprise_number(stream_file):
    occurrences = {}
    for (word, count) in stream.alphanumeric_word_stream(stream_file):
        # progress = float(count)/17518432
        # sys.stdout.write("\rProcessing: %.2f " % progress)
        # sys.stdout.flush()
        occurrences[word] = occurrences.get(word, 0) + 1
    # print ""
    # computing surprise number
    surprise = 0.0
    for appearances in occurrences.values():
        surprise += appearances ** 2
    return surprise
