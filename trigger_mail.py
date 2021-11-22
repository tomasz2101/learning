from email import message
import os
import sys
import logging
import argparse
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTP():
    def __init__(self,  username: str, password: str, address: str = "smtp.gmail.com", port: int = 587):
        self.address = address
        self.port = port
        self.username = username
        self.password = password

    def build_msg(self, receiver: str, message: str, title: str) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = receiver
        msg['Subject'] = title
        msg.attach(MIMEText(message, 'plain'))

        return msg

    def send(self, msg: MIMEMultipart) -> dict:
        if not msg:
            logging.error("Please firstly use build_msg function.")
            exit(1)

        result = {}
        session = smtplib.SMTP(self.address, self.port)
        session.starttls(context=ssl.create_default_context())
        session.login(self.username, self.password)
        result = session.sendmail(msg["From"], msg["To"], msg.as_string())
        logging.info("Mail sent.")
        logging.debug("Mail sent result: {}".format(result))

        return result


def setup_logger(log_level: str) -> None:
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(log_level.strip().upper())


def parse_args(args):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-u", "--smtp-username",  help="smtp username")
    parser.add_argument("-p", "--smtp-password",  help="smtp password")
    parser.add_argument("-r", "--receiver", help="Receiver message", required=True)
    parser.add_argument("-t", "--title", help="Title message", required=True)
    parser.add_argument("-m", "--message", help="Mail message", required=True)
    parser.add_argument("-l", "--log-level",  default=os.getenv("LOG_LEVEL", default="info"))

    return parser.parse_args(args)


def main(*arguments):
    args = parse_args(arguments)

    setup_logger(log_level=args.log_level)
    message = args.message
    title = args.title

    smtp = SMTP(username=args.smtp_username, password=args.smtp_password)
    msg = smtp.build_msg(args.receiver, message, title)
    smtp.send(msg)


if __name__ == "__main__":
    main(*(sys.argv[1:]))
