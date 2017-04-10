import math
import pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.      

#See http://www.phy.mtu.edu/~suits/notefreqs.html
LENGTH = 0.3 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
# RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

##fill remainder of frameset with silence
# for x in xrange(RESTFRAMES): 
#  WAVEDATA = WAVEDATA+chr(128)

#14159265358979323846264338327950288419716939937510582

def READ_SEQ(path):
	res = []
	with open(path, 'r') as f:
		for line in f:
			res.append(int(line))
	return res


def MY_FREQ(digit):
	return {
		0: 1174.66,
		1: 1318.51, 
		2: 1479.98,
		3: 1567.98,
		4: 1760.00,
		5: 1975.53}.get(digit, -1)


def ADD_SOUND(digit):
	global WAVEDATA
	for x in xrange(NUMBEROFFRAMES):
		WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/MY_FREQ(digit))/math.pi))*127+128))
	return    

if __name__ == "__main__":
	seq = READ_SEQ('seq/02.txt')
	for i in seq:
		sound = int(i)%6
		print(sound)
		ADD_SOUND(sound)

	p = PyAudio()
	stream = p.open(format = p.get_format_from_width(1), 
	                channels = 1, 
	                rate = BITRATE, 
	                output = True)
	stream.write(WAVEDATA)
	stream.stop_stream()
	stream.close()
	p.terminate()
