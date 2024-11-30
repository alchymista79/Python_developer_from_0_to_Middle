grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

medium_grades = ((sum(grades[0])/len(grades[0])), (sum(grades[1])/len(grades[1])), sum(grades[2])/len(grades[2]),
                 (sum(grades[3])/len(grades[3])), sum(grades[4])/len(grades[4]))
sort_students = sorted(list(students))
grade_sheet = {sort_students[0]: medium_grades[0], sort_students[1]: medium_grades[1], sort_students[2]: medium_grades[2],
               sort_students[3]: medium_grades[3], sort_students[4]: medium_grades[4]}

print(grade_sheet)