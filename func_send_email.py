from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

def send_email(company,email_list):

    def get_string(company):

        company.summary(save_plot=True)
        company.price(plot = True)
        main_string = """
        <html>
        <body>
        <h1>Summary</h1>
        <p>
        <font size=5 color="sky blue">"""

        #function to create html string format for nice looking email
        main_string = main_string + company.ticker + \
                      '</font>\n<br /><br />\n<font size=4>' + \
                      'This is the summary of ' + company.ticker + \
                      '</font>\n<br />\n<font size=4>' + \
                      company.summary + \
                      '</font>\n<br /><br />\n' + \
                      '<img src="cid:' + \
                      '0' + \
                      '" width="60%">\n<br /><br />\n' + \
                      '<font size=4>' + \
                      'The latest prices of ' + company.ticker + ' are:' + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Opening Price: ' + str(round(company.price(plot = True)['Open'].values[0],2)) + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Closing Price: ' + str(round(company.price(plot = True)['Close'].values[0],2)) + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Highest Price: ' + str(round(company.price(plot = True)['High'].values[0],2)) + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Lowest Price: ' + str(round(company.price(plot = True)['Low'].values[0],2)) + \
                      '</font>\n<br /><br />\n<img class="' + \
                      company.ticker + \
                      '" src="cid:' + \
                      '1' + \
                      '" width="60%">\n<br /><br />\n<font size=5 color="sky blue">'
        main_string = main_string + '\n</p>\n</div>\n</body>\n</html>\n'
        print(main_string)
        time.sleep(5)
        return main_string
    
    text = get_string(company)
    #formmating
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    #account & password of the sender's email, use them to send email
    from_addr = 'welovetoolsandpaul@gmail.com'
    password = 'welovepaul2018'

    pic_list = re.findall(r'img class\=\"[a-zA-z0-9-]+',text)
    test = pic_list[0][11:]

    #loop to send emails to multiple users
    for to_addr in email_list:
        #create email
        msg = MIMEMultipart()
        msg['From'] = _format_addr('Love_tools Group')
        msg['To'] = _format_addr('Recipient <%s>' % to_addr)
        msg['Subject'] = Header('Test text~~~', 'utf-8').encode()

        #adding attachment
        msg.attach(MIMEText(text, 'html', 'utf-8'))
        for i in range(len(pic_list)):
            #add word could pic
            with open(pic_list[i][11:]+'.png','rb') as fp:
                mime = MIMEBase('image', 'png', filename=pic_list[i][11:]+'.png')
                mime.add_header('Content-Disposition', 'attachment', filename=pic_list[i][11:]+'.png')
                mime.add_header('Content-ID', '<'+str(2*i)+'>')
                mime.add_header('X-Attachment-Id', str(2*i))
                mime.set_payload(fp.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
            #add price chart pic
            with open(pic_list[i][11:]+'_price.png','rb') as f:
                mime = MIMEBase('image', 'png', filename=pic_list[i][11:]+'_price.png')
                mime.add_header('Content-Disposition', 'attachment', filename=pic_list[i][11:]+'_price.png')
                mime.add_header('Content-ID', '<'+str(2*i+1)+'>')
                mime.add_header('X-Attachment-Id', str(2*i+1))
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)

        #email host server address
        smtp_server = 'smtp.gmail.com'

        #send email
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        time.sleep(1)
        #quiting the email server after sending the email
        server.quit()
    return None


