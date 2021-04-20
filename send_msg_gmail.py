import smtplib as s

#creates session(for gmail port 587)
a = s.SMTP('smtp.gmail.com', 587)

# start TLS security
a.starttls()

# gmail and password
a.login("_______________@gmail.com","_____________")

msg="Hello pycharm day 4"

#sending mail

a.sendmail("_______________@gmail.com","___________8@gmail.com",msg)

print("msg sent")

#session quit
a.quit()
