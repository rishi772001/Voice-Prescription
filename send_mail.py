'''
@Author: rishi
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import filedialog,messagebox
import tkinter
from tkinter import *
import os


def upload_util(name, emailid, upload_prompt):
    toaddr = emailid.get()
    fromaddr = ""  # Enter Your E-mail id
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Voice prescription"
    body = "Prescription"
    msg.attach(MIMEText(body, 'plain'))

    if not name:
        upload_prompt.filename = filedialog.askopenfilename(initialdir="F:\\Mini Projects Rishi\\voice prescription",
                                                            title="Select file",
                                                            filetypes=(
                                                            ("document files", "*.docx"), ("all files", "*.*")))

        a = os.path.split(upload_prompt.filename)
        filename = a[1]
        addr = a[0] + '/{}'.format(a[1])
    else:
        a = os.path.split(name)
        filename = a[1]
        addr = a[0] + '/{}'.format(a[1])

    attachment = open(addr, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "")  # Enter Your email password
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    messagebox.showinfo("Successfully completed", "Prescription sent successfully")
    s.quit()
    upload_prompt.destroy()


def upload(name=None):
    upload_prompt = tkinter.Tk()
    upload_prompt.geometry('300x200')
    upload_prompt.configure(background='#79f249')

    label = Label(upload_prompt, text="E-mail", bg="#ff3f2e")
    label.pack(side=LEFT)
    email = Entry(upload_prompt, bd=5, width="30")
    email.pack(side=RIGHT)

    submit = Button(upload_prompt, text="Submit", command=lambda: upload_util(name, email, upload_prompt), bg="#de04da")
    submit.pack(side=BOTTOM)
    upload_prompt.mainloop()


if __name__ == "__main__":
    upload(None)