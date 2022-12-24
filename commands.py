import csv

# Function to read in a csv and return a dictionary with all the data from the csv stored
def read():
    csvfile = input("Enter the name of your csv file (i.e. myfile.csv): ")
    # Read in the grade log as a csv file
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
def current_average(courses_dict):
    course = input("\nEnter the name of the course of interest: ")
    assessments = courses_dict.get(course)

    grade_weightings = add_weightings(courses_dict, course)
    grade_points = add_grade_points(courses_dict, course)

    avg = grade_points/grade_weightings * 100
    print("Your current average is " + str(avg) + "\n")
    return avg
        
# Function to calculate a required grade on a course's final exam for the user to achieve their overall grade goal
def final_exam_goal(courses_dict):
    course = input("\nEnter your course of interest: ")
    # Checking if the course is valid for this command
    if add_weightings(courses_dict, course) == 100:
        print("You have already completed the final exam in this course")
        return 

    goal = float(input("Enter your overall grade goal: "))
    exam_weight = float(input("Enter the weighting of your final exam: "))

    weighting = add_weightings(courses_dict, course)

    temp_dict = courses_dict

    total_weight = weighting + exam_weight
    # Fill in empty data on assessments
    while total_weight < 100:
        print("\nThere are some missing assessments.\n")
        print("Your total weighting is currently " + str(total_weight) + "/100, the remaining weight is " + str(100 - total_weight) + "\n")
        name = input("Enter an ungraded/incomplete assessment name: ")
        weight = float(input("Enter the assessment's weighting: "))
        grade = float(input("Enter a estimated grade for the assessment: "))
        temp_dict[course] += [[name, weight, grade]]
        total_weight += weight

        if total_weight > 100:
            total_weight -= weight
            print("\nThe weighting of that assessment is invalid (too high)\n")

    required_grade = ((goal - add_grade_points(temp_dict, course)) / exam_weight) * 100
    print("\nYou need a " + str(required_grade) + " on the final exam to get a " + str(goal) + " in the course\n")
    return required_grade    

        




    




