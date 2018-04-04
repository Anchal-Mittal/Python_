import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

sender="mayank.mcs17.du@gmail.com"
recv="anchal.mcs17.du@gmail.com"
#Next, log in to the server
server.starttls()
server.login(sender, "")

#Send the mail
msg = "chutki ko mom se daat padi , haha khargosh ko maza aya LOL!!! (from python)" # The /n separates the message from the headers
server.sendmail(sender,recv, msg)
server.quit()
