"""
grading system 
a python program that will enable students to grade their marks/score by inputing the exert marks
the system should allow students to enter marks for up to 5 subjects and find the total marks and avarage score
"""

x= int(input ("english grade:"))
y= int(input ("math grade:"))
z= int(input ("biology grade:"))
a= int(input ("chemistry grade:"))
b= int(input ("art grade:"))
print("total=",x+y+z+a+b )
avarage= x+y+z+a+b /5
print(avarage)
if avarage>200:
 print("grade: A")
elif avarage>180:
   print("grade: B")
elif avarage>140:
   print("grade: C")
elif avarage<140:
   print("grade: F")