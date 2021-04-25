# BBT-DCG
Normalized Discounted Cumulative Gain implementation for determining accuracy of BBT standings prediction submissions

## Input: 
- CSV table that contains the table header on row 1, and the actual final standings on row 2 with the User ID 'Final Standings'
- E.g. https://docs.google.com/spreadsheets/d/1HPDti0az8uBuhluna8FgDlDUNuzvKJdPbORpHbm4oPU/edit?usp=sharing

## Parameters to tweak: 
Relevance for each place (1st-12th)

Current settings are:
- 1st: 8 points of relevance
- 2nd: 7 points of relevance
- 3rd: 6 points of relevance
- 4th: 5 points of relevance
- 5th: 4 points of relevance
- 6th: 4 points of relevance
- 7th: 3 points of relevance
- 8th: 3 points of relevance
- 9th: 3 points of relevance
- 10th: 2 points of relevance
- 11th: 2 points of relevance
- 12th: 2 points of relevance

## Output: 
Printed list of accuracy scores for each of the submissions ranked from most accurate to least accurate.
