n = int(input("podaj liczbe studentow:"))
i = 1
grade = 0
while i<=n:
    grade_per = int(input("podaj ocene dla stud"))
    grade= grade+grade_per
    i = i+1

print(grade/n)



