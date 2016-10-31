from sympy.ntheory import isprime
from random import randint
import stream
import numpy as np
from memory_profiler import profile
import sys


def calculate_M(initial=10266000):
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


@profile
def distinct_words_count(n_hashes, stream_file):
    M = calculate_M()
    min_values = compute_min_values(n_hashes, M, stream_file)
    estimated_count = [M/i for i in min_values]
    count_by_nhashes = {}
    for i in xrange(1, n_hashes + 1):
        e = estimated_count[:i]
        count_by_nhashes[i] = median(e)
    return count_by_nhashes