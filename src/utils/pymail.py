#!/usr/bin/env python3
import configparser
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import os

charset = 'utf-8'
mail_config_location = 'src/configs/python-mail.cfg'

config = configparser.ConfigParser()
config.read(mail_config_location)
default_tos = config.get('devops', 'to').split(',')
default_cc = config.get('devops', 'cc')


class MailAPI(object):
    def __init__(self):
        self.user = config.get('devops', 'user')
        self.password = config.get('devops', 'password')
        self.host = config.get('devops', 'host')
        self.port = config.getint('devops', 'port')
        self.local_hostname = config.get('devops', 'local_hostname')
        self.charset = config.get('devops', 'charset')
        self.mail_sender = None

    def connect(self, ssl: bool = True):
        if ssl:
            self.mail_sender = smtplib.SMTP_SSL(self.host, self.port, self.local_hostname, timeout=5)
        else:
            self.mail_sender = smtplib.SMTP(self.host, self.port, self.local_hostname, timeout=5)
        self.mail_sender.login(self.user, self.password)
        return self

    def quit(self):
        self.mail_sender.quit()

    def close(self):
        self.mail_sender.close()

    def send_content(self, from_addr: str, to_addrs: list, msg: str, mail_options=(),
                     rcpt_options=()):
        if self.mail_sender is None:
            self.connect()
        try:
            self.mail_sender.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=msg,
                                      mail_options=mail_options,
                                      rcpt_options=rcpt_options)
        except smtplib.SMTPException as e:
            print('ERROR: send mail failed, e:', e)
            self.close()
            return False
        finally:
            self.quit()
        return True

    def send(self, from_addr: str, to_addrs: list, msg_content: str, subject: str, _from: str, to: list,
             cc: list = None,
             _type: str = 'plain',
             mail_options=(),
             rcpt_options=()):
        message = MIMEText(msg_content, _type, self.charset)
        message['From'] = _from
        message['To'] = ', '.join(to)
        if cc is not None:
            message['Cc'] = ', '.join(cc)
        message['Subject'] = subject
        return self.send_content(from_addr=from_addr, to_addrs=to_addrs, msg=message.as_string(),
                                 mail_options=mail_options,
                                 rcpt_options=rcpt_options)

    def send_default(self, to_addrs: list, msg_content: str, subject: str,
                     cc: list = None,
                     _type: str = 'plain',
                     mail_options=(),
                     rcpt_options=()):
        self.send(from_addr=self.user, to_addrs=to_addrs, msg_content=msg_content, subject=subject, _from=self.user,
                  to=to_addrs, cc=cc, _type=_type, mail_options=mail_options, rcpt_options=rcpt_options
                  )

    class GenericSender:
        def __init__(self, mail_api, subject: str, to: list, cc: list = None):
            self.mail_api = mail_api
            self._from = mail_api.user
            self.to = to
            message = MIMEMultipart('mixed')
            message['From'] = mail_api.user
            message['To'] = ', '.join(to)
            if cc is not None:
                message['Cc'] = ', '.join(cc)
            message['Subject'] = subject
            self.message = message

        def add_text(self, content: str, _type: str = 'plain'):
            self.message.attach(MIMEText(content, _type, charset))
            return self

        def add_image(self, image_file_path: str, image_id: str):
            fp = open(image_file_path, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', f'<{image_id}>')
            self.message.attach(msgImage)
            return self

        def add_image_base64str(self, image_base64_bytes: str, image_id: str):
            msgImage = MIMEImage(image_base64_bytes, _subtype='JPEG')
            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', f'<{image_id}>')
            self.message.attach(msgImage)
            return self

        def add_file(self, file_path: str):
            email_file = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
            email_file["Content-Type"] = 'application/octet-stream'
            file_name = os.path.basename(file_path)
            email_file.add_header("Content-Disposition", "attachment", filename=file_name)
            self.message.attach(email_file)
            return self

        def send(self, from_addr: str, to_addrs: list,
                 mail_options=(),
                 rcpt_options=()):
            return self.mail_api.send_content(from_addr=from_addr, to_addrs=to_addrs, msg=self.message.as_string(),
                                              mail_options=mail_options,
                                              rcpt_options=rcpt_options)

        def send_default(self,
                         mail_options=(),
                         rcpt_options=()):
            return self.mail_api.send_content(from_addr=self._from, to_addrs=self.to, msg=self.message.as_string(),
                                              mail_options=mail_options,
                                              rcpt_options=rcpt_options)
