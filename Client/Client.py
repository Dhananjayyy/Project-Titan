import cv2
import io
import socket
import struct
import time
import pickle
import zlib
#from buzzer_module import beep
from motor import Motor
car = Motor()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('Morpheus', 8485))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

try:
	while True:
		s, frame = cam.read()
		result, frame = cv2.imencode('.jpg', frame, encode_param)
		data = zlib.compress(pickle.dumps(frame, 0))
		data = pickle.dumps(frame, 0)
		size = len(data)
		client_socket.sendall(struct.pack(">L", size) + data)
		img_counter += 1
		recvd_data = client_socket.recv(1024)
		data1 = pickle.loads(recvd_data)
		print('.')
		if data1[0] == 1:
			car.forward()
		'''if data1[0] == 0:
			car.stop()'''
			#beep(0.1,1)
		car.stop()
		print(data1[0])
except:
	print('Stream disconnected')

cam.release()
