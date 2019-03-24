import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send(m):
    msg = MIMEText(m, 'plain', 'utf-8')

    from_addr = '****'
    password = '***'
    auth_code = '***'
    to_addr = '***'
    SMTP_Server = 'smtp.qq.com'

    msg['From'] = _format_addr('爬虫云服务 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('爬虫出问题啦', 'utf-8').encode()


    server = smtplib.SMTP(SMTP_Server, 25)
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_addr, auth_code)

    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
