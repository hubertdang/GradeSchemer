import csv
import os

# Function to read in a csv and return a dictionary with all the data from the csv stored
def read(csvfile):
    path = "/home/hubert/Documents/GradeSchemer/" + csvfile
    isExist = os.path.exists(path)
    if isExist == False:
        print("Invalid file")
        return False
    with open(csvfile, 'r') as file:
        csvreader = csv.DictReader(file)

        courses_dict = {}

        for row in csvreader:
            # If the course is not a key in courses_dict, initialize a key/value pair
            if row["Course"] not in courses_dict.keys():
                courses_dict[row["Course"]] = [[row["Assessment Name"], row["Assessment Weighting (%)"], row["Grade"]]]
            # If the course is already a key in courses_dict, append to the list
            else:
                courses_dict[row["Course"]] += [[row["Assessment Name"], row["Assessment Weighting (%)"], row["Grade"]]]

    return courses_dict

# Function to add the weightings of graded assessments
def add_weightings(courses_dict, course):
    assessments = courses_dict.get(course)
    grade_weightings = 0
    for assessment in assessments:
        grade_weightings += float(assessment[1])
    return grade_weightings

# Function to add the grade points of graded assessments
def add_grade_points(courses_dict, course):
    assessments = courses_dict.get(course)
    grade_points = 0
    for assessment in assessments:
        grade_points += float(assessment[2]) * 0.01 * float(assessment[1])
    return grade_points

# Function to calculate the user's average (so far) in a course
def current_average(courses_dict, course):
    if course not in courses_dict.keys():
        print("Invalid course\n")
        return False

    assessments = courses_dict.get(course)

    grade_weightings = add_weightings(courses_dict, course)
    grade_points = add_grade_points(courses_dict, course)

    avg = grade_points/grade_weightings * 100
    print("Your current average is " + str(avg) + "\n")
    return avg
        
# Function to calculate a required grade on a course's final exam for the user to achieve their overall grade goal
def final_exam_goal(courses_dict, course, goal, exam_weight, temp_dict):
    total_gp = add_grade_points(temp_dict, course)
    # Goal is too low
    if (goal < total_gp) or (goal > 100):
        return False
    if (exam_weight + add_weightings(courses_dict, course)) > 100:
        return False
    required_grade = ((goal - total_gp) / exam_weight) * 100
    print("\nYou need a " + str(required_grade) + " on the final exam to get a " + str(goal) + " in the course\n")
    return required_grade    

# Function to convert a current grade to a letter grade
def get_letter_grade(courses_dict, course):
    avg = current_average(courses_dict, course)
    if avg == False:
        return False
    elif avg >= 90:
        print("Your equivalent letter grade is A+")
        return "A+"
    elif avg >= 85:
        print("Your equivalent letter grade is A")
        return "A"
    elif avg >= 80:
        print("Your equivalent letter grade is A-")
        return "A-"
    elif avg >= 77:
        print("Your equivalent letter grade is B+")
        return "B+"
    elif avg >= 73:
        print("Your equivalent letter grade is B")
        return "B"
    elif avg >= 70:
        print("Your equivalent letter grade is B-")
        return "B-"
    elif avg >= 67:
        print("Your equivalent letter grade is C+")
        return "C+"
    elif avg >= 63:
        print("Your equivalent letter grade is C")
        return "C"
    elif avg >= 60:
        print("Your equivalent letter grade is C-")
        return "C-"
    elif avg >= 57:
        print("Your equivalent letter grade is D+")
        return "D+"
    elif avg >= 53:
        print("Your equivalent letter grade is D")
        return "D"
    elif avg >= 50:
        print("Your equivalent letter grade is D-")
        return "D-"
    elif avg >= 0:
        print("Your equivalent letter grade is F")
        return "F"
    else:
        print("Invalid grade")
        return False








        




    




