import unittest
from unittest.mock import patch
import commands_GradeSchemer

# Dictionary returned by read() when the user inputs GradeSchemerData.csv
courses_dict = {'elec2501': [['quiz 1', '1', '0'], ['quiz 2', '1', '70'], ['quiz 3', '1', '25'], ['quiz 4', '1', '100'], ['quiz 5', '1', '75'], ['assignment 1', '2.5', '75'], ['assignment 2', '2.5', '75'], ['lab 1', '4.75', '95'], ['lab 2', '4.75', '87.5'], ['lab 4', '4.75', '72.5'], ['lab 5', '4.75', '90'], ['lab 0', '1', '100'], ['midterm', '20', '82.81']], 'comp1805': [['drill 1', '1.25', '100'], ['drill 2', '1.25', '98.89'], ['drill 4', '1.25', '92.59'], ['drill 7', '1.25', '98.81'], ['drill 8', '1.25', '96.67'], ['drill 10', '1.25', '100'], ['drill 11', '1.25', '88.78'], ['drill 12', '1.25', '89.98'], ['tutorial 1', '1.25', '92.48'], ['tutorial 2', '1.25', '94'], ['tutorial 3', '1.25', '81.04'], ['tutorial 4', '1.25', '87.74'], ['tutorial 7', '1.25', '90.38'], ['tutorial 8', '1.25', '64.29'], ['tutorial 10', '1.25', '84.17'], ['tutorial 12', '1.25', '54.17'], ['problem set 2', '12', '73.77'], ['problem set 3', '12', '87.5'], ['problem set 4', '12', '97.22'], ['problem set 5', '12', '76.79'], ['test 1 part 1', '2.5', '75.09'], ['test 1 part 2', '7.5', '97.22'], ['test 2', '10', '87.84'], ['final', '12', '75.55']], 'sysc2006': [['lab 2', '1', '100'], ['lab 3', '1', '100'], ['lab 4', '1', '100'], ['lab 5', '1', '100'], ['lab 6', '1', '100'], ['lab 7', '1', '100'], ['lab 8', '1', '100'], ['lab 9', '1', '100'], ['lab 10', '1', '100'], ['lab 11', '1', '100'], ['midterm', '25', '78.57']], 'sysc2310': [['quiz 1', '1.25', '100'], ['quiz 2', '1.25', '83'], ['quiz 4', '1.25', '60'], ['quiz 5', '1.25', '40'], ['lab 1', '5', '100'], ['lab 2', '5', '100'], ['lab 3', '5', '100'], ['midterm', '20', '117']], 'math1005': [['test 1', '15', '63.33'], ['test 2', '15', '94.44']]}

