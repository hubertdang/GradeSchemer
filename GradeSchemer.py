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
                        commands_GradeSchemer.final_exam_goal(courses_dict, course)
                        

            




