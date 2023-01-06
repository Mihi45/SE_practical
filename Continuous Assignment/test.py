import random
import get
import smtplib

      # return(otp)
server =smtplib.SMTP('smtp.gmail.com',587)
Sender=get.email
Pass=get.password
email=input("Enter your email: ")
server.starttls()
server.login(Sender,password=Pass)
otp=''.join([str(random.randint(0,9))for i in range(6)])

msg='Hello, your otp is '+str(otp)
server.sendmail(Sender,email,msg)
server.quit()
# print(otp)
print("Enter The OTP")
a=input();

if a==otp:
  print("Verified")
else :
  print("Failed")
