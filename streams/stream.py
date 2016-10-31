def bow_stream(filename):
    """
        Yields dictionaries representing bag of words with the format
        described at https://archive.ics.uci.edu/ml/datasets/Bag+of+Words.
        It simulates a document stream
    """
    with open(filename) as docs:
        # skipping the first 3 lines (D, W, NNZ)
        d = int(next(docs))
        w = int(next(docs))
        next(docs)

        # yields each single different bow vectors found as dicts
        current_doc = 1
        doc_id = None
        bow = {}
        for line in docs:
            doc_id, word_id, count = [int(i) for i in line.split()]

            # if we started to scan a new doc, yields the previous one
            if doc_id != current_doc:
                yield bow, current_doc
                current_doc = doc_id
                bow = {}

            bow[word_id] = count
        yield bow, doc_id


def word_stream(filename):
    """
        Yields the word_id' in a file formatted described at
        https://archive.ics.uci.edu/ml/datasets/Bag+of+Words.
        It simulates a word stream
    """
    with open(filename) as docs:
        # skipping the first 3 lines (D, W, NNZ)
        d = int(next(docs))
        w = int(next(docs))
        next(docs)

        for line in docs:
            doc_id, word_id, count = [int(i) for i in line.split()]
            yield word_id
