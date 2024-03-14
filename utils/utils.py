import imaplib
import email
import time


def get_security_code(email_address, password, timeout=5):

    time.sleep(timeout)

    # IMAP sunucusuna bağlan
    mail = imaplib.IMAP4_SSL('imap.outlook.com')  # IMAP sunucusunun adresine ve SSL bağlantı noktasına bağlanın
    mail.login(email_address, password)  # E-posta adresinizi ve şifrenizi girin

    # Inbox'e eriş
    mail.select('inbox')

    # E-postaları ara ve filtrele
    result, data = mail.search(None, '(SUBJECT "Your EA security Code")')  # Belirli bir konuyla e-postaları filtrele
    latest_email_id = data[0].split()[-1]  # En son gelen e-postanın ID'sini al

    # En son gelen e-postayı al
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    # E-postanın içeriğini al
    subject = email_message['subject']

    code = subject[-6:]


    mail.close()
    mail.logout()

    return code
