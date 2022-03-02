'''
You have been given partial code. The objective is to reproduce the output as 
shown in the file - Output.png

1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students
   list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for 
   each iteration using ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats 
   in the course and the output should reflect that as shown in the picture.
'''

import CourseClass as cc


def main():

   name = 'MIS 4322 - Advanced Python'
   crn = '250309'
   seats = 4
   status = 'open'
   students = ['John','James','Jill','Jack','Joanne']

   adv_py = cc.Course(name,crn,seats,status)

   for stud in students:
      if adv_py.get_seats() > 0:
         #Student Registration
         stud = cc.Register(stud,crn)

         #Seats
         current_seats = adv_py.get_seats()
         current_seats -= 1
         adv_py.update_seat_count()

         #Output
         print("Student Name:", stud.get_name())
         print("Course Name:", adv_py.get_name())
         print("CRN:", adv_py.get_crn())
         print("Seats left:", adv_py.get_seats())
         print()
      else:
         print("Sorry " + stud + ", registration is closed for " + adv_py.get_name())
      print()
main()



        
    
    
