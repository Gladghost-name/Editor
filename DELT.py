import os
import tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pyttsx3

root = Tk()
root.title('TextEditor ')
root.geometry('1300x800')
root.configure(background='white')

my_menu = Menu(root)

root.config(menu=my_menu)

global selected 
selected = False 

global file 
file = False 

global i

def openFile():
    global file
    from tkinter import filedialog
    my_list.delete(0, END)
    typed = my_text.get(0.0, END)
    file = filedialog.askdirectory()

    import os 

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def DeleteFile():
    # my_list.delete(first=ANCHOR)

    select = my_list.get(ANCHOR)

    import os

    print(select) 

    folder = os.getcwd()

    os.chdir(folder)

    if FileNotFoundError:
        messagebox.showerror(title='File Not Found Error', message='cant Find file in ' + folder)

    os.remove(select)

    my_text.delete(0.0, END)

    my_list.delete(0, END)
    typed = my_text.get(0.0, END)
    import os 

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def NewFile():
    from tkinter import messagebox
    typed = my_text.get(0.0, END)

    
    if file == False:
        mso = messagebox.showwarning(title='Alert!! ', message=' No folder Opened ')

    Folder = file

    my_mes = messagebox.askyesno(title='Alert!! ', message='Are you sure you want to add this file to ' + Folder)

    if my_mes == 0:
        pass 

    if my_mes == 1:
        my_list.insert(END, typed)

        os.chdir(Folder)

        file_mes = messagebox.askokcancel(title='Alert!! ', message='File created in list but not in path ' + Folder  + ' select Add to path in the file menu')

        f = open(typed, 'w+')

        f.write('This is a new file')

        if file == False:
            mso = messagebox.showwarning(title='Alert!! ', message=' No folder Opened ')

def PythonFile():
    import os 
    import subprocess

    mes = messagebox.askyesno(title='allert!! ', message='Are you sure you want to run this python file, if there is no file this window will freeze and can cause damage')

    if mes == 0:
        pass

    if mes == 1:


        select = my_list.get(first=ANCHOR)

        print(select)

        if file == False:
            messagebox.showwarning(title='Cant run file', message='There is no file to run ')

            pass

        os.system('python ' + select)

        if SyntaxError:
            messagebox.showwarning(title='Syntax Error', message='Your file Ended, there might be a code error, please check terminal for more info')

        else:
            pass 

        # os.system('C:/Users/adara/AppData/Local/Programs/Python/Python39/python.exe ' + select)

def PythonFile1(e):
    import os 
    import subprocess

    mes = messagebox.askyesno(title='allert!! ', message='Are you sure you want to run this python file, if there is no file this window will freeze and can cause damage')

    if mes == 0:
        pass

    if mes == 1:


        select = my_list.get(first=ANCHOR)

        print(select)

        if file == False:
            messagebox.showwarning(title='Cant run file', message='There is no file to run ')

            pass

        os.system('python ' + select)

        if SyntaxError:
            messagebox.showwarning(title='Syntax Error', message='Your file Ended, there might be a code error, please check terminal for more info')

        else:
            pass 

        # os.system('C:/Users/adara/AppData/Local/Programs/Python/Python39/python.exe ' + select)

def SaveFile():
    import os 

    Folder = os.getcwd()

    typed = my_text.get(0.0, END)

    files = os.listdir(Folder)

    os.chdir(Folder)
    
    File = my_list.get(ANCHOR)

    good = open(file=File, mode='w+')

    good.write(typed)

def SaveFile1(e):
    import os 

    Folder = os.getcwd()

    typed = my_text.get(0.0, END)

    files = os.listdir(Folder)

    os.chdir(Folder)
    
    File = my_list.get(ANCHOR)

    good = open(file=File, mode='w+')

    good.write(typed)

