import pandas as pd
import email
import smtplib


class MailSpam(object):
    def __init__(self, data, participants_list):
        self.data = data
        self.participants_list = participants_list
        self.server = "cloudmail103.zonecybersite.com"
        self.user = "bbb.ylt@osg.sg"
        self.password = "Borders@2022"

    def send_data(self):
        to = ""
        for arg in self.participants_list:
            to += arg + ","
        server = smtplib.SMTP(self.server)
        server.login(self.user, self.password)
        body = "\r\n".join((
            "From: %s" % self.user,
            "To: %s" % to[:len(to)-1],
            "Subject: test",
            "",
            self.data
        ))

        for i in range(0, len(self.participants_list)):
            server.sendmail(self.user, self.participants_list, body)
        server.quit()


text = "Hello World"

data = pd.read_excel("Test.xlsx", header=None).values.tolist()
res = []
for arg in data:
    res.append(arg[0])
print(res)
participants_list = res
test = MailSpam(text, participants_list)
test.send_data()




