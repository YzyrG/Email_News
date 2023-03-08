"""
Send news to email
"""

import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.utils import formataddr


# 创建email格式
def create_email(news_source, news):
    msg = MIMEText(news, 'plain', 'utf-8')
    msg["From"] = formataddr(("My News App", "15683966878@163.com"))
    msg["To"] = formataddr(("ZYR", "2456327328@qq.com"))
    msg['Subject'] = f"Check out fresh faience news from {news_source}"
    return msg


def send_email(message):
    # 使用163邮箱作为SMTP服务器
    host = "smtp.163.com"
    port = 465

    # 发件人账号信息
    sender = "15683966878@163.com"
    password = os.getenv("PASSWORD")

    # 收件人账号
    receiver = "2456327328@qq.com"

    # 返回一个新的带有安全默认设置的上下文
    context = ssl.create_default_context()

    # 使用安全加密的SSL协议连接到SMTP服务器
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