def openFile1(e):
    from tkinter import filedialog
    global i
    my_list.delete(0, END)
    typed = my_text.get(0.0, END)
    file = filedialog.askdirectory()
    import os 

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def TransFile():
    typed = my_text.get(0.0, END)

    engine = pyttsx3.init()

    engine.say(typed)

    engine.runAndWait()

def TransFile1(e):
    typed = my_text.get(0.0, END)

    engine = pyttsx3.init()

    engine.say(typed)

    engine.runAndWait()

def deleteAll():
    my_list.delete(0, END)

    my_text.delete(0.0, END)

def JavaFile():
    file = my_list.get(ANCHOR)

    import os 

    os.system('java ' + file)

def JavaFile1(e):
    file = my_list.get(ANCHOR)

    import os 

    os.system('java ' + file)

def SaveAs():
    from tkinter import filedialog

    folder = file


    f = filedialog.asksaveasfilename(defaultextension='.*', initialdir=folder, title='Save As', filetypes=(("Python Files", '*.py'), ("Java Files", '*.java'), ('C# Files', '*.cs'), ('HTML Files', '*.html'), ('cpp Files', '*.cpp'), ('C Files', '*.c')))
    
    f = open(file, 'w')
    
    f.write(my_text.get(0.0, END))

    f.close()

    root.title('TextEditor - ' + file)

def filecreator(e):
    file_menu.tk_popup(e.x_root, e.y_root)

def fileEdit(e):
    edit_menu.tk_popup(e.x_root, e.y_root)

