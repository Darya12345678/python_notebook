import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile # две функции: одна для сохранения вторая для открытия файла
from tkinter.messagebox import showerror # для отображ ошибок
from tkinter import messagebox

FILE_NAME = tkinter.NONE # переменная с пустым именем файла
# функция для создания файла
def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END) #очищает текст. поле от всех символов-это и будет соз-ие нового файла

#функция сохранения файла
def save_file():
    data = text.get('1.0', tkinter.END)#перемен DATA получает весь текст, кот.хранится в текстовом поле
    out = open(FILE_NAME, 'w')#открываем пустой файл с режимом записи
    out.write(data) #запис-ет все из перемен DATA в пустой файл 
    out.close()

#функция сохранения файла с возможностью выбора места хранения и имени
def save_as():
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Ошибка сохранения файла")

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0',tkinter.END)
    text.insert('1.0', data)

def info():
    messagebox.showinfo("Information", "Приложение 'Заметки' для записи текстовых заметок")

root = tkinter.Tk() # с помощью перем.root вызываются ф-ции из библиотеки
root.title("Заметки") # заголовок окна

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500) # мин и макс размеры окна

text = tkinter.Text(root, width=400, height=400, bg="steel blue", wrap="word")# пер-ая выз-ет виджет текстового поля, первым параметром указано в каком окне
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)


text.pack()  # метод отображ-я интерфейса

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar) #пер-ая для хранения функции вызова меню
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Info", command=info)
menuBar.add_cascade(label="Exit", command=root.quit) #root.quit ф-ция выхода с программы
root.config(menu=menuBar)

root.mainloop() # вызов интерфейса

