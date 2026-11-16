#. Take a password from the user. If the password is "python123", print "Login Successful", otherwise print "Invalid Password".
#from django.core.serializers import python


#password=str(input("Enter Password :"))
#if password== 'python123':
#    print("Login Successful")
#else:
#    print("Invalid Password")

from django.core.serializers import python

password = str(input("Enter the password :"))

if password == 'python@123' :
    print("Login successful........ ")
else :
    print("Invalid Password.......")