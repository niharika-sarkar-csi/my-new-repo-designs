from email.message import EmailMessage
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import os

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def gmail_authenticate():
    creds = None

    # Load token.json if it exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Authenticate if no valid credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # AUTHENTICATION using credentials.json
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save token for next time
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def send_gmail_api_email(sender, receiver, subject, message_text):
    service = gmail_authenticate()  # ← FIXED (no arguments)

    email = EmailMessage()
    email["To"] = receiver
    email["From"] = sender
    email["Subject"] = subject
    email.set_content(message_text)

    encoded_message = base64.urlsafe_b64encode(email.as_bytes()).decode()

    send_message = {"raw": encoded_message}

    service.users().messages().send(
        userId="me",
        body=send_message
    ).execute()

    print("Email sent using Gmail API!")


# -------------------------
# Example call to send email
# -------------------------
send_gmail_api_email(
    sender="niharikaofficial.2023@gmail.com",
    receiver="dhruvrana4244@gmail.com",
    subject="Regarding Internship",
    message_text=(
        "Hi,\n\n"
        "I hope this message finds you well.\n"
        "I am writing to express my interest in the internship opportunity.\n\n"
        "Thank you for considering my application.\n"
        "Warm regards,\nNiharika"
    )
)
