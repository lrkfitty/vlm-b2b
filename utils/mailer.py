import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NOTIFY        = "tylarkin@vlmcreateflow.com"
NOTIFY_GMAIL  = "virallensemediavlm@gmail.com"
USER          = os.getenv("SMTP_USER", "noreply@vlmcreateflow.com")
PASS          = os.getenv("SMTP_PASS", "PLACEHOLDER")


def _send(subject: str, body: str, to: str):
    if PASS == "PLACEHOLDER":
        print(f"[EMAIL PLACEHOLDER] To: {to} | {subject}")
        return
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = USER
    msg["To"]      = to
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP("mail.privateemail.com", 587) as s:
            s.starttls(); s.login(USER, PASS); s.sendmail(USER, to, msg.as_string())
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")


def send_lead_notification(lead: dict):
    body = f"""New B2B Lead — CreateFlow Enterprise

Name:      {lead.get('name')}
Company:   {lead.get('company')}
Role:      {lead.get('role')}
Email:     {lead.get('email')}
Niche:     {lead.get('niche')}
Budget:    {lead.get('budget')}
Challenge: {lead.get('challenge')}
Team Size: {lead.get('team_size')}
Lead ID:   {lead.get('id')}
"""
    subject = f"New B2B Lead — {lead.get('name')} @ {lead.get('company')}"
    _send(subject, body, NOTIFY)
    _send(subject, body, NOTIFY_GMAIL)


def send_booking_notification(booking: dict):
    body = f"""New Setup Call Booking — VLM

Name:        {booking.get('name')}
Email:       {booking.get('email')}
Company:     {booking.get('company')}
Availability:{booking.get('availability')}
Message:     {booking.get('message')}
"""
    subject = f"Setup Call Request — {booking.get('name')} @ {booking.get('company')}"
    _send(subject, body, NOTIFY_GMAIL)
    _send(subject, body, NOTIFY)
