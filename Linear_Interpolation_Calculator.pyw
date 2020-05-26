''' 
"Linear Interpolation Calculator" is an application with graphical user interface developed using Python and mainly tkinter module.
It lets users find value y3 at x3 by using linear interpolation method, if there are two points of known values and (x3, y3) is located between them.

Author: Krzysztof Wowczeniuk.
'''

from tkinter import Tk
from tkinter import Frame
from tkinter import font
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import messagebox
import webbrowser
import platform
import subprocess

class linear_interpolation_calc(object):
	'''
	A class with a tkinter user interface to enter data to make linear interpolation between two values.
	Call the display function to display the main window of application on the screen.
	'''

	def display(self):
		'''
		Displays the window of "Linear Interpolation Calculator".
		When the window is closed, this method completes.
		'''

		root = Tk()
		root.resizable(width = False, height = False)
		root.title('Linear Interpolation Calculator')

		def open_link():
			webbrowser.open_new_tab('https://github.com/krzwow/')

		frame0 = Frame(root)
		font_hyperlink = font.Font(underline = 1,  size = 9)
		hyperlink = Button(frame0, text = 'GitHub', command = open_link, fg = 'blue', cursor = 'hand2', borderwidth = 0,\
			 relief = 'sunken', font = font_hyperlink)
		hyperlink.grid(sticky = 'E', row = 0, column = 0, padx = 5, pady = 5)
		frame0.grid(sticky = 'E'+'N', row = 0, column = 0, padx = 5, pady = 5, columnspan = 3)

		frame1 = Frame(root)
		x12_label = Label(frame1, text = 'x1 and x2')
		x12_label.grid(sticky = 'W', row = 0, column = 0, padx = 5, pady = 5)

		x1_entry = Entry(frame1, width = 18)
		x1_entry.grid(sticky = 'W', row = 1, column = 0, padx = 5, pady = 5)

		x2_entry = Entry(frame1, width = 18)
		x2_entry.grid(sticky = 'W', row = 2, column = 0, padx = 5, pady = 5)

		x3_label = Label(frame1, text = 'x3')
		x3_label.grid(sticky = 'W', row = 3, column = 0, padx = 5, pady = 5)

		x3_entry = Entry(frame1, width = 18)
		x3_entry.grid(sticky = 'W', row = 4, column = 0, padx = 5, pady = 5)
		frame1.grid(sticky = 'W'+'N', row = 1, column = 0, padx = 5, pady = 5)

		frame2 = Frame(root)
		y12_label = Label(frame2, text = 'y1 and y2')
		y12_label.grid(sticky = 'W', row = 0, column = 0, padx = 35, pady = 5)

		y1_entry = Entry(frame2, width = 18)
		y1_entry.grid(sticky = 'W', row = 1, column = 0, padx = 35, pady = 5)

		y2_entry = Entry(frame2, width = 18)
		y2_entry.grid(sticky = 'W', row = 2, column = 0, padx = 35, pady = 5)

		answer_label = Label(frame2, text = 'y3')
		answer_label.grid(sticky = 'W', row = 3, column = 0, padx = 35, pady = 5)

		answer_entry = Entry(frame2, width = 16)
		answer_entry.config(state = 'readonly', readonlybackground = 'white', font = 'TkDefaultFont 9 bold')
		answer_entry.grid(sticky = 'W', row = 4, column = 0, padx = 35, pady = 5)
		frame2.grid(sticky = 'W'+'N', row = 1, column = 1, padx = 5, pady = 5)

		frame3 = Frame(root)
		notation_label = Label(frame3, text = 'Exponent of base 10', width = 15)
		notation_label.grid(sticky = 'W', row = 0, column = 0, padx = 5, pady = 3, columnspan = 2)

		notation_x123_label = Label(frame3, text = 'For x1, x2 and x3')
		notation_x123_label.grid(sticky = 'W', row = 1, column = 0, padx = 5, pady = 6, columnspan = 2)

		notation_x123_10_label = Label(frame3, text = '10 ^ ')
		notation_x123_10_label.grid(sticky = 'W', row = 2, column = 0, padx = 5, pady = 3)

		notation_x123_entry = Entry(frame3, width = 3)
		notation_x123_entry.insert(0, '0')
		notation_x123_entry.grid(sticky = 'W', row = 2, column = 1, padx = 5, pady = 3)

		notation_y12_label = Label(frame3, text = 'For y1 and y2')
		notation_y12_label.grid(sticky = 'W', row = 3, column = 0, padx = 5, pady = 6, columnspan = 2)

		notation_y12_10_label = Label(frame3, text = '10 ^ ')
		notation_y12_10_label.grid(sticky = 'W', row = 4, column = 0, padx = 5, pady = 3)

		notation_y12_entry = Entry(frame3, width = 3)
		notation_y12_entry.insert(0, '0')
		notation_y12_entry.grid(sticky = 'W', row = 4, column = 1, padx = 5, pady = 3)
		frame3.grid(sticky = 'W'+'N', row = 1, column = 2, padx = 5, pady = 5)
		frame3.grid_columnconfigure(1, weight = 2)

		frame4 = Frame(root)
		ck1_value = IntVar()
		ck1_value.set(1)
		ck1 = Checkbutton(frame4, text = 'Four significant figures and scientific notation', variable = ck1_value)
		ck1.grid(sticky = 'W', row = 0, column = 0, padx = 5, pady = 2)

		ck2_value = IntVar()
		ck2 = Checkbutton(frame4, text = '"*10^" instead of "e" in scientific notation', variable = ck2_value)
		ck2.grid(sticky = 'W', row = 1, column = 0, padx = 5, pady = 2)

		ck3_value = IntVar()
		ck3 = Checkbutton(frame4, text = 'Replace comma with dot in result', variable = ck3_value)
		ck3.grid(sticky = 'W', row = 2, column = 0, padx = 5, pady = 2)
		frame4.grid(sticky = 'W'+'N', row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)

		frame5 = Frame(root)
		message_label = Label(frame5, text = '\n', font = 'TkDefaultFont 10 bold')
		message_label.grid(row = 0, column = 0, padx = 5, pady = 5)
		frame5.grid(row = 3, column = 0, padx = 5, pady = 5, columnspan = 3)

		def calculate():
			'''
			text
			'''
			x1_str = x1_entry.get()
			x1_str = x1_str.replace(',', '.')
			try:
				x1 = float(x1_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Incorrect value of x1.')
				return
            
			x2_str = x2_entry.get()
			x2_str = x2_str.replace(',', '.')
			try:
				x2 = float(x2_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Incorrect value of x2.')
				return
			
			x3_str = x3_entry.get()
			x3_str = x3_str.replace(',', '.')
			try:
				x3 = float(x3_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Incorrect value of x3.')
				return
			
			if x2 >= x1:
				if x3 >= x2 or x3 <= x1:
					messagebox.showerror(title = 'Value error', message = 'Value of x3 have to be in range (x1, x2).')
					return
			else:
				if x3 >= x1 or x3 <= x2:
					messagebox.showerror(title = 'Value error', message = 'Value of x3 have to be in range (x2, x1).')
					return

			notation_x123_str = notation_x123_entry.get()
			notation_x123_str = notation_x123_str.replace(',', '.')
			try:
				notation_x123 = int(notation_x123_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Value of exponent of base 10 for x1, x2 and x3 have to be an integer.')
				return
            
			notation_y12_str = notation_y12_entry.get()
			notation_y12_str = notation_y12_str.replace(',', '.')
			try:
				notation_y12 = int(notation_y12_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Value of exponent of base 10 for y1 and y2 have to be an integer.')
				return

			y1_str = y1_entry.get()
			y1_str = y1_str.replace(',', '.')
			try:
				y1 = float(y1_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Incorrect value of y1.')
				return
            
			y2_str = y2_entry.get()
			y2_str = y2_str.replace(',', '.')
			try:
				y2 = float(y2_str)
			except ValueError:
				messagebox.showerror(title = 'Value error', message = 'Incorrect value of y2.')
				return

			x1_n = x1 * 10 ** notation_x123
			x2_n = x2 * 10 ** notation_x123
			x3_n = x3 * 10 ** notation_x123
			y1_n = y1 * 10 ** notation_y12
			y2_n = y2 * 10 ** notation_y12

			answer = y1_n + ((y2_n - y1_n)/(x2_n - x1_n)) * (x3_n - x1_n)

			if ck1_value.get() == 1:
				answer_show = '{:.3e}'.format(answer)
				answer_show = str(answer_show)
				if ck2_value.get() == 1:
					answer_show = answer_show.replace('e', '*10^')
					answer_show = answer_show.replace('+', '')
					if answer_show[9] == "-" and answer_show[10] == "0":
						answer_show = answer_show[:10] + answer_show[11:]
					elif answer_show[9] == "0":
						answer_show = answer_show[:9] + answer_show[10:]
			else:
				answer_show = '{:f}'.format(answer)
				answer_show = str(answer_show)

			if ck3_value.get() == 0:
				answer_show = str(answer_show)
				answer_show = answer_show.replace('.', ',')

			if platform.system() == 'Windows':
				subprocess.run(['clip.exe'], input = answer_show.strip().encode('utf-8'), check = True)
				message_label.config(text = 'Result has been copied to a clipboard.\n', foreground = 'black')
			else:
				message_label.config(text = 'Result could not have been copied to a clipboard.\nFunction supported only on Windows Vista and newer.',\
									 foreground = 'red')
			
			answer_entry.config(state = 'normal')
			answer_entry.delete(0, 'end')
			answer_entry.insert(0, answer_show)
			answer_entry.config(state = 'readonly')

		def clear():
			x1_entry.delete(0, 'end')
			x2_entry.delete(0, 'end')
			x3_entry.delete(0, 'end')
			y1_entry.delete(0, 'end')
			y2_entry.delete(0, 'end')

			notation_x123_entry.delete(0, 'end')
			notation_x123_entry.insert(0, '0')
			notation_y12_entry.delete(0, 'end')
			notation_y12_entry.insert(0, '0')

			answer_entry.config(state = 'normal')
			answer_entry.delete(0, 'end')
			answer_entry.config(state = 'readonly')

			message_label.config(text = '\n')

		def the_end():
			root.destroy()

		frame6 = Frame(root)
		calculate_btn = Button(frame6, text = 'Calculate', command = calculate, width = 10)
		calculate_btn.grid(row = 0, column = 0, padx = 20, pady = 5)

		clear_btn = Button(frame6, text = 'Clear', command = clear, width = 10)
		clear_btn.grid(row = 0, column = 1, padx = 20, pady = 5)

		exit_btn = Button(frame6, text = 'Exit', command = the_end, width = 10)
		exit_btn.grid(row = 0, column = 2, padx = 20, pady = 5)
		frame6.grid(sticky = 'S', row = 4, column = 0, padx = 5, pady = 5, columnspan = 3)

		root.mainloop()

if __name__ == '__main__':
	app = linear_interpolation_calc()
	app.display()