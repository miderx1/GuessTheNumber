from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os


def sendEmail(user: dict):
    senderName = 'Alan Patrick Dev'
    senderEmail = os.getenv('FROM_EMAIL','')
    destination = user['email']

    smtpServer = 'smtp.gmail.com'
    smtpPort = 587
    smtpUsername = senderEmail
    smtpPassword = os.getenv('FROM_EMAIL_PASSWORD','')

    emailText = f" Olá, {user['login']}!\n a senha da sua conta é: {user['senha']}"

    mimeMultpart = MIMEMultipart()
    mimeMultpart['from'] = f"{senderName} <{senderEmail}>"
    mimeMultpart['to'] = destination
    mimeMultpart['subject'] = 'Recuperação de senha'

    emailBody = MIMEText(emailText,'plain','utf-8')
    mimeMultpart.attach(emailBody)

    with smtplib.SMTP(smtpServer,smtpPort) as server:
        server.ehlo()
        server.starttls()
        server.login(smtpUsername,smtpPassword)
        server.send_message(mimeMultpart)