class TestGradeSchemer(unittest.TestCase):
    def test_add_grade_points(self):
        self.assertEqual(commands_GradeSchemer.add_grade_points(courses_dict, "elec2501"), 40.3995)

    def test_add_weightings(self):
        self.assertEqual(commands_GradeSchemer.add_weightings(courses_dict, "sysc2006"), 35)

    def test_read(self):
        # The inputted file exists in the working directory
        self.assertEqual(commands_GradeSchemer.read("GradeSchemerData.csv"), courses_dict) 
        # The inputted file does not exist in the working directory
        self.assertEqual(commands_GradeSchemer.read("NonExistantFile"), False)

    def test_current_average(self):
        # The course inputted exists (i.e. is not in the csv file)
        self.assertEqual(commands_GradeSchemer.current_average(courses_dict, "math1005"), 78.885)
        # The course inputted does not exist (i.e. is not in the csv file)
        self.assertEqual(commands_GradeSchemer.current_average(courses_dict, "notvalidcourse"), False)

    def test_final_exam_goal(self):
        # Normal goal, exam weighting is possible, there are no missing assessments
        self.assertEqual(commands_GradeSchemer.final_exam_goal(courses_dict, "sysc2310", 80, 50, {'elec2501': [['quiz 1', '1', '0'], ['quiz 2', '1', '70'], ['quiz 3', '1', '25'], ['quiz 4', '1', '100'], ['quiz 5', '1', '75'], ['assignment 1', '2.5', '75'], ['assignment 2', '2.5', '75'], ['lab 1', '4.75', '95'], ['lab 2', '4.75', '87.5'], ['lab 4', '4.75', '72.5'], ['lab 5', '4.75', '90'], ['lab 0', '1', '100'], ['midterm', '20', '82.81']], 'comp1805': [['drill 1', '1.25', '100'], ['drill 2', '1.25', '98.89'], ['drill 4', '1.25', '92.59'], ['drill 7', '1.25', '98.81'], ['drill 8', '1.25', '96.67'], ['drill 10', '1.25', '100'], ['drill 11', '1.25', '88.78'], ['drill 12', '1.25', '89.98'], ['tutorial 1', '1.25', '92.48'], ['tutorial 2', '1.25', '94'], ['tutorial 3', '1.25', '81.04'], ['tutorial 4', '1.25', '87.74'], ['tutorial 7', '1.25', '90.38'], ['tutorial 8', '1.25', '64.29'], ['tutorial 10', '1.25', '84.17'], ['tutorial 12', '1.25', '54.17'], ['problem set 2', '12', '73.77'], ['problem set 3', '12', '87.5'], ['problem set 4', '12', '97.22'], ['problem set 5', '12', '76.79'], ['test 1 part 1', '2.5', '75.09'], ['test 1 part 2', '7.5', '97.22'], ['test 2', '10', '87.84'], ['final', '12', '75.55']], 'sysc2006': [['lab 2', '1', '100'], ['lab 3', '1', '100'], ['lab 4', '1', '100'], ['lab 5', '1', '100'], ['lab 6', '1', '100'], ['lab 7', '1', '100'], ['lab 8', '1', '100'], ['lab 9', '1', '100'], ['lab 10', '1', '100'], ['lab 11', '1', '100'], ['midterm', '25', '78.57']], 'sysc2310': [['quiz 1', '1.25', '100'], ['quiz 2', '1.25', '83'], ['quiz 4', '1.25', '60'], ['quiz 5', '1.25', '40'], ['lab 1', '5', '100'], ['lab 2', '5', '100'], ['lab 3', '5', '100'], ['midterm', '20', '117'], ['lab x', '10', '100']], 'math1005': [['test 1', '15', '63.33'], ['test 2', '15', '94.44']]}), 56.125)
        # Goal is too low, exam weighting is possible, there are no missing assessments
        self.assertEqual(commands_GradeSchemer.final_exam_goal(courses_dict, "sysc2310", 20, 50, {'elec2501': [['quiz 1', '1', '0'], ['quiz 2', '1', '70'], ['quiz 3', '1', '25'], ['quiz 4', '1', '100'], ['quiz 5', '1', '75'], ['assignment 1', '2.5', '75'], ['assignment 2', '2.5', '75'], ['lab 1', '4.75', '95'], ['lab 2', '4.75', '87.5'], ['lab 4', '4.75', '72.5'], ['lab 5', '4.75', '90'], ['lab 0', '1', '100'], ['midterm', '20', '82.81']], 'comp1805': [['drill 1', '1.25', '100'], ['drill 2', '1.25', '98.89'], ['drill 4', '1.25', '92.59'], ['drill 7', '1.25', '98.81'], ['drill 8', '1.25', '96.67'], ['drill 10', '1.25', '100'], ['drill 11', '1.25', '88.78'], ['drill 12', '1.25', '89.98'], ['tutorial 1', '1.25', '92.48'], ['tutorial 2', '1.25', '94'], ['tutorial 3', '1.25', '81.04'], ['tutorial 4', '1.25', '87.74'], ['tutorial 7', '1.25', '90.38'], ['tutorial 8', '1.25', '64.29'], ['tutorial 10', '1.25', '84.17'], ['tutorial 12', '1.25', '54.17'], ['problem set 2', '12', '73.77'], ['problem set 3', '12', '87.5'], ['problem set 4', '12', '97.22'], ['problem set 5', '12', '76.79'], ['test 1 part 1', '2.5', '75.09'], ['test 1 part 2', '7.5', '97.22'], ['test 2', '10', '87.84'], ['final', '12', '75.55']], 'sysc2006': [['lab 2', '1', '100'], ['lab 3', '1', '100'], ['lab 4', '1', '100'], ['lab 5', '1', '100'], ['lab 6', '1', '100'], ['lab 7', '1', '100'], ['lab 8', '1', '100'], ['lab 9', '1', '100'], ['lab 10', '1', '100'], ['lab 11', '1', '100'], ['midterm', '25', '78.57']], 'sysc2310': [['quiz 1', '1.25', '100'], ['quiz 2', '1.25', '83'], ['quiz 4', '1.25', '60'], ['quiz 5', '1.25', '40'], ['lab 1', '5', '100'], ['lab 2', '5', '100'], ['lab 3', '5', '100'], ['midterm', '20', '117'], ['lab x', '10', '100']], 'math1005': [['test 1', '15', '63.33'], ['test 2', '15', '94.44']]}), False)
        # Normal goal, exam weighting is impossible, there are no missing assessments
        self.assertEqual(commands_GradeSchemer.final_exam_goal(courses_dict, "elec2501", 82, 60, courses_dict), False)
        # Goal is too low, exam weighting is impossible, there are no missing assessments
        self.assertEqual(commands_GradeSchemer.final_exam_goal(courses_dict, "elec2501", 10, 60, courses_dict), False)

    @patch("commands_GradeSchemer.current_average")
    def test_get_letter_grade(self, mock_current_average):
        # Normal grade in A range
        mock_current_average.return_value = 85
        self.assertEqual(commands_GradeSchemer.get_letter_grade(courses_dict, "comp1805"), "A")
        # Grade is right under A range 
        mock_current_average.return_value = 84.999999999
        self.assertEqual(commands_GradeSchemer.get_letter_grade(courses_dict, "comp1805"), "A-")
        # Negative average 
        mock_current_average.return_value = -1
        self.assertEqual(commands_GradeSchemer.get_letter_grade(courses_dict, "math1005"), False)
        # Invalid course name
        mock_current_average.return_value = False
        self.assertEqual(commands_GradeSchemer.get_letter_grade(courses_dict, "comp1234"), False)
        

if __name__ == "__main__":
    unittest.main()

 