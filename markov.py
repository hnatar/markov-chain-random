#!/usr/bin/env python3

import collections
import random
import markovify

class Markov:
    def __init__(self, memory=5):
        self.Next = {'':{}}
        self.memory = memory
    def scan(self, text):
        if text[0] not in self.Next['']:
            self.Next[''][text[0]] = 0
        self.Next[''][text[0]] += 1
        for Len in range(1, self.memory):
            for i in range(0, len(text)):
                end = i + Len
                # (i, i+1, .. i+Len-1) -> i+Len
                if end >= len(text):
                    break
                t = tuple( text[i:end] )
                if t not in self.Next:
                    self.Next[t] = {}
                if text[end] not in self.Next[t]:
                    self.Next[t][text[end]] = 0
                self.Next[t][text[end]] += 1
        for k in self.Next:
            print(k, self.Next[k])
    def markov_get(self, res):
        max_seq = 3
        key = res[-max_seq:]
        for Len in reversed(range(0, max_seq+1)):
            print('Checking for: ', key)
            if key not in self.Next:
                continue
            r = random.random()
            if r <1000:
                word = random.choice(list(self.Next[key].keys()))
                print('choosing big len=', Len, ' -> ', word)
                return word
            res = res[1:]
        return random.choice(list(self.Next[''].keys()))

    def generate(self, size):
        max_seq = 3
        cur = 0
        res = ''
        while len(res) < size:
            key = res[-max_seq:]
            res += self.markov_get(res)
        return res

"""
m = Markov(memory=3)
m.scan('The whale was blue')
print('Generate:')
print(m.generate(10))

"""

with open('LA_addresses.txt', 'r') as f:
    text = f.read()

text_model = markovify.NewlineText(text)
for i in range(5):
    print(text_model.make_sentence())
