import time

def recordSound(filename, proxy, num=5):
	proxy.post.startMicrophonesRecording(filename)
	print "We are recording!"
	time.sleep(num)
	print "We are done recording"
	proxy.stopMicrophonesRecording()

def playSound(filename, proxy):
	proxy.playFile(filename)