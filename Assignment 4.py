#Q1 Grades
x = int(input("Enter marks:"))
if x<25:
    print("F")
elif (x>=25) and (x<45):
    print("E")
elif (x>=45) and (x<50):
    print("D")
elif (x>=50) and (x<60):
    print("C")
elif (x>=60) and (x<80):
    print("B")
elif (x>=80) and (x<100):
    print("A")
else:
    print("Not correct marks")

print("\n")

#Q2 Leap Year
year = int(input("Enter year: "))

if year % 400 == 0 :
    print(year, "is a Leap Year")
elif year % 100 == 0 :
    print(year, "is not a Leap Year")
elif year % 4 == 0 :
    print(year, "is a Leap Year")
else :
    print(year, "is not a Leap Year")

#Q3
import random as r
score = 0
print("I am going to generate random variable")
for i in range(5):
    first = r.randint(1,10)
    second = r.randint(1,10)
    print(first," * ",second, " = ",end = "")
    product = first*second
    ask = eval(input(""))
    if(ask==product):
        score+=1
        print("You got the score")
    else:
        print("Your answer is wrong")
        print(first," * ",second," = ",product)
print("Total score = ", score,"/5")


#Q4
x=200

for i in range(x):

    if i % 5 == 2:
       if i % 6 == 3:
          if i % 7 == 2:
             print(i, 'candies are in the bowl!')
