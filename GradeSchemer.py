import commands_GradeSchemer

quit = False
print("Hello, welcome to GradeSchemer\n")
# If quit is ever true, program should terminate
while quit == False:
    courses_dict = False
    # Prompting the user repeatedly until they enter a valid file name
    while courses_dict == False:
        csvfile = input("Enter the name of your csv file (i.e. myfile.csv), or quit by entering 'Q': ")
        # If user enters 'Q', break out of this loop, and outside loop
        if csvfile == 'Q':
            quit = True
            break
        else:
            courses_dict = commands_GradeSchemer.read(csvfile)
            if courses_dict != False:
                cmdloop = True
                while cmdloop == True:
                    # Prompting the user to enter a command
                    usr_cmd = input("\nSelect a command: \nA - Calculate current average in a course\nB - Calculate a final exam grade goal\nQ - Quit\n")
                    # Command Q
                    if usr_cmd == 'Q':
                        quit = True
                        break
                    # Command A
                    elif usr_cmd == 'A':
                        course = input("\nEnter the name of the course of interest: ")
                        commands_GradeSchemer.current_average(courses_dict, course)
                    elif usr_cmd == 'B':
                        course = input("\nEnter the name of the course of interest: ")
                        if course not in courses_dict.keys():
                            print("Invalid course\n")
                            # Break out of command loop
                            break
                        # Checking if the course is valid for this command
                        elif commands_GradeSchemer.add_weightings(courses_dict, course) == 100:
                            print("You have already completed the final exam in this course")
                            # Break out of command loop
                            break

                        temp_dict = courses_dict
                        goal = float(input("Enter your overall grade goal as digits: "))
                        exam_weight = float(input("Enter the weighting of your final exam as digits: "))

                        weighting = commands_GradeSchemer.add_weightings(courses_dict, course)

                        if ((goal < commands_GradeSchemer.add_grade_points(temp_dict, course)) or ((exam_weight + weighting) > 100)):
                            while (goal < commands_GradeSchemer.add_grade_points(temp_dict, course)):
                                goal = float(input("The goal entered was invalid. Enter your overall grade goal as digits again: "))
                            while (exam_weight + weighting) > 100:
                                exam_weight = float(input("The final exam weighting entered was too high. Enter the weighting of your final exam as digits again: "))
                        
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
                        commands_GradeSchemer.final_exam_goal(courses_dict, course, goal, exam_weight, temp_dict)

                            
                            

                




