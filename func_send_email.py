from email.header import Header
from email.mime.text import MIMEText
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
        msg = MIMEText(string, 'html', 'utf-8')
        msg['From'] = _format_addr('Love_tools Group')
        msg['To'] = _format_addr('Recipient <%s>' % to_addr)
        msg['Subject'] = Header('Test text~~~', 'utf-8').encode()

        smtp_server = 'smtp.gmail.com'

        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        time.sleep(3)
        server.quit()



email_list = ['trihesdlin@163.com']
string = '<html><body><h1>Today\' summary</h1>' + \
         '<p>You can search it by yourself on <a href="http://www.google.com" target = "_blank">Google</a> XD</p>' + \
         '</body></html>'
send_email(string,email_list)
