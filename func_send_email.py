from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import time

def send_email(string,email_list):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'welovetoolsandpaul@gmail.com'
    password = 'welovepaul2018'

    for to_addr in email_list:
        msg = MIMEMultipart()
        msg['From'] = _format_addr('Love_tools Group')
        msg['To'] = _format_addr('Recipient <%s>' % to_addr)
        msg['Subject'] = Header('Test text~~~', 'utf-8').encode()

        msg.attach(MIMEText(string, 'html', 'utf-8'))
        with open('/Users/trihesdlin/Pictures/pic_eg.png','rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename='summary.png')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='summary.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)

        smtp_server = 'smtp.gmail.com'

        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        time.sleep(1)
        server.quit()



email_list = ['trihesdlin@163.com']
input_string = """
<html>
<body>
<h1>Today\' summary</h1>
<div class="summary">
<p>
<font size=5>You can search it by yourself on Google XD</font><br /><br />
<img src="cid:0" width="60%">
</p>
</div>
</body>
</html>
"""
send_email(input_string,email_list)
