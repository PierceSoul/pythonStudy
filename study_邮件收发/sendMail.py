#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.mime.image import MIMEImage
import smtplib
'''
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''
#第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性

# 	smtp.qq.com
#ebvjlibresuviedi
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def sendMail(msg):
    from_addr = "1546307458@qq.com"
    password = "ebvjlibresuviedi"
    to_addr = "122982134@qq.com"
    smtp_server = "smtp.qq.com"
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def sendPlain():
    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    sendMail(msg)
def sendHtml():
    msg = MIMEText('''
        <html><body><h1>Hello</h1>
        <p>send by <a href="http://www.liaoxuefeng.com">Python</a>...</p>
        </body></html>
    '''
    , 'html', 'utf-8')
    sendMail(msg)
def sendFile():
    msg = MIMEMultipart()
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('C:/Users/Administrator/Desktop/1.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpg', filename='1.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='1.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    sendMail(msg)
#要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，
# 先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
# 如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
def sendImg():
    msg = MIMEMultipart()
    msg.attach(MIMEText('''
        <html><body><h1>Hello</h1>
        <p>send by <img src="cid:1" />...</p>
        </body></html>

    ''', 'html', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:

    # 定义图片 ID，在 HTML 文本中引用
    with open('C:/Users/Administrator/Desktop/1.jpg', 'rb') as f:
        # 加上必要的头信息:
        mime = MIMEImage(f.read())
        mime.add_header('Content-ID', '<1>')
        msg.attach(mime)

    sendMail(msg)
sendImg()
