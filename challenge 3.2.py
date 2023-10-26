# 3.2 implement a function called sort_students that takes a list of student objects and sorts the list based on their cgpa ( cumulative grade point average) in descending order. each student object has the following attributes: name (string),roll_number( string) and cgpa ( float). test the function with different input list of student
# objects.
class student:
    def __init__(self,name,roll_number,cgpa):
      self.name=name
      self.roll_number=roll_number
      self.cgpa=cgpa

def sort_students(student_list):
 sorted_students =sorted(  student_list, key= lambda student=student: student.cgpa, reverse=True)
 return sorted_students
  
#example usage:
Student1= student("alice","s123", 3.7)
student2= student("bob", "s124", 3.9)
student3= student("charlie", "s125", 3.5)
student4= student(" david","s126", 3.8)

students = [ Student1, student2, student3, student4]
sorted_students= sort_students(students)

#print the sorted list of students by cgpa in descending order
for student in sorted_students:
  print(f"name:{student.name} ,number:{student.roll_number},cgpa: {student.cgpa}")

