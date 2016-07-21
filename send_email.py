'''This function can be used as an email notifier or a trigger. Whenever a certain 
event occurs, one can call this function and send a custom message to specified email id. '''

import smtplib

def Send_Email(msg):

    FROMADDR = "xyz@abc.com"
    # provide your login  
    LOGIN    = "xyz@abc.com"
    # provide your password 
    PASSWORD = "" 
    TOADDRS  = ["xyz@abc.com"] 
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
    
    Send_Email('Program Terminated With Error code XXX')
