from tkinter import *
import json
import random
import string


def generate_random_string(array):
    # Generate a random string of 6 characters
    # consisting of lowercase letters and digits
    chars = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(chars, k=6))

    # Check if the random string exists in the array
    for obj in array:
        if obj.id == random_string:
            # If the random string is found in the array,
            # generate a new random string and try again
            return generate_random_string(array)

    # If the random string is not found in the array,
    # return the string
    return random_string


def weekdaysToShortString(weekdays):
    # List of strings representing the weekdays
    weekdaysArr = ["Monday", "Tuesday", "Wednesday",
                   "Thursday", "Friday", "Saturday", "Sunday"]

    # Convert the integers to weekdays
    weekday_names = [weekdaysArr[number - 1] for number in weekdays]
    weekday_string = ", ".join(weekday_names)
    return weekday_string


def AddNewCourse():

    def AddNewCourse_onSubmit():
        frequency_arr = []
        if monVar.get() == 1:
            frequency_arr.append(1)
        if tueVar.get() == 1:
            frequency_arr.append(2)
        if wedVar.get() == 1:
            frequency_arr.append(3)
        if thrVar.get() == 1:
            frequency_arr.append(4)
        if friVar.get() == 1:
            frequency_arr.append(5)
        if satVar.get() == 1:
            frequency_arr.append(6)
        if sunVar.get() == 1:
            frequency_arr.append(7)

        with open('CourseData.json', 'r+') as CourseDataFile:
            FileData = json.load(CourseDataFile)
            newArr = FileData['emp_details']
            newArr.append({
                "id": generate_random_string(newArr),
                "semester": Semester_input_area.get(),
                "course": Course_input_area.get(),
                "location": location_input_area.get(),
                "frequency": frequency_arr,
                "startTime": start_time_input_area.get(),
                "endTime": start_time_input_area.get(),
            })
            FileData['emp_details'] = newArr
            CourseDataFile.seek(0)
            json.dump(FileData, CourseDataFile, indent=4)
            CourseDataFile.truncate()
            addCourseScreen.destroy()

    # user enter course information
    addCourseScreen = Toplevel()
    addCourseScreen.title('Add New Course')
    addCourseScreen.geometry("600x400")

    monVar = IntVar()
    tueVar = IntVar()
    wedVar = IntVar()
    thrVar = IntVar()
    friVar = IntVar()
    satVar = IntVar()
    sunVar = IntVar()

    title = Label(addCourseScreen, text="Add New Course",
                  font=("Arial", 22)).place(x=40, y=20)
    Semester = Label(addCourseScreen,
                     text="Semester:").place(x=40,
                                             y=80)
    Semester_input_area = Entry(addCourseScreen,
                                width=30,)
    Semester_input_area.place(x=110, y=80)
    Course = Label(addCourseScreen,
                   text="Course:").place(x=40,
                                         y=120)
    Course_input_area = Entry(addCourseScreen,
                              width=30)
    Course_input_area.place(x=110, y=120)
    location = Label(addCourseScreen,
                     text="Location:").place(x=40,
                                             y=160)
    location_input_area = Entry(addCourseScreen,
                                width=30)
    location_input_area.place(x=110, y=160)
    frequency = Label(addCourseScreen,
                      text="frequency:").place(x=40,
                                               y=200)
    frequency_input_area_1 = Checkbutton(addCourseScreen,
                                         text='Mon.', variable=monVar)
    frequency_input_area_1.place(x=110, y=200)
    # frequency_input_area_1.pack()
    frequency_input_area_2 = Checkbutton(addCourseScreen,
                                         text='Tue.', variable=tueVar)
    frequency_input_area_2.place(x=170, y=200)
    # frequency_input_area_2.pack()
    frequency_input_area_3 = Checkbutton(addCourseScreen,
                                         text='Wed.', variable=wedVar)
    frequency_input_area_3.place(x=230, y=200)
    # frequency_input_area_3.pack()
    frequency_input_area_4 = Checkbutton(addCourseScreen,
                                         text='Thr.', variable=thrVar)
    frequency_input_area_4.place(x=290, y=200)
    # frequency_input_area_4.pack()
    frequency_input_area_5 = Checkbutton(addCourseScreen,
                                         text='Fri.', variable=friVar)
    frequency_input_area_5.place(x=350, y=200)
    # frequency_input_area_5.pack()
    frequency_input_area_6 = Checkbutton(addCourseScreen,
                                         text='Sat.', variable=satVar)
    frequency_input_area_6.place(x=410, y=200)
    # frequency_input_area_6.pack()
    frequency_input_area_7 = Checkbutton(addCourseScreen,
                                         text='Sun.', variable=sunVar)
    frequency_input_area_7.place(x=470, y=200)
    # frequency_input_area_7.pack()
    start_time = Label(addCourseScreen,
                       text="Start Time:").place(x=40, y=240)
    start_time_input_area = Entry(addCourseScreen,
                                  width=30)
    start_time_input_area.place(x=110, y=240)
    end_time = Label(addCourseScreen,
                     text="End  Time:").place(x=40, y=280)
    end_time_area = Entry(addCourseScreen,
                          width=30)
    end_time_area.place(x=110, y=280)
    submit_button = Button(addCourseScreen, text="Add",
                           command=AddNewCourse_onSubmit).place(x=40, y=320)
    cancel_button = Button(addCourseScreen, text="Cancel",
                           command=addCourseScreen.destroy).place(x=100, y=320)


def ShowAllCourses():
    ShowAllCoursesScreen = Toplevel()
    ShowAllCoursesScreen.title('All courses')
    ShowAllCoursesScreen.geometry("600x400")
    listbox = Listbox(ShowAllCoursesScreen, width=400, height=500)
    # Create a vertical scrollbar and attach it to the listbox
    scrollbar = Scrollbar(ShowAllCoursesScreen, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    with open('CourseData.json', 'r+') as CourseDataFile:
        FileData = json.load(CourseDataFile)
        currentCourses = FileData['emp_details']
        # Create a large number of labels and pack them into the inner frame
        for c in currentCourses:
            listbox.insert("end", 'Semester: ' + c['semester'])
            listbox.insert("end", 'Course: ' + c['course'])
            listbox.insert("end", 'Location: ' + c['location'])
            listbox.insert("end", 'Frequency: ' +
                           weekdaysToShortString(c['frequency']))
            listbox.insert("end", 'Start Time: ' + c['startTime'])
            listbox.insert("end", 'End Time: ' + c['endTime'])
            listbox.insert(
                "end", '------------------------------------------------------------')

    listbox.config(yscrollcommand=scrollbar.set)
    listbox.pack()


mainScreen = Tk()
mainScreen.title('Course Schedule Manager')
mainScreen.geometry("450x300")

title = Label(mainScreen, text="Course Schedule Manager",
              font=("Arial", 25)).place(x=40, y=20)

submit_button = Button(mainScreen, text="Add New Class",
                       command=AddNewCourse).place(x=40, y=80)
submit_button = Button(mainScreen, text="Show all Classes",
                       command=ShowAllCourses).place(x=40, y=120)
submit_button = Button(mainScreen, text="Quit",
                       command=mainScreen.destroy).place(x=40, y=160)

mainScreen.mainloop()
