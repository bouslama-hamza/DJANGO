import smtplib
import random
#generale function for sending email
def send_email(email,password,type):
    EMAIL_ADDRESS = 'test.herbaly@gmail.com'
    EMAIL_PASSWORD = 'badBOY@2020'
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        if type == 'send':
            subject = 'Request To Access To Hearbly Data Base'
            body = 'This Person is trying to access to Hearbly Data Base System .if it able to : please inser it into the Data Base Query System with the fallowing email : '+str(email)
            msg = f'Subject : {subject} \n\n {body}'
            smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)
        elif type == 'request':
            subject = 'You Have Been Add To Hearbly Data Base'
            body = 'You Are New Able To Acess To Hearbly Data Base System ,Use The Folowing Information To Acces : \nUsername : '+email+'\nPassword : '+password 
            msg = f'Subject : {subject} \n\n {body}'
            smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)
        elif type == 'change':
            n = random.randint(11111111,99999999)
            subject = 'Request To change Password'
            body = 'Your request to change your password has been added successfuly please use the following code to access : \n'+str(n)
            msg = f'Subject : {subject} \n\n {body}'
            smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)
            return n
