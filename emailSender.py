from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

# Função que envia um email de recuperação de senha para o usuário informado
def sendEmail(user: dict):
    
    # Define os dados do remetente
    senderName = 'Alan Patrick Dev'
    senderEmail = os.getenv('FROM_EMAIL','')
    destination = user['email']
    
    # Define os dados do servidor smtp
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587
    smtpUsername = senderEmail
    smtpPassword = os.getenv('FROM_EMAIL_PASSWORD','')

    # Define o texto que será usado no corpo do email
    emailText = f" Olá, {user['login']}!\n a senha da sua conta é: {user['senha']}"

    # Cria um MIMEMultipart definindo o remetente, destinatário e assunto
    mimeMultpart = MIMEMultipart()
    mimeMultpart['from'] = f"{senderName} <{senderEmail}>"
    mimeMultpart['to'] = destination
    mimeMultpart['subject'] = 'Recuperação de senha'

    # Cria o corpo do email usando o texto definido anteriormente
    emailBody = MIMEText(emailText,'plain','utf-8')
    # Anexa o corpo do email ao MIMEMultipart
    mimeMultpart.attach(emailBody)

    # Cria uma conexão com o servidor e envia o email
    with smtplib.SMTP(smtpServer,smtpPort) as server:
        server.ehlo()
        server.starttls()
        server.login(smtpUsername,smtpPassword)
        server.send_message(mimeMultpart)
