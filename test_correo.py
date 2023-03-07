from email.message import EmailMessage
import smtplib

remitente = "confirmedbooking53@gmail.com"
destinatario = "jalvinrene@gmail.com"
mensaje = "¡Hola, mundo!"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"]= "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "jyoawjnoojibrsoc")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit() 
