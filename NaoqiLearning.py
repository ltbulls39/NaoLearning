from naoqi import ALProxy
from ftplib import FTP
import paramiko
import time
import globals
from talking_examples import justStand


def getPictures(files):
	for thing in files:
		ftp.retrbinary("RETR %s" % (thing), open(thing, "wb").write)

port = 9559
IP = "192.168.1.104"

transport = paramiko.Transport((IP, port))
user = 'username'
passw = 'password'

transport.connect(username=user, password=passw)
