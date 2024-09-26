import urllib.request
import json
from math import floor

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(my_request.read()) # Courses is a list of dictionaries

    active_courses = currently_active(courses)
    print(active_courses)

    return active_courses


def currently_active(json_courses):
    active = []

    for course in json_courses:
        data = []
        if course["enabled"] == True:
            data.append(course["fullName"])
            data.append(course["name"])
            data.append(course["year"])
            data.append(sum(course["exercises"]))   # Returns the value of the values listed in 'exercises'
        if len(data) > 0:   # Only adds data to active courses if it isn't empty
            active.append(tuple(data))  # Converts each course data into a tuple that is then added to a active course list
    
    return active


def retrieve_course(course_name):
    urls = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"
    urls = urls.replace("****", course_name)
    my_request = urllib.request.urlopen(urls)
    specific_data = json.loads(my_request.read()) # Courses is a list of dictionaries
    specific_dictionary = dictionary_builder(specific_data)

    print(specific_dictionary)

    return specific_dictionary

def dictionary_builder(specific_data):  
    my_dict = {}
    student_list = []
    hours_list = []
    exercises_list = []

    for key, data in specific_data.items():
        student_list.append(data["students"])
        hours_list.append(data["hour_total"])
        exercises_list.append(data["exercise_total"])



    my_dict["weeks"] = len(specific_data)
    my_dict["students"] = max(student_list)
    my_dict["hours"] = sum(hours_list)
    my_dict["hours_average"] = floor(my_dict["hours"] / my_dict["students"])
    my_dict["exercises"] = sum(exercises_list)
    my_dict["exercises_average"] = floor(my_dict["exercises"] / my_dict["students"])
    
    return my_dict

if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")