#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twilio.rest import Client
import os
import smtplib 
from email.message import EmailMessage


# In[2]:


class whatsapp_msg:
    def __init__(self, acc_sid, acc_token):
        self.acc_sid = acc_sid
        self.acc_token = acc_token
    def send_msg(self, msg):
        client = Client(self.acc_sid,self.acc_token)
        message = client.messages.create(
                              body = msg,
                              from_ = 'whatsapp:+14155238886',
                              to = 'whatsapp:+919601153415',
                          )
        return message


# In[3]:


class email_msg:
    def __init__(self, content, frm, to, passwd):
        self.content = content
        self.frm = frm
        self.to = to
        self.password = passwd
    def send_msg(self):
        msg = EmailMessage()
        msg.set_content(self.content)
        msg["subject"] = "FACE DETECTED" 
        msg["to"] = self.to
        msg["from"] = self.frm
        password = self.password
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(self.frm,self.password)
        server.send_message(msg)
        server.quit()
        return "Sent Successful"


# In[ ]:




