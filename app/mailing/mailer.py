from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from sqlalchemy.orm import Session
from ..database import SessionLocalMail
from .. import crud

class Mailer:

    def __init__(self):
        self.server = "smtpdce.brose.net"
        self.sender_email = "calibration.app@brose.com"
        self.msg = MIMEMultipart()

        self._from = None
        self._to = None
        

    def _get_recipients_from_db(self) -> list[str]:
        """Fetch all recipient emails from the mail database"""
        db = SessionLocalMail()
        try:
            recipients = crud.get_all_mail(db)
            return [recipient.email for recipient in recipients]
        finally:
            db.close()

    def send_email(self, subject: str, body: str):
        """Send an email to all recipients in the database with the specified subject and body."""
        recipients = self._get_recipients_from_db()
        if recipients:
            pass
        else:
            print("No recipients found in the database. Email not sent.")
            return
        
        self.msg['From'] = self.sender_email
        self._from = self.sender_email
        self.msg['To'] = ", ".join(recipients)
        self._to = recipients
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.server, 25, timeout=30) as server:
                server.sendmail(self._from, self._to, self.msg.as_string()) #For some reson _from and _to must be used so that the mail is sent, otherwise it won't work.
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
