import array

T = [[0,314,263,595,387],[1,124,252,282,291],[2,19,252,122,278],[3,197,182,307,191],[4,299,178,377,191],[5,534,170,638,209],[6,305,147,368,159],[7,442,135,540,157]]
import csv
with open('tag1.csv', 'w', newline='') as f:
    tw = csv.writer(f)
    tw.writerows(T)