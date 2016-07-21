'''This function can be used as an email notifier or a trigger. Whenever a certain 
event occurs, one can call this function and send a custom message to specified email id. '''

import smtplib

def send_email(msg):

    FROMADDR = "xyz@gmail.com"
    # provide your login id 
    LOGIN    = "xyz@gmail.com"
    # provide your password 
    PASSWORD = "" 
    TOADDRS  = ["xyz@gmail.com","abc@gmail.com"] 
    SUBJECT  = msg 
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" 
    % (FROMADDR, ", ".join(TOADDRS), SUBJECT) ) 
    msg += msg+"\r\n"
    server = smtplib.SMTP('smtp.gmail.com:587') 
    server.set_debuglevel(1) 
    server.ehlo() 
    server.starttls() 
    server.login(LOGIN, PASSWORD) 
    server.sendmail(FROMADDR, TOADDRS, msg) 
    server.quit()
    
if __name__ == '__main__':
    send_email('Program Terminated With Error code XXX')
