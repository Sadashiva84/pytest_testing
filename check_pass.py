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

def check():
    pass_counter = 0
    dataset = pd.read_csv('sqrt.csv')
    for i in range(len(dataset)):
        if(dataset.loc[i][6] == 'failed'):
            print("Can't commit, code doesn't clear test")
            break
        elif dataset.loc[i][6] == 'passed':
            pass_counter+=1
            if pass_counter == len(dataset):
                execute()
check()





