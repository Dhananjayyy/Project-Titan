import cv2
import socket
import struct
import pickle
import zlib
#from buzzer_module import beep
from manual import Manual
import curses
from time import sleep

class Engine(Manual):
	def __init__(self):
		super().__init__()
		self.cam = cv2.VideoCapture(0)
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
		try:
			self.client_socket.connect(('Morpheus', 8485))
		except:
			print('Connection refused')
			print('Quitting')
			sleep(2)
			curses.endwin()
			quit()
		self.cam.set(3, 320)
		self.cam.set(4, 240)

	def transmission(self):
		n = curses.initscr()
		print("Press 'a' for Automatic, 'm' for Manual and 'q' to quit")
		while True:
			key = n.getch()
			if key == ord('a'):
				print('Automatic Drive Enabled')
				self.run()
			elif key == ord('m'):
				print('Manual Drive Enabled')
				self.drive()
			elif key == ord('q'):
				print('Exit')
				self.screen.keypad(0)
				curses.endwin()
				break

	def data_transfer(self,frame):
		data = pickle.dumps(frame, 0)
		size = len(data)
		self.client_socket.sendall(struct.pack(">L", size) + data)
		recvd_data = self.client_socket.recv(1024)
		data = pickle.loads(recvd_data)
		return data

	def camera(self):
		s, frame = self.cam.read()
		result, frame = cv2.imencode('.jpg', frame, self.encode_param)
		return frame

	def run(self):
		try:
			while True:
				frame = self.camera()
				data = self.data_transfer(frame)
				if data[0] == 1:
					self.start()
					self.forward()
				if data[0] == 0:
					self.stop()
					#beep(0.1,1)
				#car.stop()
				#print(data[0])
		finally:
			self.cam.release()
			curses.endwin()
			#cv2.destroyAllWindows()

if __name__ == '__main__':
    engine = Engine()
    engine.transmission()
