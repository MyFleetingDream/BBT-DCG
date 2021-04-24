import time
import csv
import math
from operator import itemgetter


def input_parser():
    submissions = []
    filename = input('Enter submission filename in .csv format in /inputdata/: ')
    with open('inputdata/' + filename) as csvfile:
        submission_reader = csv.DictReader(csvfile)
        for row in submission_reader:
            submissions.append(row)

    return submissions

def submission_scorer(submissions):
    for submission in submissions:
        submission['score'] = DCG(rankings, relevance)

    return submissions
        