def cut_text(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()
        my_text.delete('sel.first', 'sel.last')

def copy_text(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()

def paste_text(e):
    if selected:
        position = my_text.index(INSERT)
        my_text.insert(position, selected)

def insert_img():
    global my_image 
    img = filedialog.askopenfilename()

    my_image = PhotoImage(file=img)
    my_text.image_create(INSERT, image=my_image)

def Renamefile():
    File = my_list.get(ANCHOR)
    import os 

    Folder = file

    if File == '':
        mes = messagebox.showwarning(title='Alert!! ', message='No file found to rename') 

        pass 

    rename = Tk()
    rename.title('Rename File - ' + file)
    rename.geometry('300x500')
    rename.resizable(False, False)

    my_entry = Entry(rename, width=50,)
    my_entry.pack()

    my_file = my_list.get(first=ANCHOR)

    def Rename():
        entry = my_entry.get()

        os.chdir(Folder)

        os.rename(my_file, entry)

        my_list.delete(0, END)
        typed = my_text.get(0.0, END)

        list = os.listdir(file)

        def File(e):
            File = my_list.get(ANCHOR)
            my_text.delete(0.0, END)
            print(File)

            os.chdir(file)

            wow = open(file=File, mode='r')

            red = wow.read()

            my_text.insert(0.0, red)

        for i in list:
            my_list.insert(END, i)

        root.title('TextEditor - ' + file)

        my_list.bind('<<ListboxSelect>>', File)

    my_entry.insert(0, File)

    my_button = Button(rename, width=300, height=0, bg='white', text='rename', border=0, command=Rename)
    my_button.pack()

    rename.mainloop()

def explorefile():
    from tkinter import filedialog
    Folder = file 

    vol = filedialog.asksaveasfilename(defaultextension='.*', initialdir=Folder, title='Project dialog', filetypes=(("Python Files", '*.py'), ("Java Files", '*.java'), ('C# Files', '*.cs'), ('HTML Files', '*.html'), ('cpp Files', '*.cpp'), ('C Files', '*.c')))

def explorefile1(e):
    from tkinter import filedialog
    Folder = file 

    vol = filedialog.asksaveasfilename(defaultextension='.*', initialdir=Folder, title='Project dialog', filetypes=(("Python Files", '*.py'), ("Java Files", '*.java'), ('C# Files', '*.cs'), ('HTML Files', '*.html'), ('cpp Files', '*.cpp'), ('C Files', '*.c')))


def ReloadFile():
    my_list.delete(0, END)
    typed = my_text.get(0.0, END)
    import os 

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def PrintFile():
    import win32print
    import sys 
    import win32api
    from tkinter import messagebox

    printer_name = win32print.GetDefaultPrinter()

    mes = messagebox.askyesno(title='Before you print!! ', message='are you sure you want to print this file with ' + printer_name)

    if mes == 0:
        print('Stopped printing!! ') 

    if mes == 1:
        print('Printing... ')

        text = my_list.get(first=ANCHOR)

        if text:
            win32api.ShellExecute(0, 'print', text, None, '.', 0)

def PrintFile1(e):
    import win32print
    import sys 
    import win32api
    from tkinter import messagebox

    printer_name = win32print.GetDefaultPrinter()

    mes = messagebox.askyesno(title='Before you print!! ', message='are you sure you want to print this file with ' + printer_name)

    if mes == 0:
        print('Stopped printing!! ') 

    if mes == 1:
        print('Printing... ')

        text = my_list.get(first=ANCHOR)

        if text:
            win32api.ShellExecute(0, 'print', text, None, '.', 0)

def App():
    typed = my_text.get(0.0, END)
    file  = my_list.get(ANCHOR)

    os.getcwd()

    print(file)

    os.system('pip install pyinstaller')

    os.system('pyinstaller ' + file)

def Limp():
    my_text.config(bg='#10E111', fg='black')

    my_list.config(bg='#128373')

def Knot():
    my_text.config(bg='#1E3454', fg='green')

    my_list.config(bg='#274585')

def Coil():
    my_text.config(bg='#1E6476', fg='white')

    my_list.config(bg='#567383')

def Bigante():
    my_text.config(bg='#0044FF', fg='black')

    my_list.config(bg='#FFC700')

def Recon():
    my_text.config(bg='#000D0F', fg='white')

    my_list.config(bg='#FF0013')

def Danger():
    my_text.config(bg='#FF3500', fg='purple', selectbackground='grey', selectforeground='white')

    my_list.config(bg='#FF005B')

def Default():
    my_text.config(bg='#3A3A3A', fg='orange', selectbackground='light blue', selectforeground='white')

    my_list.config(bg='#252526')

def About():
    mes = messagebox.askokcancel(title='About TextEditor? ', message='TextEditor version(v0.1) Thank you for using TextEditor. ')

def deleteAll1(e):
    import os 

    Folder = file 

    mes = messagebox.showwarning(title='warning', message='Are you sure you want to delete all files in ' + Folder)

    print(mes)

    my_list.delete(0, END)

    os.chdir(Folder)

    all = my_list.get(1, END)

    my_text.delete(0.0, END)

    my_list.delete(0, END)
    typed = my_text.get(0.0, END)

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def SaveAs1(e):
    from tkinter import filedialog

    folder = file
    
    f = filedialog.asksaveasfilename(defaultextension='.*', initialdir=folder, title='Save As', filetypes=(("Python Files", '*.py'), ("Java Files", '*.java'), ('C# Files', '*.cs'), ('HTML Files', '*.html'), ('cpp Files', '*.cpp'), ('C Files', '*.c')))
    
    f = open(file, 'w')
    
    f.write(my_text.get(0.0, END))

    f.close()

    root.title('TextEditor - ' + file + ' (Saved)')

def NewFile1(e):
    from tkinter import messagebox
    typed = my_text.get(0.0, END)

    Folder = file

    my_mes = messagebox.askyesno(title='Alert!! ', message='Are you sure you want to add this file to ' + Folder)

    if my_mes == 0:
        pass 

    if my_mes == 1:
        my_list.insert(END, typed)

        os.chdir(Folder)

        file_mes = messagebox.askokcancel(title='Alert!! ', message='File created in list but not in path ' + Folder + ' select Add to path in the file menu')

        f = open(typed, 'w+')

        f.write('This is a new file')

def ReloadFile1(e):
    my_list.delete(0, END)
    typed = my_text.get(0.0, END)
    import os 

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def DeleteFile1(e):
    select = my_list.get(ANCHOR)

    import os

    print(select) 

    folder = os.getcwd()

    os.chdir(folder)

    os.remove(select)

    my_text.delete(0.0, END)

    my_list.delete(0, END)
    typed = my_text.get(0.0, END)
    import os 

    list = os.listdir(file)

    def File(e):
        File = my_list.get(ANCHOR)
        my_text.delete(0.0, END)
        print(File)

        os.chdir(file)

        wow = open(file=File, mode='r')

        red = wow.read()

        my_text.insert(0.0, red)

    for i in list:
        my_list.insert(END, i)

    root.title('TextEditor - ' + file)

    my_list.bind('<<ListboxSelect>>', File)

def AddFile():
    Folder = file 

    typed = my_text.get(0.0, END)

    select = my_list.get(first=ANCHOR)

    os.chdir(Folder)

    os.getcwd()

def PlaySound():
    import playsound 

    Folder = file 

    my_sound= my_list.get(ANCHOR)

    if UnicodeDecodeError:
        messagebox.showwarning(title='Decode Error ', message='Cant read file ' + my_sound)

    os.chdir(Folder)

    playsound.playsound(sound=my_sound, block=False)

def PlaySound1(e):
    import playsound 

    Folder = file 

    my_sound= my_list.get(ANCHOR)

    if UnicodeDecodeError:
        messagebox.showwarning(title='Decode Error ', message='Cant read file ' + my_sound)

    os.chdir(Folder)

    playsound.playsound(sound=my_sound, block=False)

def OpenFile():
    f = filedialog.askopenfilename(initialdir='C:/', title='Save As', filetypes=(("Python Files", '*.py'), ("Java Files", '*.java'), ('C# Files', '*.cs'), ('HTML Files', '*.html'), ('cpp Files', '*.cpp'), ('C Files', '*.c')))

    my_list.insert(END, f)

    red  = open(f, 'w+')

    wow = red.read()

    my_text.insert(0.0, wow)

def OpenFile1(e):
    f = filedialog.askopenfilename(initialdir='C:/', title='Save As', filetypes=(("Python Files", '*.py'), ("Java Files", '*.java'), ('C# Files', '*.cs'), ('HTML Files', '*.html'), ('cpp Files', '*.cpp'), ('C Files', '*.c')))

    my_list.insert(END, f)

    red  = open(f, 'w+')

    wow = red.read()

    my_text.insert(0.0, wow)

def PlayApp():
    folder = file 

    select = my_list.get(first=ANCHOR)

    os.chdir(folder)

    os.system(command='cd ' + folder)

    os.system(command=select)

def PlayApp1(e):
    folder = file 

    select = my_list.get(first=ANCHOR)

    os.chdir(folder)

    os.system(command='cd ' + folder)

    os.system(command=select)

def OpenApp():
    folder = file 

    my_text.delete(0.0, END)

    os.chdir(folder)

    select = my_list.get(first=ANCHOR)

    root.title('TextEditor - ' + select)

    f = filedialog.askopenfilename(initialdir=select, title='Folder location')

    my_list.delete(0, END)

    typed = my_text.get(0.0, END)

    shit = select

    folder = f

    os.system('cd ' + folder)

    all = os.listdir(select)

    for files in all:
        my_list.insert(END, files)

    wow = open(f, 'r')

    red = wow.read()

    my_list.insert(END, f)

    my_text.insert(0.0, red)

def OpenApp1(e):
    folder = file 

    my_text.delete(0.0, END)

    os.chdir(folder)

    select = my_list.get(first=ANCHOR)

    root.title('TextEditor - ' + select)

    f = filedialog.askopenfilename(initialdir=select, title='Folder location')

    my_list.delete(0, END)

    typed = my_text.get(0.0, END)

    shit = select

    file = f

    os.system('cd ' + folder)

    all = os.listdir(select)

    for files in all:
        my_list.insert(END, files)

    wow = open(f, 'r')

    red = wow.read()

    my_list.insert(END, f)

    my_text.insert(0.0, red)

def AddFile1(e):
    Folder = file 

    typed = my_text.get(0.0, END)

    select = my_list.get(first=ANCHOR)

    os.chdir(Folder)

    os.getcwd()

def Renamefile1(e):
    File = my_list.get(ANCHOR)
    import os 

    Folder = file

    if File == '':
        mes = messagebox.showwarning(title='Alert!! ', message='No file found to rename') 

        pass 

    rename = Tk()
    rename.title('Rename File - ' + file)
    rename.geometry('300x500')
    rename.resizable(False, False)

    my_entry = Entry(rename, width=50,)
    my_entry.pack()

    my_file = my_list.get(first=ANCHOR)

    def Rename():
        entry = my_entry.get()

        os.chdir(Folder)

        os.rename(my_file, entry)

        my_list.delete(0, END)
        typed = my_text.get(0.0, END)

        list = os.listdir(file)

        def File(e):
            File = my_list.get(ANCHOR)
            my_text.delete(0.0, END)
            print(File)

            os.chdir(file)

            wow = open(file=File, mode='r')

            red = wow.read()

            my_text.insert(0.0, red)

        for i in list:
            my_list.insert(END, i)

        root.title('TextEditor - ' + file)

        my_list.bind('<<ListboxSelect>>', File)

    my_entry.insert(0, File)

    my_button = Button(rename, width=300, height=0, bg='white', text='rename', border=0, command=Rename)
    my_button.pack()

    rename.mainloop()

def wrap():
    my_text.config(wrap='word')

def docFile():
    import PyPDF2

    mes = messagebox.showwarning(title='Work in progress... ', message='pyinputer version 0.1 is still work in progress, there might be some line bugs')

    open_file = filedialog.askopenfilename(initialdir='C:/', title='open pdf file', filetypes=(('PDF files', '*.pdf'),('All Files', '*.*')))

    if open_file:
        pdf_file = PyPDF2.PdfFileReader(open_file)

        page = pdf_file.getPage(0)

        stuff = page.extractText()

        my_text.insert(0.0, stuff)

def htmlFile():
    folder = file 

    select = my_list.get(first=ANCHOR)

    os.system('cd ' + folder)

    os.system(select)

def CppFile():
    folder = file 

    select = my_list.get(first=ANCHOR)

    os.system('cd ' + folder)

    os.system(select)

my_scroll = Scrollbar(root)

my_frame = Frame(root, width=200, height=800, border=0, bg='dark blue')
my_frame.place(y=0, x=0)

my_list = Listbox(my_frame, width=30, height=500, cursor='hand2',bg='#252526', border=False, fg='white', selectmode=MITER, activestyle=NONE)
my_list.place(x=0, y=0)

my_text = Text(root, width=114, height=400, bg='#3A3A3A', undo=True,border=0,fg='orange', insertbackground='white',yscrollcommand=my_scroll, autoseparators=True, font=('Calibri', 12))
my_text.pack(side=RIGHT)

my_scroll.pack()

my_text.focus()

FileImage = PhotoImage(file="folder.png")

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open Folder', command=openFile, accelerator='Ctrl+O')
file_menu.add_command(label='Delete File', command=DeleteFile, accelerator='Shift+D')
file_menu.add_command(label='New File', command=NewFile, accelerator='Ctrl+N')
file_menu.add_command(label='Save Project', command=SaveFile, accelerator='Ctrl+S')
file_menu.add_command(label='Delete All', command=deleteAll, accelerator='Ctrl+D')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit, accelerator='Ctrl+W')
file_menu.add_separator()
file_menu.add_command(label='Save As', command=SaveAs, accelerator='Ctrl+A')
file_menu.add_command(label='Open File', command=OpenFile, accelerator='Ctrl+F')
file_menu.add_command(label='Rename File', command=Renamefile, accelerator='Ctrl+R')
file_menu.add_command(label='Open Project in File explorer', command=explorefile, accelerator='Ctrl+E')
file_menu.add_command(label='Reload from disk', command=ReloadFile, accelerator='Shift+U')
file_menu.add_command(label='Add to path', command=AddFile, accelerator='Ctrl+H')
file_menu.add_command(label='Import PDFFile', command=docFile, accelerator='Ctrl+H')


run_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Run', menu=run_menu)
run_menu.add_command(label='Python', command=PythonFile, accelerator='Ctrl+M')
run_menu.add_command(label='HTML', command=htmlFile, accelerator='Ctrl+U')
run_menu.add_command(label='cpp', command=CppFile, accelerator='Ctrl+Q')
run_menu.add_command(label='Translate', command=TransFile, accelerator='Ctrl+T')
run_menu.add_command(label='Print to printer', command=PrintFile, accelerator='Ctrl+I')
run_menu.add_command(label='Play Sound', command=PlaySound, accelerator='ALT+P')
run_menu.add_command(label='Run Programes', command=PlayApp, accelerator='ALT+R')
run_menu.add_command(label='Open directory', command=OpenApp, accelerator='Ctrl+K')

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=lambda: cut_text(False))
edit_menu.add_command(label='Copy', command=lambda: copy_text(False))
edit_menu.add_command(label='Paste', command=lambda: paste_text(False))
edit_menu.add_command(label='Insert image', command=insert_img)

