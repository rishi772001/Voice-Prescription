import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
import os
from time import sleep


# Import local modules
from extract_text import extract
from create_document import create
from send_mail import upload


# Function to open the file for verification
def verify(name=None):
	# To open files redirected form other function after creation
	if name:
		p = "F:/Mini Projects Rishi/voice prescription/{}.docx".format(name)
	# Manual verification of existing files
	else:
		filename = filedialog.askopenfilename(initialdir="F:\\Mini Projects Rishi\\voice prescription", title="Select file", filetypes=(("document files", "*.docx"), ("all files", "*.*")))
		p = filename

	# Split path and file name
	a = os.path.split(p)
	try:
		# Opens file
		os.startfile(a[0] + '/' + a[1])
		sleep(10)
		# Call upload function to send prescription through mail
		upload(p)
	except:
		messagebox.showerror("ERROR", "Could not open file")


# Function for existing audio file
def doc():
	# Open existing audio file
	filename = filedialog.askopenfilename(initialdir="F:\\Mini Projects Rishi\\voice prescription", title="Select file", filetypes=(("wav files", "*.wav"),("all files", "*.*")))
	
	# split path and filename
	a = os.path.split(filename)
	a = a[0] + "/" + a[1]

	r = sr.Recognizer()
	try:
		with sr.AudioFile(a) as source:
			audio = r.listen(source)
	except:
		messagebox.showerror("ERROR","Could not open file, please select .wav file")
		return

	# Convert audio to text
	try:
		text = r.recognize_google(audio)
		messagebox.showinfo("Alert", "Converted Text: {}".format(text))
	except:
		messagebox.showerror("ERROR","Could not recognize the voice")
	
	# Extract text
	try:
		name, age, date, tablet = extract(text)
	except ValueError:
		messagebox.showerror("ERROR","Could not find patient Name")
	except:
		messagebox.showerror("ERROR","Could not extract text")
	
	# Create document
	try:
		create(name, age, date, tablet)
	except PermissionError:
		messagebox.showerror("ERROR","The document is open, please close and try again!")
	except:
		messagebox.showerror("ERROR","Could not create document")

	# Verify document
	try:
		verify(name)
	except:
		messagebox.showerror("ERROR","Could not open file")
	

# Function for live recording
def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		messagebox.showinfo("Alert", "Start Speaking")
		audio = r.listen(source)
		messagebox.showinfo("Alert", "completed.")
	
	# Convert audio to text
	try:
		text = r.recognize_google(audio)
		messagebox.showinfo("Alert", "Converted Text: {}".format(text))
	except:
		messagebox.showerror("ERROR","Could not recognize the voice")
	
	# Extract text
	try:
		name, age, date, tablet = extract(text)
	except ValueError:
		messagebox.showerror("ERROR","Could not find patient Name")
	except:
		messagebox.showerror("ERROR","Could not extract text")
	
	# Create document
	try:
		create(name, age, date, tablet)
	except PermissionError:
		messagebox.showerror("ERROR","The document is open, please close and try again!")
	except:
		messagebox.showerror("ERROR","Could not create document")

	# Verify document
	try:
		verify(name)
	except:
		messagebox.showerror("ERROR","Could not open file")


# Create GUI main window
main_window = tk.Tk()
main_window.geometry('300x300')
main_window.configure(background='#54a8cc')
main_window.title('Voice Prescription')

try:
	# Add buttons for every functions
	btn1 = tk.Button(main_window, text='Upload Audio File', width=25, command=doc, bg="#eb7e44")
	btn2 = tk.Button(main_window, text='Start new recording', width=25, command=listen, bg="#eb7e44")
	btn4 = tk.Button(main_window, text='Verify document', width=25, command=verify, bg="#eb7e44")
	btn3 = tk.Button(main_window, text='Send Document through mail', width=25, command=upload, bg="#eb7e44")
	btn1.pack(pady=20)
	btn2.pack(pady=20)
	btn4.pack(pady=20)
	btn3.pack(pady=20)
except:
	messagebox.showinfo("Error", "Something went wrong, please try again")

main_window.mainloop()
main_window.destroy()
