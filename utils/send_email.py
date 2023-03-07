from email.message import EmailMessage
import smtplib

def send_email(name, correo):
    remitente = "confirmedbooking53@gmail.com"
    destinatario = correo
    mensaje = \
    f"<h1>Hola {name} tu reserva ha sido confirmada¡<h1>"

    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "¡Enviado desde HotelSericeApi!"
    email.set_content(mensaje, subtype="html")

    # El puerto del protocolo TLS es generalmente 587.
    smtp = smtplib.SMTP("smtp.gmail.com", port=587)
    # Iniciar la conexión segura vía TLS.
    smtp.starttls()

    smtp.login(remitente, "jyoawjnoojibrsoc")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()