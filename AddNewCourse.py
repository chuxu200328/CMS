import json

print("Welcome to the Course Schedule Manager")
print("please enter the following information in oder to add a new course")

# user enter course information
semester = input("Semester: ")
course = input("Course: ")
title = input("Title: ")
instructor = input("Instructor: ")
location = input("Location: ")
print("(0 for mon, 1 for tue, 2 for wed, 3 for thu, 4 for fri)")
frequency_arr = []
while True:
    temp_freq = input("Frequency(enter N to end input frequency): ")
    if (temp_freq != "N"):
        frequency_arr.append(temp_freq)
    else:
        break
startTime = input("Start Time(format: HH:MM): ")
endTime = input("End Time(format: HH:MM): ")

with open('CourseData.json', 'r+') as CourseDataFile:
    FileData = json.load(CourseDataFile)
    newArr = FileData['emp_details']
    newArr.append({
        "semester": semester,
        "course": course,
        "title": title,
        "instructor": instructor,
        "location": location,
        "frequency": frequency_arr,
        "startTime": startTime,
        "endTime": endTime,
    })
    FileData['emp_details'] = newArr
    CourseDataFile.seek(0)
    json.dump(FileData, CourseDataFile, indent=4)
    CourseDataFile.truncate()
