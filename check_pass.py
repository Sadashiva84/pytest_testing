import csv
import os
import pandas as pd


def execute():
    print("Automating...")
    os.system('git add .')
    print("Added files to branch")
    os.system('git commit -m "Automated Push after test"')
    print("Commited files")
    os.system('git push origin testing:deployment')
    print("Pushed code to deployment branch")

word = 'passed'

found = False
def check():
    dataset = pd.read_csv('sqrt.csv')
    for i in range(len(dataset)):
        if(dataset.loc[i][6] == 'failed'):
            found = True
    return found


if found != 'False': 
        print("Passed")
        execute()
else:
        print("Failed")
        




