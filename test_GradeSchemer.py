import unittest
import commands_GradeSchemer

courses_dict = {'elec2501': [['quiz 1', '1', '0'], ['quiz 2', '1', '70'], ['quiz 3', '1', '25'], ['quiz 4', '1', '100'], ['quiz 5', '1', '75'], ['assignment 1', '2.5', '75'], ['assignment 2', '2.5', '75'], ['lab 1', '4.75', '95'], ['lab 2', '4.75', '87.5'], ['lab 4', '4.75', '72.5'], ['lab 5', '4.75', '90'], ['lab 0', '1', '100'], ['midterm', '20', '82.81']], 'comp1805': [['drill 1', '1.25', '100'], ['drill 2', '1.25', '98.89'], ['drill 4', '1.25', '92.59'], ['drill 7', '1.25', '98.81'], ['drill 8', '1.25', '96.67'], ['drill 10', '1.25', '100'], ['drill 11', '1.25', '88.78'], ['drill 12', '1.25', '89.98'], ['tutorial 1', '1.25', '92.48'], ['tutorial 2', '1.25', '94'], ['tutorial 3', '1.25', '81.04'], ['tutorial 4', '1.25', '87.74'], ['tutorial 7', '1.25', '90.38'], ['tutorial 8', '1.25', '64.29'], ['tutorial 10', '1.25', '84.17'], ['tutorial 12', '1.25', '54.17'], ['problem set 2', '12', '73.77'], ['problem set 3', '12', '87.5'], ['problem set 4', '12', '97.22'], ['problem set 5', '12', '76.79'], ['test 1 part 1', '2.5', '75.09'], ['test 1 part 2', '7.5', '97.22'], ['test 2', '10', '87.84'], ['final', '12', '75.55']], 'sysc2006': [['lab 2', '1', '100'], ['lab 3', '1', '100'], ['lab 4', '1', '100'], ['lab 5', '1', '100'], ['lab 6', '1', '100'], ['lab 7', '1', '100'], ['lab 8', '1', '100'], ['lab 9', '1', '100'], ['lab 10', '1', '100'], ['lab 11', '1', '100'], ['midterm', '25', '78.57']], 'sysc2310': [['quiz 1', '1.25', '100'], ['quiz 2', '1.25', '83'], ['quiz 4', '1.25', '60'], ['quiz 5', '1.25', '40'], ['lab 1', '5', '100'], ['lab 2', '5', '100'], ['lab 3', '5', '100'], ['midterm', '20', '117']], 'math1005': [['test 1', '15', '63.33'], ['test 2', '15', '94.44']]}

class TestGradeSchemer(unittest.TestCase):

    def test_add_grade_points(self):
        self.assertEqual(commands_GradeSchemer.add_grade_points(courses_dict, "elec2501"), 40.3995)

    def test_add_weightings(self):
        self.assertEqual(commands_GradeSchemer.add_weightings(courses_dict, "sysc2006"), 35)

    def test_read(self):
        self.assertEqual(commands_GradeSchemer.read("GradeSchemerData.csv"), courses_dict) 
        self.assertEqual(commands_GradeSchemer.read("NonExistantFile"), False)

    def test_current_average(self):
        self.assertEqual(commands_GradeSchemer.current_average(courses_dict, "math1005"), 78.885)
        self.assertEqual(commands_GradeSchemer.current_average(courses_dict, "notvalidcourse"), False)
        

if __name__ == "__main__":
    unittest.main()
 