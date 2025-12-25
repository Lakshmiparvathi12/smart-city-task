from flask import Flask, render_template, request
import sqlite3
import uuid
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ---------- Database Connection ----------
def get_db_connection():
    conn = sqlite3.connect("issues.db")
    return conn

# ---------- Home Page ----------
@app.route("/")
def index():
    return render_template("index.html")

# ---------- Submit Issue ----------
@app.route("/submit", methods=["POST"])
def submit():
    city = request.form["city"]
    area = request.form["area"]
    street = request.form["street"]
    issue = request.form["issue"]
    email = request.form["email"]

    # Generate short unique reference ID
    ref_id = str(uuid.uuid4())[:6]

    # Store in database
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY,
            ref_id TEXT,
            city TEXT,
            area TEXT,
            street TEXT,
            issue TEXT,
            email TEXT
        )
    """)
    c.execute("INSERT INTO issues (ref_id, city, area, street, issue, email) VALUES (?, ?, ?, ?, ?, ?)",
              (ref_id, city, area, street, issue, email))
    conn.commit()
    conn.close()

    # ---------- Send confirmation email ----------
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Smart City Issue Confirmation'
        msg['From'] = 'your-email@gmail.com'          # <-- replace with your Gmail
        msg['To'] = email
        msg.set_content(f"""
        Hello,

        Thank you for reporting an issue in your city.
        Your Reference ID is: {ref_id}

        Details:
        City: {city}
        Area: {area}
        Street: {street}
        Issue: {issue}

        Smart City Team
        """)

        # Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('lakshmiparvathibudda@gmail.com', 'mbdi dvhk zsun krfc')  # <-- use app password here
            smtp.send_message(msg)

    except Exception as e:
        print("Error sending email:", e)

    # Show Reference ID on page
    return f"""
    <h2>Issue submitted successfully!</h2>
    <p>Your Reference ID is: <b>{ref_id}</b></p>
    <p>Check your email ({email}) for confirmation!</p>
    <p><a href='/'>Submit another issue</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)


