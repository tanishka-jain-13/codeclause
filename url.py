import pyshorteners
import pyperclip
from tkinter import *

root = Tk()
# root.geometry("400*200")
root.geometry('600x300')
root.title("codeclause project--1 url shortner")
root.configure(bg='gray')
url = StringVar()
url_addrerss = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_addrerss.set(url_short)

def copyurl():
    url_short = url_addrerss.get()
    pyperclip.copy(url_short)

Label(root,text="URL Shortener", font="poppins").pack(pady=15)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_addrerss).pack(pady=5)
Button(root, text="copy URL", command=copyurl).pack(pady=7)

root.mainloop()