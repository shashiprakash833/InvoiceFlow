import smtplib
from email.message import EmailMessage

def send_email(receiver_email, pdf_path):

    sender_email = "prakashoff46@gmail.com"
    app_password = "okdw knaw pygd dcwb"

    msg = EmailMessage()

    msg["Subject"] = "Your Invoice"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        "Thank you for your order. Please find your invoice attached."
    )

    with open(pdf_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=pdf_path.split("/")[-1]
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    return True