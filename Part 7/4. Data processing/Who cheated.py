import csv 
from datetime import *

def read_files():
    start_dict = {}
    cheaters = []

    with open("start_times.csv") as start_times:
        for line in csv.reader(start_times, delimiter=";"):
            start_name = line[0]
            start_hours, start_minutes = line[1].split(":")
            start_time = time(int(start_hours), int(start_minutes))
            start_dict[start_name] = start_time


    with open("submissions.csv") as submissions:
        for line in csv.reader(submissions, delimiter=";"):
            submission_name = line[0]
            task = line[1]
            points = line[2]
            submission_time = datetime.strptime(line[3], '%H:%M').time()

            if submission_name in start_dict:
                start_time = start_dict[submission_name]
                start_datetime = datetime.combine(datetime.today(), start_time) # Necessary to calculate time limit
                time_limit = start_datetime + timedelta(hours=3)
                if submission_time > time_limit.time():
                    cheaters.append(submission_name)
    
    return cheaters

def cheaters(): # Can be improved
    cheaters = read_files()
    no_duplicates = [] 

    for cheater in cheaters:
        if cheater not in no_duplicates:
            no_duplicates.append(cheater)

    print(no_duplicates)
    
    return no_duplicates

if __name__ == "__main__":
    cheaters()