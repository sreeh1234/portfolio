from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP server
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'sreehapzzz@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'whev ecco krlz qknk'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = ('sreehapzzz@gmail.com')  # Sender info

mail = Mail(app)

@app.route('/')
def index():
    # Renders the home page
    return render_template('index.html')

@app.route('/contact_me', methods=['POST'])
def contact_me():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create email message
        msg = Message(
            subject="Contact Form Submission",
            recipients=['sreehapzzz@gmail.com'],  # Recipient email
            body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
        )
        print(name,email,message)
        try:
            mail.send(msg)  # Send the email
            flash("!! Thank You for your response. I will connect with you ASAP !!", "success")
        except Exception as e:
            print(f"Error: {e}")
            flash("Failed to send message. Please try again.", "danger")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
