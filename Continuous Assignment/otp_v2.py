import random
import smtplib  # Python module to send E-mail

def send_otp():
    server = smtplib.SMTP('smtp.gmail.com',587)  #to create gmail server, "587" is port of gmail
    server.starttls()                              # tls security
    server.login('mihir12242002@gmail.com',password='mmxh eyuj nvik fnuy')
    otp=''.join([str(random.randint(0,9))for i in range(4)])  # func. call of no. of digits
    msg='Hello, your otp is '+str(otp)
    mj=msg
    ml=str(input("Enter receiver's mail: "))
    server.sendmail('mihir12242002@gmail.com',str(ml),msg)
    server.quit()
    # print(otp)
    return otp

def verify_otp(m):
    temp = input("Enter received OTP: ")
    if(str(m)==temp):
        print("Verified..!!!")
    else:
        print("Not Verified")

m = send_otp()
verify_otp(m)