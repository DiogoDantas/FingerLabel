from tkinter import *
import ctypes
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
import os

class Application:
	def __init__(self, master=None):
		self.get_screensize()
		self.path_text = tk.StringVar()
		self.font = ('Arial', '10')
		self.container_1 = Frame(master)
		self.container_1['padx'] = 20
		self.container_1['pady'] = 10
		self.container_1.pack()

		self.container_2 = Frame(master)
		self.container_2['padx'] = 20
		self.container_2['pady'] = 10
		self.container_2.pack()

		self.container_3 = Frame(master)
		self.container_3['padx'] = 20
		self.container_3['pady'] = 10
		self.container_3.pack()

		self.container_4 = Frame(master)
		self.container_4['padx'] = 20
		self.container_4['pady'] = 10
		self.container_4.pack()

		self.label_path = Label(self.container_2, text='Path', font=self.font)
		self.label_path.pack(side=LEFT)

		self.path = Entry(self.container_2, textvariable=self.path_text)
		self.path['width'] = 40
		self.path['font'] = self.font
		self.path.pack(side=LEFT, padx=5)

		self.btnOpen = Button(self.container_2, text='Open', font=self.font, width=4)
		self.btnOpen['command'] = self.open
		self.btnOpen.pack(side=LEFT, padx=10)

		self.label_output = Label(self.container_2, text='Output', font=self.font)
		self.label_output.pack(side=LEFT)

		self.output = Entry(self.container_2)
		self.output['width'] = 40
		self.output['font'] = self.font
		self.output.pack(side=LEFT, padx=5)

		self.btnLoad = Button(self.container_2, text='Load', font=self.font, width=8)
		self.btnLoad['command'] = self.load
		self.btnLoad.pack(side=RIGHT)

		self.image = Label(self.container_3)

		self.btnA = Button(self.container_4, text='A', font=self.font, width=8)
		self.btnA['command'] = self.load
		self.btnA.pack(side=LEFT, padx=10)

		self.btnT = Button(self.container_4, text='T', font=self.font, width=8)
		self.btnT['command'] = self.load
		self.btnT.pack(side=RIGHT, padx=10)

		self.btnL = Button(self.container_4, text='L', font=self.font, width=8)
		self.btnL['command'] = self.load
		self.btnL.pack(side=RIGHT, padx=10)

		self.btnR = Button(self.container_4, text='R', font=self.font, width=8)
		self.btnR['command'] = self.load
		self.btnR.pack(side=RIGHT, padx=10)

		self.btnW = Button(self.container_4, text='W', font=self.font, width=8)
		self.btnW['command'] = self.load
		self.btnW.pack(side=RIGHT, padx=10)


	def get_screensize(self):
		user32 = ctypes.windll.user32
		self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	
	def load(self):
		img = Image.open('cardeal.JPG')
		photo = ImageTk.PhotoImage(img)
		self.image['width'] = 480
		self.image['height'] = 512
		self.image.pack(side=LEFT)
		self.image.configure(image=photo)
		self.image.image = photo

	def open(self):
		folder = filedialog.askdirectory(initialdir='Documents', title='Select a Directory')
		self.files = [folder + '/' + file for file in os.listdir(folder)]
		self.path_text.set(str(folder))
		

def main():
	root = Tk()
	root.title('Fingerprint Types')
	Application(root)
	root.mainloop()

if __name__ == '__main__':
	main()
