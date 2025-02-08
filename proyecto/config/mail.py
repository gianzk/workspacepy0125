import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class Mail:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password    

    def send_email(self, receiver_email, subject, body, file_path=None):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            if file_path:
                with open(file_path, 'rb') as file:
                    attachment = MIMEApplication(file.read(), _subtype="csv")
                    attachment.add_header('Content-Disposition', 'attachment', filename=file_path.split("/")[-1])
                    msg.attach(attachment)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls() 
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, receiver_email, msg.as_string())

            print("✅ Correo enviado exitosamente a", receiver_email)

        except Exception as e:
            print("❌ Error al enviar correo:", e)        