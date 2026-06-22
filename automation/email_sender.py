import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")

def send_email(receiver_email, pdf_path):

```
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": [receiver_email],
    "subject": "Your Invoice",
    "html": "<p>Thank you for your order. Please find your invoice attached.</p>",
    "attachments": [
        {
            "filename": pdf_path.split("/")[-1],
            "content": pdf_bytes
        }
    ]
})

return True
```
