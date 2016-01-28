# coding:utf-8
# just can run on python 3.x  2.x is diffrent

from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
# w  = Label(root,text = "guess number")
# w.pack()

number = 59

mb.showinfo("welcome","haha lixi guess some number?")

while True:
    guess = dl.askinteger("Give me a Number","Enter a number")

    if guess == number:
        output = "you are right ! duang duang duang"
        mb.showinfo("output",output)
        break
    elif guess > number:
        output = "it's smaller"
    else:
        output = "it' bigger"

    mb.showinfo("output",output)


