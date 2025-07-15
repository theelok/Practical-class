score = float(input("Enter a score: "))
grade =""

if score >=90 and score<=100:
    grade ="A"
elif score >=80 and score<90:
    grade ="B"
elif score >=80 and score<90:
    grade ="C"
elif score >=70 and score<80:
    grade ="D"
elif score >=60 and score<70:
    grade ="E"
else: 
      grade ="Fail"

match grade:
   case "A"| "F":
    print("You got an " ,grade)
   case "B"| "C":
    print("You got an " ,grade)
   case "D"| "E":
    print("You got an " ,grade)
   case " ":
    print("You have enter wrong value " )