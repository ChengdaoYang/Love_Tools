def send_email(string,email_list):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'welovetoolsandpaul@gmail.com'
    password = 'welovepaul2018'
    pic_list = re.findall(r'img class\=\"[a-zA-z0-9-]+',string)
    test = pic_list[0][11:]

    for to_addr in email_list:
        msg = MIMEMultipart()
        msg['From'] = _format_addr('Love_tools Group')
        msg['To'] = _format_addr('Recipient <%s>' % to_addr)
        msg['Subject'] = Header('Test text~~~', 'utf-8').encode()

        msg.attach(MIMEText(string, 'html', 'utf-8'))
        for i in range(len(pic_list)):
            with open(pic_list[i][11:]+'.png','rb') as fp:
                mime = MIMEBase('image', 'png', filename=pic_list[i][11:]+'.png')
                mime.add_header('Content-Disposition', 'attachment', filename=pic_list[i][11:]+'.png')
                mime.add_header('Content-ID', '<'+str(2*i)+'>')
                mime.add_header('X-Attachment-Id', str(2*i))
                mime.set_payload(fp.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
            with open(pic_list[i][11:]+'-price.png','rb') as f:
                mime = MIMEBase('image', 'png', filename=pic_list[i][11:]+'-price.png')
                mime.add_header('Content-Disposition', 'attachment', filename=pic_list[i][11:]+'-price.png')
                mime.add_header('Content-ID', '<'+str(2*i+1)+'>')
                mime.add_header('X-Attachment-Id', str(2*i+1))
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)

        smtp_server = 'smtp.gmail.com'

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        time.sleep(1)
        server.quit()
