import json

with open('CourseData.json', 'r') as CourseDataFile:
    FileData = json.load(CourseDataFile)
    if (FileData['emp_details'] == []):
        print("No course yet.")
    else:
        for course in FileData['emp_details']:
            print("Semester: " + course['semester'])
            print("Course: " + course['course'])
            print("Title: " + course['title'])
            print("Instructor: " + course['instructor'])
            print("Location: " + course['location'])
            print("Frequency: " + str(course['frequency']))
            print("Start Time: " + course['startTime'])
            print("End Time: " + course['endTime'])
            print("=========================================")
            print("")
