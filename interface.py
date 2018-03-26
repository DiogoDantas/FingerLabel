from tkinter import *
import ctypes
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
import os
from shutil import copyfile

class Application:
	def __init__(self, master=None):
		self.get_screensize()
		self.path_text = tk.StringVar()
		self.count_A = tk.StringVar()
		self.count_T = tk.StringVar()
		self.count_L = tk.StringVar()
		self.count_R = tk.StringVar()
		self.count_W = tk.StringVar()
		self.current_image = ''
		self.fingertypes = ['A', 'T', 'L', 'R', 'W']
		self.font = ('Arial', '10')
		self.container_1 = Frame(master)
		self.container_1.grid(padx=20, pady=10)

		self.container_2 = Frame(master)
		self.container_2['padx'] = 20
		self.container_2['pady'] = 10
		self.container_2.grid(padx=20, pady=10)

		self.container_3 = Frame(master)
		self.container_3['padx'] = 20
		self.container_3['pady'] = 10
		self.container_3.grid(padx=20, pady=10)

		self.container_4 = Frame(master)
		self.container_4['padx'] = 20
		self.container_4['pady'] = 10
		self.container_4.grid(padx=20, pady=10)

		self.label_path = Label(self.container_1, text='Path', font=self.font)
		self.label_path.grid(row=0, column=0, padx=5)
		
		self.path = Entry(self.container_1, textvariable=self.path_text)
		self.path['width'] = 100
		self.path['font'] = self.font
		self.path.grid(row=0, column=1)

		self.btnOpen = Button(self.container_1, text='Open', font=self.font, width=4)
		self.btnOpen['command'] = self.open
		self.btnOpen.grid(row=0, column=2, padx=10)

		self.btnA = Button(self.container_2, text='A', font=self.font, width=8)
		self.btnA['command'] = self.type_A
		self.btnA.grid(row=0, column=1, padx=5, pady=10)

		self.btnT = Button(self.container_2, text='T', font=self.font, width=8)
		self.btnT['command'] = self.type_T
		self.btnT.grid(row=0, column=2, padx=5, pady=10)

		self.btnL = Button(self.container_2, text='L', font=self.font, width=8)
		self.btnL['command'] = self.type_L
		self.btnL.grid(row=0, column=3, padx=5, pady=10)

		self.btnR = Button(self.container_2, text='R', font=self.font, width=8)
		self.btnR['command'] = self.type_R
		self.btnR.grid(row=0, column=4, padx=5, pady=10)

		self.btnW = Button(self.container_2, text='W', font=self.font, width=8)
		self.btnW['command'] = self.type_W
		self.btnW.grid(row=0, column=5, padx=5, pady=10)

		self.label_count_A = Label(self.container_2, textvariable=self.count_A, font=self.font)
		self.label_count_A.grid(row=1, column=1, padx=10)

		self.label_count_T = Label(self.container_2, textvariable=self.count_T, font=self.font)
		self.label_count_T.grid(row=1, column=2, padx=10)

		self.label_count_L = Label(self.container_2, textvariable=self.count_L, font=self.font)
		self.label_count_L.grid(row=1, column=3, padx=10)

		self.label_count_R = Label(self.container_2, textvariable=self.count_R, font=self.font)
		self.label_count_R.grid(row=1, column=4, padx=10)

		self.label_count_W = Label(self.container_2, textvariable=self.count_W, font=self.font)
		self.label_count_W.grid(row=1, column=5, padx=10)

		self.image = Label(self.container_3)
		self.image.grid(row=0, column=1, padx=40)

		self.listbox = Listbox(self.container_3, width=30, height=30)
		scrollbar = Scrollbar(self.container_3, orient=VERTICAL)
		scrollbar.grid(row=0, column=0, sticky=E+N+S)
		self.listbox.config(yscrollcommand=scrollbar.set)
		scrollbar.config(command=self.listbox.yview)
		self.listbox.bind('<<ListboxSelect>>', self.onselect)
		self.listbox.grid(row=0, column=0)


	def get_screensize(self):
		user32 = ctypes.windll.user32
		self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

	def load_image(self, path):
		print(path)
		self.current_image = path
		img = Image.open(self.current_image)
		photo = ImageTk.PhotoImage(img)
		return photo

	def set_image(self, path):
		photo = self.load_image(path)
		self.image.configure(image=photo)
		self.image.image = photo

	def onselect(self, evt):
		w = evt.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		path = self.path.get() + '/' + value
		self.current_image = path
		self.set_image(path)

	def open(self):
		self.listbox.delete(0, END)
		folder = filedialog.askdirectory(initialdir='Documents', title='Select a Directory')
		self.output_path = os.path.join(folder, 'output')
		self.files = [folder + '/' + file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
		self.path_text.set(str(folder))
		if not os.path.exists(os.path.join(folder, 'output')):
			os.makedirs(os.path.join(folder, 'output/A'))
			os.mkdir(os.path.join(folder, 'output/T'))
			os.mkdir(os.path.join(folder, 'output/L'))
			os.mkdir(os.path.join(folder, 'output/R'))
			os.mkdir(os.path.join(folder, 'output/W'))
		for file in self.files:
			self.listbox.insert(END, file[file.rfind('/')+1:])

		self.set_image(self.files[0])
		self.update_count()

	def check(self):
		output = os.path.join(self.path_text.get(), 'output')
		file = self.current_image[self.current_image.rfind('/')+1:]
		if os.path.exists(output):
			for fingertype in self.fingertypes:
				if os.path.exists(os.path.join(os.path.join(output, fingertype), file)):
					os.remove(os.path.join(os.path.join(output, fingertype), file))
			
	def update_count(self):
		output = os.path.join(self.path_text.get(), 'output')
		file = self.current_image[self.current_image.rfind('/')+1:]
		if os.path.exists(output):
			count = [len(os.listdir(os.path.join(os.path.join(output, fingertype)))) for fingertype in self.fingertypes]
			self.count_A.set(str(count[0]))
			self.count_T.set(str(count[1]))
			self.count_L.set(str(count[2]))
			self.count_R.set(str(count[3]))
			self.count_W.set(str(count[4]))



	def type_A(self):
		des = os.path.join(self.output_path, 'A')
		self.check()
		copyfile(self.current_image, os.path.join(des, self.current_image[self.current_image.rfind('/')+1:]))
		self.update_count()

	def type_T(self):
		des = os.path.join(self.output_path, 'T')
		self.check()
		copyfile(self.current_image, os.path.join(des, self.current_image[self.current_image.rfind('/')+1:]))
		self.update_count()

	def type_L(self):
		des = os.path.join(self.output_path, 'L')
		self.check()
		copyfile(self.current_image, os.path.join(des, self.current_image[self.current_image.rfind('/')+1:]))
		self.update_count()

	def type_R(self):
		des = os.path.join(self.output_path, 'R')
		self.check()
		copyfile(self.current_image, os.path.join(des, self.current_image[self.current_image.rfind('/')+1:]))
		self.update_count()

	def type_W(self):
		des = os.path.join(self.output_path, 'W')
		self.check()
		copyfile(self.current_image, os.path.join(des, self.current_image[self.current_image.rfind('/')+1:]))
		self.update_count()

def main():
	root = Tk()
	root.title('Fingerprint Types')
	Application(root)
	root.mainloop()

if __name__ == '__main__':
	main()
