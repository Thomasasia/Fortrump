#!/usr/bin/env python
import csv, random

with open('tweets.csv', 'r') as csvfile:
    tweets = csv.reader(csvfile)
    rows = []
    for row in tweets:
        rows.append(row)
    rand_index = random.randint(0,len(rows))
    print(rows[rand_index][0])
