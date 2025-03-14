nstudent = int (input("Enter the number of students: "))

score = int(input("Enter your score: "))
if score >= 80:
    value ="Excellent" 
elif score >= 60:
    value ="Very good"
elif score >= 40:
    value ="Good"
elif score >=0:
    value ="You need to study more"
print(f"{value}\n"* 16)