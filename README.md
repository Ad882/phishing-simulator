<h1 align='center'> Phishing Simulator 🎣 </h1>  

Welcome to the **Phishing Simulator** project! This tool is designed to simulate phishing attacks in a controlled and educational environment. **The goal is NOT to perform real phishing attacks** but to understand how phishing works, how attackers craft emails, and how to protect against them. 🔐

<br>

## 🌟 Features

This project simulates a phishing attack to help users understand the phishing process. The attack is launched via email, which contains a link that leads to a fake login page. Once the victim enters their email and password, this data is stored and can be analyzed by the "attacker".   
The attack itself is **in French** (since it simulates a phishing email targeted at French-speaking users), but the project documentation and setup are in **English**.


<br>

## 🗂️ Project structure

Here's the current structure of the project:

```
phishing-simulator/
├── database/               # Contains the SQLite database and related 
│   ├── activities.db       # Local SQLite database file
│   └── database.py         # Handles database operations
│
├── frontend/               # Frontend files (HTML pages, assets) 
│   ├── email_styles.css    # File styling the phishing email
│   ├── login_page.html     # Activation page
│   └── thank_you.html      # Thank you page
│
├── .env                    # Environment variables for configuration
├── .gitignore              # Git ignore file
├── main.py                 # Main server file
├── README.md               # Project documentation (this file)
├── requirements.txt        # Python dependencies
└── send_email.sh           # Script to automatically send the phishing emails
```


<br>

## 🕵️‍♂️ How the attack works 

1. The server sends an email to the victim with a link to a fake activation page.
2. The victim clicks the 'activate my account' button and is taken to a fake login page.
3. Once the victim has clicked on the button, the server logs the credentials (activation token, IP address and activation time) for further analysis.
4. The victim enters their credentials (password).
5. The server logs the credentials (email and password) for further use.
6. The server responds with a "Thank You" page, confirming the activation and mocking the victim.
  
⚠️ **Important Note:** This project is purely for educational purposes and should never be used in real-world attacks. The goal is to help individuals understand how phishing attacks work, so they can better protect themselves. 🚫

<br>

## ⚡ Quick start

Before you can simulate the attack, you need to set up the project and configure the environment variables.


### 1. Clone the repository 📥

```bash
git clone https://github.com/Ad882/phishing-simulator.git
cd phishing-simulator
```

--- 
### 2. Install dependencies 🧑‍💻

Make sure you have Python 3.7+ installed. Then, install the necessary dependencies with:

```bash
pip install -r requirements.txt
```

--- 
### 3. Configure the `.env` file ⚙️

Create a `.env` file in the root directory of the project. This file contains sensitive configuration data, such as email credentials. Make sure to replace the values with your own.

Example `.env`:

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
TARGET_EMAIL=target-email@gmail.com
```

**Important:**
Gmail is recommended because:
- An **app password** is required for your email account to avoid login issues. Gmail can provide app passwords: On the Google account settings (under "Security" > "App passwords").
- It allows SMTP access (must be enabled in settings).
  
--- 
### 4. Run the server 🚀

To start the server, use the following command:

```bash
python main.py
```

This will start the Flask server on `http://127.0.0.1:5000/`. You can open this URL in your browser to simulate the phishing attack.

<br>

## 🎯 How to simulate an attack 

1. **Configure the email content**: Before running the attack, make sure your `.env` file is correctly configured with the necessary email and server details.

2. **Make the script executable**:
   ```bash
   chmod +x send_email.sh
    ```
   
4. **Run the `send_email.sh` script**: This script will send the phishing email to the target. It automates the process of calling the `/send_email` endpoint to send the phishing email:
   ```bash
   ./send_email.sh
    ```
   
5. **Check the collected data**: The collected passwords can be seen on the databases:
    ```bash
    sqlite3 database/activities.db
    ```
    
Once in the database, check the passwords by entering the following request:
```sql
SELECT * FROM captured_passwords;
```


<br>

## 🔗 Dependencies

- **Flask**: A lightweight web framework for Python to create the backend.
- **Smtplib**: For sending the phishing emails via SMTP.
- **SQLite**: Used for storing the victim's information (email, password, IP, and timestamp).
- **Python-dotenv**: For loading environment variables from the `.env` file.
- **UUID**: For generating unique tokens for the activation link.

Install them using:

```bash
pip install -r requirements.txt
```


<br>

## 🛡️ Protection
To protect against phishing, please follow these few recommendations:
- Check the sender's address.
- Read the email carefully:
  Pay particular attention to
  - spelling mistakes
  - sense of urgency often used
- Verify the link provided to click (by hovering over the link and checking the bottom-left corner of the browser)
- Use tools to verify the link in case of doubt: (e.g., [Google safe-browsing](https://transparencyreport.google.com/safe-browsing/search))

**Protect yourself at all time!**
