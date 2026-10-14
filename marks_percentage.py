subjects = int(input("Enter number of subjects :"))
total = 0

for i in range(subjects):
  marks = float(input("Enter marks for subject {i+1}:"))
  total += marks
  
  percentage = total / subjects

  if percentage >= 90:
    grade = "A+"
  elif percentage >= 80:
    grade = "A"
  elif percentage >= 70:
    grade = "B"
  elif percentage >= 60:
    grade = "C"
  elif percentage >= 40:
    grade = "D"
  else:
    grade = "Fail"
    
    print("Total marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    5
    
