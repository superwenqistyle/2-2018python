from test import *
s1 = Student('jack', 25, 'football')
s1.showperson()
print('*'*20) 
#无法访问__taste,导致报错
#s1.showstudent()
s1.construction('rose', 30, 'basketball')
s1.showperson()
print('*'*20)

s1.showstudent()
print('*'*20)
 
Student.testbug()
                      
