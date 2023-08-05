import csv
import os


def execute():
    print("Automating...")
    os.system('git add .')
    print("Added files to branch")
    os.system('git commit -m "Automated Push after test"')
    print("Commited files")
    os.system('git push origin testing:deployment')
    print("Pushed code to deployment branch")

word = 'passed'
with open ("sqrt.csv", mode = 'r') as file:
    pass_check = csv.reader(file)
    for i in pass_check: 
        if word == 'passed':
            print("Executing")
            execute()
            break




