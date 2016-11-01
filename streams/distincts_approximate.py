from sympy.ntheory import isprime
from random import randint
import stream
import numpy as np
import sys


def calculate_M(initial):
    m = initial
    while not isprime(m):
        m += 1
    return m


def generate_hashes(number, M):
    hashes = []
    for i in xrange(number):
        ra = randint(0, M - 1)
        rb = randint(0, M - 1)
        h = lambda x, a=ra, b=rb: (a*x + b) % M
        hashes.append(h)
    return hashes


def compute_min_values(n_hashes, M, stream_file):
    hashes = generate_hashes(n_hashes, M)
    min_values = [float("inf")] * n_hashes
    for (bow, doc_id) in stream.bow_stream(stream_file):
        sys.stdout.write("\rDocument: %s" % doc_id)
        sys.stdout.flush()
        for word_id in bow:
            for i in xrange(n_hashes):
                h = hashes[i]
                min_values[i] = min(min_values[i], h(word_id))
    return min_values


def median(lst):
    return np.median(np.array(lst))


def distinct_words_count(n_hashes, stream_file, universe_set_size=10266000):
    M = calculate_M(universe_set_size)
    min_values = compute_min_values(n_hashes, M, stream_file)
    print "Min Values:", min_values
    estimated_count = [M/i for i in min_values if i != 0]
    count_by_nhashes = {}
    for i in xrange(1, n_hashes + 1):
        e = estimated_count[:i]
        count_by_nhashes[i] = median(e)
    return count_by_nhashes