Pub_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Publish', menu=Pub_menu, accelerator='B')
Pub_menu.add_command(label='Application', command=App, accelerator='Q')
Pub_menu.add_command(label='module', command=lambda: copy_text(False), accelerator='M')
Pub_menu.add_command(label='Add', command=insert_img, accelerator='W')

for_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Format', menu=for_menu, accelerator='B')
for_menu.add_command(label='Word Wrap', command=wrap, accelerator='Shift+W')
for_menu.add_command(label='Default Wrap', command=wrap, accelerator='Ctrl+L')
for_menu.add_command(label='Font', command=wrap)

The_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Theme', menu=The_menu)
The_menu.add_command(label='Limp hole', command=Limp)
The_menu.add_command(label='Redknot', command=Knot)
The_menu.add_command(label='Coil', command=Coil)
The_menu.add_command(label='Bigante', command=Bigante)
The_menu.add_command(label='Recon', command=Recon)
The_menu.add_command(label='Danger', command=Danger)
The_menu.add_command(label='Default', command=Default)

Help_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Help', menu=Help_menu)
Help_menu.add_command(label='find', command=App)
Help_menu.add_command(label='About... ', command=About)


my_text.bind('<Control-s>', SaveFile1)
my_text.bind('<Control-o>', openFile1)
my_list.bind('<Button-3>', filecreator)
my_text.bind('<Button-3>', fileEdit)
my_text.bind('<Control-w>', quit)
my_text.bind('<Control-n>', NewFile1)
my_text.bind('<Control-a>', SaveAs1)
my_text.bind('<Control-f>', OpenFile1)
my_text.bind('<Shift-U>', ReloadFile1)
my_text.bind('<Control-e>', explorefile1)
my_list.bind('<Shift-D>', DeleteFile1)
my_list.bind('<Control-d>', deleteAll1)

my_text.bind('<Control-h>', AddFile1)
my_text.bind('<Control-r>', Renamefile1)
my_text.bind('<Control-m>', PythonFile1)
my_text.bind('<Control-u>', JavaFile1)
my_text.bind('<Control-q>', NewFile1)
my_text.bind('<Control-t>', TransFile1)
my_text.bind('<Control-i>', PrintFile1)
my_text.bind('<Alt-p>', PlaySound1)
my_text.bind('<Alt-r>', PlayApp1)
my_text.bind('<Control-k>', OpenApp1)
my_list.bind('<Shift-D>', DeleteFile1)
my_list.bind('<Control-d>', deleteAll1)

root.mainloop()