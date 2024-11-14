students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(sorted(students))
students_abc = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_students = dict(zip(students_abc, grades))
print(grades_students)
grades_students_new = {'Aaron': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Johnny': [4, 5, 5, 2], 'Khendrik': [4, 4, 3], 'Steve': [5, 5, 5, 4, 5]}
Aaron = [5, 3, 3, 5, 4]
sum_Aaron = sum(Aaron)
grade_Aaron = sum_Aaron/len(Aaron)
Bilbo = [2, 2, 2, 3]
sum_Bilbo = sum(Bilbo)
grade_Bilbo = sum_Bilbo/len(Bilbo)
Johnny = [4, 5, 5, 2]
sum_Johnny = sum(Johnny)
grade_Johnny = sum_Johnny/len(Johnny)
Khendrik = [4, 4, 3]
sum_Khendrik = sum(Khendrik)
grade_Khendrik = sum_Khendrik/len(Khendrik)
Steve = [5, 5, 5, 4, 5]
sum_Steve = sum(Steve)
grade_Steve = sum_Steve/len(Steve)
set_ = {'Aaron':grade_Aaron, 'Bilbo':grade_Bilbo, 'Johnny': grade_Johnny, 'Khendrik':grade_Khendrik, 'Steve': grade_Steve}
print(set_)