import time
import csv
import math
from operator import itemgetter

relevance = {}
relevance['Dewalt'] = 8
relevance['Bonyth'] = 7
relevance['Trutacz'] = 6
relevance['Dandy'] = 5
relevance['Terror'] = 4
relevance['Oyaji'] = 4
relevance['Sziky'] = 3
relevance['Koget'] = 3
relevance['Cross'] = 3
relevance['Dragon'] = 2
relevance['Voddy'] = 2
relevance['Stryker'] = 2


def input_parser():
    submissions = []
    filename = input('Enter submission filename in .csv format in /inputdata/: ')
    with open('inputdata/' + filename) as csvfile:
        submission_reader = csv.DictReader(csvfile)
        for row in submission_reader:
            submissions.append(row)

    return submissions

def submission_scorer(submissions):
    max_score = 1

    scores = []

    for submission in submissions:
        rankings = []
        rankings.append(submission['1st'])
        rankings.append(submission['2nd'])
        rankings.append(submission['3rd'])
        rankings.append(submission['4th'])
        rankings.append(submission['5th'])
        rankings.append(submission['6th'])
        rankings.append(submission['7th'])
        rankings.append(submission['8th'])
        rankings.append(submission['9th'])
        rankings.append(submission['10th'])
        rankings.append(submission['11th'])
        rankings.append(submission['12th'])
        submission['score'] = DCG(rankings, relevance)

        if (submission['User'] == 'Final Standings'):
            max_score = submission['score']

        submission['score'] = submission['score'] / max_score

        scores.append({'User' : submission['User'], 'score' : submission['score']})

    return scores
        
def DCG(rankings, relevance):
    score = 0
    for i in range(len(rankings)):
        score = score + relevance[rankings[i]] / (math.log2(i + 2))

    return score

submissions = input_parser()
scores = submission_scorer(submissions)
scores  = sorted(scores, key=itemgetter('score'), reverse=True)
for score in scores:
    print(score)
