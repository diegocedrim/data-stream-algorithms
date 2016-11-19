"""
Cumputes the surprise number using the AMS method

The description of the implemented algorithm can be found at
http://infolab.stanford.edu/~ullman/mmds/ch4.pdf starting from Section 4.5.1
"""

import stream
import sys
import random


class AmsAlgorithm:

    def __init__(self, n_variables, stream_file):
        self.stream_file = stream_file
        self.n_variables = n_variables
        self.variables = {}
        self.n = 0  # the current stream size

    def start_stream(self):
        self.n = 0
        for (word, count) in stream.alphanumeric_word_stream(self.stream_file):
            if word in self.variables:
                self.variables[word] += 1
            else:
                self.__create_new_variable(word)
            self.n += 1

    def surprise_number(self):
        sum_values = 0.0
        for word in self.variables:
            sum_values += self.n * (2*self.variables[word] - 1)  # Section 4.5.2
        return sum_values/len(self.variables)

    def __create_new_variable(self, word):
        if len(self.variables) < self.n_variables:
            self.variables[word] = 1
            return

        threshold = float(self.n_variables)/(self.n + 1)
        should_create = random.random() <= threshold  # Section 4.5.5
        if should_create:
            to_remove = random.choice(self.variables.keys())
            del self.variables[to_remove]
            self.variables[word] = 1