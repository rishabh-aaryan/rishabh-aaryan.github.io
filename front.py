#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog, Text, font
import sys
import timeit
import os
from os import path
from datetime import datetime
import pickle


def checkex(tag):
    write_to = tag
    print(path.exists(write_to + '.html'))
    if path.exists(write_to + '.html') == False:
        return 0
    else:
        return 1


def publish4(
    user,
    texx,
    titl,
    taglist,
    ):

    start = timeit.default_timer()

    now = datetime.now()
    dt_string = now.strftime('%d/%m/%Y %H:%M')
    title = titl[0:len(titl) - 1]

    tags = eval(taglist)

    for z in range(0, len(tags)):

        write_to = tags[z]
        print(path.exists(write_to + '.html'))
        if path.exists(write_to + '.html') == False:
            index = open('index.html', 'r')
            ch = 1
            tmp = tmp2 = tmp3 = ''

            for line in index:
                if ch >= 18:
                    tmp2 += line
                else:
                    tmp3 += line
                ch += 1

            index = open('index.html', 'w')

            tmp = tmp3 + '<div class = "entry"><p><a href="' + write_to \
                + '.html">' + write_to + '</a></p></div>' + tmp2

            html = open(write_to + '.html', 'w')
            index.write(tmp)

            tmp = tmp3 + '\n' + '</body> </html>'
            html.write(tmp)
            html.close()
            index.close()

        write_to += '.html'
        html = open(write_to, 'r')
        main = open('blog.txt', 'r')
        i = j = 1
        s = s2 = ''

        for line in html:
            if j >= 18:
                s2 += line
            j += 1

        html.close()
        html = open(write_to, 'r')

        for line in html:
            if i == 18:
                html.close()
                html = open(write_to, 'w')
                text = texx
                s1 = '<h2 id=\'' + title + '\'>' + title \
                    + '</h2><small>[<a href="blog/' + title \
                    + '.html">standalone</a>]</small>'
                s1 += '<div class = "tag"><small><b>Tags: </b>'
                for q in range(0, len(tags)):
                    s1 += tags[q] + ' '
                s1 += '</small></div><p>' + text + '</p> <small>' \
                    + dt_string + ' ' + datetime.today().strftime('%A') \
                    + '</small>'
                s1 = '<div class = "entry">' + '\n' + s1 + '</div>'

                indie = open('blog/' + title + '.html', 'w')
                indie.write(s1)

                s += s1 + s2
                html.write(s)
                html.close()
                break
            s += line
            i += 1

    cmd = "git add . && git status -s && git commit -m " + 'BLOG' + " && git push origin master"

    os.system(cmd)

    stop = timeit.default_timer()
    return ('Operation Successful. Time taken: ', stop - start)


def gui():


    def clear():
        my_text.delete(1.0, END)

    def changecolours(option):
        print(option)
        binf = open('data.bin', 'rb')
        bindata = dict()
        try:
                bindata = pickle.load(binf)
        except:
                pass
        binf.close()

        print(bindata)

        cssfile = open('style.css', 'w')
        if int(option) == 1:
                scheme = 'light'
        else:
                scheme = 'dark'

        nex = 0
        idx = 0
        for i in range(0, len(bindata['css'])):
                if nex == 1:
                        nex = 0
                        try:
                                bindata['css'][i] = bindata[scheme][0][idx]
                        except:
                                print('ow')
                        idx += 1
                if bindata['css'][i] == 'color:':
                        nex = 1

                print(i, bindata['css'][i])

        nex = 0
        idx = 0
        for i in range(0, len(bindata['css'])):
                if nex == 1:
                        nex = 0
                        try:
                                bindata['css'][i] = bindata[scheme][1][idx]
                        except:
                                print('aaa')
                        idx += 1
                if bindata['css'][i] == 'background-color:':
                        nex = 1

        bindata['css'][bindata['css'].index('border-left:') + 3] = bindata[scheme][2]

        newcss = ''
        for i in bindata['css']:
                newcss += i + ' '
        cssfile.write(newcss)
        cssfile.close()

    def colourfunc():
        popup = Tk()
        popup.geometry('500x150')

        def leave():
            popup.destroy()

        def submit_colour():
            global colours
            colours = colour.get('1.0', END)
            print(colours)
            changecolours(colours)
            leave()

        popup.wm_title('Enter colourscheme ')
        label = Label(popup,
                      text='''Enter option: 
1: Light Theme
2: Dark Theme''',
                      font=('Helvetica', 10))
        label.pack(side='top', fill='x', pady=10)
        colour = Text(
            popup,
            width=27,
            height=2,
            font=('Helvetica', 14),
            undo=True,
            selectbackground='yellow',
            selectforeground='black',
            )
        colour.pack()
        b1 = Button(popup, text='Submit', command=submit_colour)
        b1.pack()

        popup.mainloop()

        return 0

    def tags():
        popup = Tk()
        popup.geometry('500x150')

        def leave():
            popup.destroy()

        def submit_tags():
            global tagslist
            tagslist = tags.get('1.0', END)
            leave()

        popup.wm_title('Enter tags')
        label = Label(popup,
                      text='Enter Tags in the form [tag1,tag2,tag3]',
                      font=('Helvetica', 10))
        label.pack(side='top', fill='x', pady=10)
        tags = Text(
            popup,
            width=27,
            height=2,
            font=('Helvetica', 14),
            undo=True,
            selectbackground='yellow',
            selectforeground='black',
            )
        tags.pack()
        b1 = Button(popup, text='Submit', command=submit_tags)
        b1.pack()

        popup.mainloop()

        return 0

    def popupn(msg):

        def leave():
            popup.destroy()
            return

        popup = Tk()
        popup.wm_title()
        label = Label(popup, text=msg, font=('Helvetica', 10))
        label.pack(side='top', fill='x', pady=10)
        b1 = Button(popup, text='OK', command=leave)
        b1.pack()
        popup.mainloop()

    def upl():
        text = my_text.get('1.0', END)
        title = my_title.get('1.0', END)
        tags()
        colourfunc()
        alist = eval(tagslist)
        (ret_msg, time_taken) = publish4('a', text, title, tagslist)
        popupn(ret_msg + str(time_taken))

    root = Tk()
    root.title('Blog maker')
    root.geometry('1280x800')

    my_frame = Frame(root)
    my_frame.pack(pady=5)

    w = Label(root, text='Title')
    w.pack()

    my_title = Text(
        root,
        width=97,
        height=2,
        font=('Helvetica', 14),
        undo=True,
        selectbackground='yellow',
        selectforeground='black',
        )
    my_title.pack()

    w = Label(root, text='Blog Text')
    w.pack()

    my_text = Text(
        root,
        width=97,
        height=25,
        font=('Helvetica', 14),
        undo=True,
        selectbackground='yellow',
        selectforeground='black',
        )
    my_text.pack()

    status_bar = Label(root, text='Ready    ', anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)

    button_frame = Frame(root)
    button_frame.pack()

    clear_button = Button(button_frame, text='Clear Screen',
                          command=clear)
    clear_button.grid(row=0, column=0)

    my_label = Label(root, text='')
    my_label.pack()

    upload = Button(
        root,
        text='Upload Blog',
        padx=15,
        pady=10,
        fg='white',
        bg='gray',
        command=upl,
        )
    upload.pack()

    root.mainloop()


gui()


			
