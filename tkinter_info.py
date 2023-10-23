from tkinter import *
from tkinter.messagebox import showerror, showinfo, askokcancel
import sqlite3

py = True

def new_window():
    global py
    def on_focus(event):
        Name_log = entry_name.get()
        if Name_log == 'Логин':
            entry_name.delete(0, END)
            entry_name['fg'] = 'black'
        else:
            pass
     
    def off_focus(event):
        Name = entry_name.get()
        if len(Name) == 0:
            entry_name['fg'] = '#B3B3B3'
            entry_name.insert(0, 'Логин')
        else:
            pass
     
     
    def on_pass(event):
        Pass = entry_password.get()
        if len(Pass) == 6:
            entry_password.delete(0, END)
            entry_password['show'] = '•'
            entry_password['fg'] = 'black'
        else:
            pass
        
    def off_pass(event):
        Password = entry_password.get()
        if len(Password) == 0:
            entry_password['show'] = ''
            entry_password['fg'] = '#B3B3B3'
            entry_password.insert(0, 'Пароль')
     
    def reg():
        global py
        if py == True:
            btn_sign_in['text'] = 'Регистрация'
            btn_sign_in['bg'] = 'silver'
            btn_sign_in['activebackground'] = 'silver'
            avto_lbl['text'] = 'Регистрация'
            account['text'] = 'У вас есть аккаунт?'
            btn_registr['text'] = 'Войти'
            py = False
        else:
            btn_sign_in['text'] = 'Войти'
            btn_sign_in['bg'] = 'gray'
            btn_sign_in['activebackground'] = 'gray'
            account['text'] = 'У вас нет аккаунт?'
            btn_registr['text'] = 'Регистрация'
            avto_lbl['text'] = 'Авторизация'
            py = True
    
    def test():
        login = entry_name.get()
        password = entry_password.get()
        if btn_sign_in['text'] == 'Войти':
            if login == 'Логин' or login == '' or password == 'Пароль' or password == '':
                showerror('Error in SignIn', 'Пожалуйста введите все поле')
            elif login.endswith('@gmail.com') == False or len(password) < 8:
                showerror('Error in SignIn', 'Должен быть длина пароля больше 8 и правильный электронный почта')
            else:
                conn = sqlite3.connect('Account.db')
                c = conn.cursor()
                c.execute('SELECT * FROM Users WHERE login=? AND password=?', (login, password))
                result = c.fetchone()
                c.close()
                conn.close()
                if result is not None:
                    new_Window()
                else:
                    showerror('Ошибка', 'Аккаунт не найден')
        if btn_sign_in['text'] == 'Регистрация':
            if login == 'Логин' or login == '' or password == 'Пароль' or password == '':
                showerror('Error in SignIn', 'Пожалуйста введите все поле')
            elif login.endswith('@gmail.com') == False or len(password) < 8:
                showerror('Error in SignIn', 'Должен быть длина пароля больше 8 и правильный электронный почта')
            else:
                con = sqlite3.connect('Account.db')
                c1 = con.cursor()
                c1.execute('SELECT * FROM Users WHERE login=? AND password=?', (login, password))
                result2 = c1.fetchone()
                c1.close()
                con.close()
                if result2 is not None:
                    showerror('Error account', 'Такой аккаунт уже есть')
                else:
                    co = sqlite3.connect('Account.db')
                    # создать курсор
                    c2 = co.cursor()
                    # выполнить запрос SQL
                    c2.execute("INSERT INTO Users (login, password) VALUES (?, ?)", (login, password))
                    co.commit()
                    co.close()
                    showinfo('Поздравлю', 'Успешно зарегистрировано.Теперь можно войти!')
    
    def new_Window():
        
        name = entry_name.get()
        password = entry_password.get()

        def Destroy():
            if askokcancel('Выход из аккаунта?', 'Точно хотите выйти из аккаунта?'):
                new_window()

        def Close():
            if askokcancel('Закрыть приложения?', 'Вы уверены?'):
                root.destroy()
        
        def Delete():
            if askokcancel('Удалить аккаунт', 'Уверены, хотите удалит аккаунт?'):
                s = sqlite3.connect('Account.db')
                crs = s.cursor()
                crs.execute('DELETE FROM Users WHERE login = ? and password = ?', (name, password))
                s.commit()
                crs.execute('SELECT * FROM Users')
                print(crs.fetchall())
                crs.close()
                s.close()
                new_window()
        
        def Info():
            showinfo('Мой аккаунт', f'Ваш логин: {name}\nВаш пароль:{password}')
        
        def Program():
            showinfo('О программе', 'Приложения: Руководство по PYTHON\nСоздатель: Ережеп Бекарыс\nДата создания: 23.04.2023\nВремя создания: 07:00\nПоследняя обновления: 23.04.2023')

        def Help():
            showinfo('Помощь', 'Здраствуйте, у меня несколько совет:\n1.После регистрация вам нужно в отдел Войти;\n2.После удаление аккаунта вы попадете в отдел регистрации;\n3.Это приложения для изучения Tkinter, а не Python;\n4.Если вам сложно понять что там написано вам нужно начать с самого Python')


        # function-1
        def tk_info():
            info_frame_tk = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            info_frame_tk.place(x = 205, y = 40)

            lbl_info = Label(info_frame_tk, text = 'Введение Tkinter', bg = '#fff', font = 'Calibri 14 bold')
            lbl_info.place(x = 100, y = 20)

            text_in = '''Многие программы на сегодняшний день используют графический интерфейс, который более интуитивен и удобен для пользователя, чем консоль. И с помощью языка программирования Python также можно создавать графические программы. Для этого в Python по умолчанию применяется специальный тулкит - набор компонентов, который называется tkinter. Тулкит tkinter доступен в виде отдельного встроенного модуля, который содержит все необходимые графические компоненты - кнопки, текстовые поля и т.д.\nПо сути Tkinter представляет интерфейс в Python для графической библиотеки Tk (Собственно само название "Tkinter" является сокращением "Tk interface"). Первоначально данная библиотека разрабатывалась для языка Tcl - ее создал в 1988 году Джон Остерхаут (John Ousterhout), профессор computer science из Беркли для создания графических приложений для своего языка Tcl.Но впоследствии Tk была адаптирована для широкого ряда динамических языков, в частности, для Ruby, Perl и естественно для языка Python (в 1994 году). И на сегодняшний день и библиотека Tk, и сам тулкит tkinter доступны для большинства операционных систем, в том числе для Mac OS, Linux и Windows.'''

            text_tk = Text(info_frame_tk, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 27)
            text_tk.place(x = 20, y = 50)

            text_tk.insert(END, text_in)
            text_tk['state'] = 'disabled'
        
        # function-2
        def win_info():
            win_frame_tk = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            win_frame_tk.place(x = 205, y = 40)

            win_info = Label(win_frame_tk, text = 'Создание окно', bg = '#fff', font = 'Calibri 14 bold')
            win_info.place(x = 100, y = 20)

            window_text = Text(win_frame_tk, width = 45, height = 6, bg = 'black', bd = 0, fg = 'white', font = 'Calibri 12 bold')
            window_text.place(x = 20, y = 60)
            text_win = '''import tkinter as tk\n
root = tk.Tk()
root.title('Example')
root.geometry('300x300')
root.mainloop()
'''
            window_text.insert(END, text_win)
            window_text['state'] = 'disabled'

            window_info = Text(win_frame_tk, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 30)
            window_info.place(x = 20, y = 180)
            win_text = '''Как и любой модуль, tkinter в Python можно импортировать двумя способами: командами import tkinter или from tkinter import *.Объект окна верхнего уровня создается при обращении к классу Tk модуля tkinter. Переменную связанную с объектом-окном принято называть root (хотя понятно, что можно назвать как угодно, но так уж принято).главное окно тоже не появится, пока не будет вызван специальный метод mainloop.В нашем примере также можно использовать класс:'''
            window_info.insert(END, win_text)
            window_info['state'] = 'disabled'

            class_info = '''from tkinter import *
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Example')
        self.geometry('300x300')
    def run(self):
        self.mainloop()
root = App()
root.run()'''
            class_in = Text(win_frame_tk, bd = 0, bg = 'black', fg = '#fff', font = 'Calibri 12 bold', wrap = 'word', width = 45, height=10)
            class_in.place(x = 20, y = 370)
            class_in.insert(END, class_info)
            class_in['state'] = 'disabled'

        # function-3
        def widget():
            widget_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            widget_frame.place(x = 205, y = 40)

            win_info = Label(widget_frame, text = 'Виджеты', bg = '#fff', font = 'Calibri 14 bold')
            win_info.place(x = 140, y = 10)

            wid_text = '''Виджет это объект видимый на экране, как правило прямоугольной формы.Виджеты:
- Canvas : "холст", на нем можно "рисовать";
- Button : кнопка;
- Checkbutton : кнопка-флажок;
- Radiobutton : кнопка-переключатель;
- Entry : однострочный редактор текста;
- Text : многострочный редактор текста;
- ScrolledText : многострочный редактор текста с возможностью прокрутки;
- Frame : рамка, внутри рамки можно размещать другие виджеты;
- LabelFrame : рамка с надписью для группировки виджетов;
- Label : текстовая строка, надпись;
- Message : надпись из нескольких текстовых строк;
- Listbox : меню в виде списка с возможностью выбора нескольких элементов;
- Spinbox : список выбора с двумя стрелками (колесом) прокрутки;
- PanedWindow : окно из нескольких зон с подвижными разделителями;
- Scale : шкала с ползунковым регулятором (слайдер);
- Scrollbar : скроллбар (полоса прокрутки);
- Menu : главное меню и подменю в главном меню;
- Menubutton : кнопка инициирующая выпадающее меню класса Menu;'''
            text_wid = Text(widget_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 42, height = 30)
            text_wid.place(x = 20, y = 50)
            text_wid.insert(END, wid_text)
            text_wid['state'] = 'disabled'

        # function-4
        def button():
            button_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            button_frame.place(x = 205, y = 40)

            button_label = Label(button_frame, text = 'Кнопки', bg = '#fff', font = 'Calibri 14 bold')
            button_label.place(x = 140, y = 10)

            but_text = '''Объект-кнопка создается вызовом класса Button модуля tkinter. При этом обязательным аргументом является лишь родительский виджет(например, окно верхнего уровня). Другие свойства могут указываться при создании кнопки или задаваться (изменяться) позже. Синтаксис:'''
            btn_text = Text(button_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 42, height = 6)
            btn_text.place(x = 20, y = 50)
            btn_text.insert(END, but_text)
            btn_text['state'] = 'disabled'

            text1 = Text(button_frame, bd = 0, bg = 'black', fg = '#fff', font = 'Calibri 12 bold', wrap = 'word', width = 42, height = 2)
            text1.place(x = 20, y = 175)
            text1.insert(END, 'переменная = Button (родит_виджет, *свойство=значение, … ….+)')
            text1['state'] = 'disabled'

            but_text2 = '''В tkinter кнопки представлены классом Button. Основные параметры виджета Button:
● command: функция, которая вызывается при нажатии на кнопку
● compund: устанавливает расположение картинки и текста относительно друг друга
● cursor: курсор указателя мыши при наведении на метку
● image: ссылка на изображение, которое отображается на метке
● pading: отступы от границ вилжета до его текста
● state: состояние кнопки
● text: устанавливает текст метки
● textvariable: устанавливает привязку к элементу StringVar
● width: ширина виджета'''
            text2 = Text(button_frame,  bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 42, height = 18)
            text2.place(x = 20, y = 220)
            text2.insert(END, but_text2)
            text2['state'] = 'disabled'

        # function-5
        def pack_1():
            pack_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            pack_frame.place(x = 205, y = 40)

            pack_label = Label(pack_frame, text = 'Метод .pack()', bg = '#fff', font = 'Calibri 14 bold')
            pack_label.place(x = 140, y = 10)

            text1 = '''Для позиционирования виджетов в контейнере применяются различные способы. Один из них представляет вызов у виджета метода pack(). Этот метод принимает следующие параметры:

● expand: если равно True, то виджет заполняет все пространство контейнера;
● fill: определяет, будет ли виджет растягиваться, чтобы заполнить свободное пространство вокруг. Этот параметр может принимать следующие значения: NONE (по умолчанию, элемент не растягивается), X (элемент растягивается только по горизонтали), Y (элемент растягивается только по вертикали) и BOTH (элемент растягивается по вертикали и горизонтали);
● anchor: помещает виджет в определенной части контейнера. Может принимать значения n, e, s, w, ne, nw, se, sw, c, которые являются сокращениями от Noth(север - вверх), South (юг - низ), East (восток - правая сторона), West (запад - левая сторона) и Center (по центру). Например, значение nw указывает на верхний левый угол;
● side: выравнивает виджет по одной из сторон контейнера. Может принимать значения: TOP (по умолчанию, выравнивается по верхней стороне контейнера), BOTTOM (выравнивание по нижней стороне), LEFT (выравнивание по левой стороне), RIGHT (выравнивание по правой стороне);
● ipadx: устанавливает отступ содержимого виджета от его границы по горизонтали;
● ipady: устанавливают отступ содержимого виджета от его границы по вертикали;
● padx: устанавливает отступ виджета от границ контейнера по горизонтали;
● pady: устанавливает отступ виджета от границ контейнера по вертикали.'''

            label_text = Text(pack_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', width = 42, height = 25,  wrap = 'word')
            label_text.place(x = 20, y = 50)
            label_text.insert(END, text1)
            label_text['state'] = 'disabled'
        
        # function-6
        def place_1():
            place_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            place_frame.place(x = 205, y = 40)

            place_label = Label(place_frame, text = 'Метод .place()', bg = '#fff', font = 'Calibri 14 bold')
            place_label.place(x = 140, y = 10)

            text1 = '''Метод place() позволяет более точно настроить координаты и размеры виджета. Он принимает следующие параметры:
● height и width: устанавливают соответственно высоту и ширину элемента в пикселях;
● relheight и relwidth: также задают соответственно высоту и ширину элемента, но в качестве значения используется число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера;
● x и y: устанавливают смещение элемента по горизонтали и вертикали в пикселях соответственно относительно верхнего левого угла контейнера;
● relx и rely: также задают смещение элемента по горизонтали и вертикали, но в качестве значения используется число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера;
● bordermode: задает формат границы элемента. Может принимать значение INSIDE (по умолчанию) и OUTSIDE;
● anchor: устанавливает опции растяжения элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, c, которые являются сокращениями от North(север - вверх), South (юг - низ), East (восток - правая сторона), West (запад - левая сторона) и Center (по центру). Например, значение nw указывает на верхний левый угол.'''
            place_text = Text(place_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', width = 42, height = 25,  wrap = 'word')
            place_text.place(x = 20, y = 50)
            place_text.insert(END, text1)
            place_text['state'] = 'disabled'


        # function-7
        def grid_1():
            grid_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            grid_frame.place(x = 205, y = 40)

            grid_label = Label(grid_frame, text = 'Метод .grid()', bg = '#fff', font = 'Calibri 14 bold')
            grid_label.place(x = 140, y = 10)

            text1 = '''Метод grid() позволяет поместить виджет в определенную ячейку условной сетки или грида.Метод grid применяет следующие параметры:
● column: номер столбца, отсчет начинается с нуля;
● row: номер строки, отсчет начинается с нуля;
● columnspan: сколько столбцов должен занимать элемент;
● rowspan: сколько строк должен занимать элемент;
● ipadx и ipady: отступы по горизонтали и вертикали соответственно от границ элемента до его содержимого;
● padx и pady: отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ элемента;
● sticky: выравнивание элемента в ячейке, если ячейка больше элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, которые указывают соответствующее направление выравнивания.'''

            grid_text = Text(grid_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', width = 42, height = 25,  wrap = 'word')
            grid_text.place(x = 20, y = 50)
            grid_text.insert(END, text1)
            grid_text['state'] = 'disabled'
        
        # function-8
        def label():
            label_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            label_frame.place(x = 205, y = 40)

            label_label = Label(label_frame, text = 'Виджет Label', bg = '#fff', font = 'Calibri 14 bold')
            label_label.place(x = 140, y = 10)

            text1 = '''Виджет Label представляет текстовую метку. Этот элемент позволяет выводить статический текст без возможности редактирования.Для создания элемента Label применяется конструктор, который принимает два параметра:'''
            label1_text = Text(label_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 5)
            label1_text.place(x = 20, y = 50)
            label1_text.insert(END, text1)
            label1_text['state'] = 'disabled'

            text2 = 'переменная = Label(master, options)'
            label2_text = Text(label_frame, bd = 0, bg = 'black', fg = '#fff', font = 'Calibri 12 bold', wrap = 'word', width = 45, height = 1)
            label2_text.place(x = 20, y = 150)
            label2_text.insert(END, text2)
            label2_text['state'] = 'disabled'

            text3 = '''Параметр master представляет ссылку на родительский контейнер, а параметр options представляет следующие именованные параметры
● background: фоновый цвет;
● borderwidth: толщина границы метки;
● cursor: курсор указателя мыши при наведении на метку;
● font: шрифт текста;
● foreground: цвет текста;
● height: высота виджета;
● image: ссылка на изображение, которое отображается на метке;
● justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю;
● pading: отступы от границ вилжета до его текста;
● text: устанавливает текст метки;
● textvariable: устанавливает привязку к элементу StringVar;
● width: ширина виджета.'''
            label3_text = Text(label_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 20)
            label3_text.place(x = 20, y = 170)
            label3_text.insert(END, text3)
            label3_text['state'] = 'disabled'


        # function-9
        def entry():
            entry_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            entry_frame.place(x = 205, y = 40)

            entry_label = Label(entry_frame, text = 'Виджет Entry', bg = '#fff', font = 'Calibri 14 bold')
            entry_label.place(x = 140, y = 10)

            text1 = '''Элемент Entry представляет поле для ввода текста. С помощью конструктора Entry можно установить ряд параметров, основные из них:
● background: фоновый цвет;
● cursor: курсор указателя мыши при наведении на текстовое поле;
● foreground: цвет текста;
● font: шрифт текста;
● justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю;
● show: задает маску для вводимых символов;
● state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED;
● textvariable: устанавливает привязку к элементу StringVar;
● width: ширина элемента;
Элемент Entry имеет ряд методов. Основные из них:
● insert(index, str): вставляет в текстовое поле строку по определенному индексу;
● get(): возвращает введенный в текстовое поле текст;
● delete(first, last=None): удаляет символ по индексу first. Если указан параметр last, то удаление производится до индекса last. Чтобы удалить до конца, в качестве второго параметра можно использовать значение END;
● focus(): установить фокус на текстовое поле.'''
            entry_text = Text(entry_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 25)
            entry_text.place(x = 20, y = 50)
            entry_text.insert(END, text1)
            entry_text['state'] = 'disabled'

        
        # function-10
        def text():
            text_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            text_frame.place(x = 205, y = 40)

            text_label = Label(text_frame, text = 'Виджет Text', bg = '#fff', font = 'Calibri 14 bold')
            text_label.place(x = 140, y = 10)

            text1 = '''Text предназначен для отображения и редактирования многострочного текста. Стоит отметить, что данный виджет доступен только в основном пакете tkinter, в пакете tkinter.ttk аналога нет.Основные параметры конструктора Text:
● bd / borderwidth: толщина границы;
● bg/background: фоновый цвет;
● fg/foreground: цвет текста;
● font: шрифт текста, например, font="Arial 14" - шрифт Arial высотой 14px, или font=("Verdana", 13, "bold") - шрифт Verdana высотой 13px с выделением жирным;
● height: высота в строках;
● padx: отступ от границ кнопки до ее текста справа и слева;
● pady: отступ от границ кнопки до ее текста сверху и снизу;
● relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE;
● state: устанавливает состояние кнопки, может принимать значения DISABLED, ACTIVE, NORMAL (по умолчанию);
● width: ширина в символах;
● wrap: указывает, каким образом переносить текст, если он не вмещается в границы виджета.'''
            text_text = Text(text_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 25)
            text_text.place(x = 20, y = 50)
            text_text.insert(END, text1)
            text_text['state'] = 'disabled'

        # function-11
        def check():
            check_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            check_frame.place(x = 205, y = 40)

            check_label = Label(check_frame, text = 'Checkbutton', bg = '#fff', font = 'Calibri 14 bold')
            check_label.place(x = 140, y = 10)

            text1 = '''Элемент Checkbutton представляет собой флажок, который может находиться в двух состояниях: отмеченном и неотмеченном.Конструктор Checkbutton принимает ряд параметров, отметим основные из них:
● command: ссылка на функцию, которая вызывается при нажатии на флажок;
● cursor: курсор при наведении на элемент;
● image: графическое изображение, отображаемое на элементе;
● offvalue: значение флажка в неотмеченном состоянии, по умолчанию равно 0;
● onvalue: значение флажка в отмеченном состоянии, по умолчанию равно 1;
● padding: отступы от текста до границы флажка;
● state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE ;
● text: текст элемента;
● textvariable: привязанный к тексту объект StringVar;
● underline: индекс подчеркнутого символа в тексте флажка;
● variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка;
● width: ширина элемента.'''

            check_text = Text(check_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 26)
            check_text.place(x = 20, y = 50)
            check_text.insert(END, text1)
            check_text['state'] = 'disabled'


        # function-12
        def radio():
            radio_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            radio_frame.place(x = 205, y = 40)

            radio_label = Label(radio_frame, text = 'Radiobutton', bg = '#fff', font = 'Calibri 14 bold')
            radio_label.place(x = 140, y = 10)

            text1 = '''Виджет Radiobutton представляет переключатель, который может находиться в двух состояниях: отмеченном или неотмеченном. Но в отличие от Checkbutton переключатели могут создавать группу, из которой одномоментно мы можем выбрать только один переключатель.Среди параметров конструктора Radiobutton стоит выделить следующие:
● command: ссылка на функцию, которая вызывается при нажатии на переключатель;
● cursor: курсор при наведении на виджет;
● image: графическое изображение, отображаемое виджетом;
● padding: отступы от содержимого до границы переключателя;
● state: состояние виджета, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE;
● text: текст виджета;
● textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя;
● underline: индекс подчеркнутого символа в тексте виджета;
● variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя;
● value: значение переключателя;
● width: ширина виджета.'''

            radio_text = Text(radio_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 26)
            radio_text.place(x = 20, y = 50)
            radio_text.insert(END, text1)
            radio_text['state'] = 'disabled'


        # function-13
        def frame():
            frame_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            frame_frame.place(x = 205, y = 40)

            frame_label = Label(frame_frame, text = 'Frame', bg = '#fff', font = 'Calibri 14 bold')
            frame_label.place(x = 140, y = 10)

            text1 = '''Каждый виджет, кроме окна, располагается в определенном родительском контейнере.
 И для каждого виджета можно явным образом установить контейнер с помощью первого параметра конструктора, который называтся master.
 Frame отображает прямоугольник и обычно применяется для организации интерфейса в отдельные блоки. Некоторые основные параметры, которые мы можем установить через конструктор класса Frame:
● borderwidth: толщина границы фрейма, по умолчанию равно 0;
● relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE;
● cursor: устанавливает курсор при наведении на фрейм;
● height: высота фрейма;
● width: ширина фрейма;
● padding: отступы от вложенного содержимого до границ фрейма;
Frame - это виджет в Tkinter, который позволяет создавать контейнеры для других виджетов и группировать их вместе внутри окна. Фреймы можно использовать для организации интерфейса приложения, чтобы сделать его более понятным и легко управляемым.'''

            frame_text = Text(frame_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 26)
            frame_text.place(x = 20, y = 50)
            frame_text.insert(END, text1)
            frame_text['state'] = 'disabled'

        # function-14
        def List():
            list_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            list_frame.place(x = 205, y = 40)

            list_label = Label(list_frame, text = 'Listbox', bg = '#fff', font = 'Calibri 14 bold')
            list_label.place(x = 140, y = 10)

            text1 = '''Виджет Listbox в tkinter представляет список объектов. Стоит отметить, что данный виджет присутствует только в пакете tkinter, а в пакете tkinter.ttk для него нет аналогов.Для настройки Listbox мы можем указать в его конструкторе следующие параметры:
● listvariable: список элементов, которые добавляются в ListBox;
● bg: фоновый цвет;
● bd: толщина границы вокруг элемента;
● cursor: курсор при наведении на Listbox;
● font: настройки шрифта;
● fg: цвет текста;
● highlightcolor: цвет элемента, когда он получает фокус;
● highlightthickness: толщина границы элемента, когда он находится в фокусе;
● relief: устанавливает стиль элемента, по умолчанию имеет значение SUNKEN;
● selectbackground: фоновый цвет для выделенного элемента;
● selectmode: определяет, сколько элементов могут быть выделены. Может принимать следующие значения: BROWSE, SINGLE, MULTIPLE, EXTENDED. Например, если необходимо включить множественное выделение элементов, то можно использовать значения MULTIPLE или EXTENDED.;
● height: высота элемента в строках. По умолчанию отображает 10 строк;
● width: устанавливает ширину элемента в символах. По умолчанию ширина - 20 символов;
● xscrollcommand: задает горизонтальную прокрутку;
● yscrollcommand: устанавливает вертикальную прокрутку.'''

            list_text = Text(list_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 26)
            list_text.place(x = 20, y = 50)
            list_text.insert(END, text1)
            list_text['state'] = 'disabled'


        # function-15
        def combo():
            combo_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            combo_frame.place(x = 205, y = 40)

            combo_label = Label(combo_frame, text = 'Combobox', bg = '#fff', font = 'Calibri 14 bold')
            combo_label.place(x = 140, y = 10)

            text1 = '''Виджет Combobox представляет выпадающий список, из которого пользователь может выбрать один элемент. Фактически он представляет комбинацию виджетов Entry и Listbox.Основные параметры конструктора Combobox:
● values: список строк для отображения в Combobox;
● background: фоновый цвет;
● cursor: курсор указателя мыши при наведении на текстовое поле;
● foreground: цвет текста;
● font: шрифт текста;
● justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю;
● show: задает маску для вводимых символов;
● state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED;
● textvariable: устанавливает привязку к элементу StringVar;
● height: высота элемента;
● width: ширина элемента.'''

            combo_text = Text(combo_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 26)
            combo_text.place(x = 20, y = 50)
            combo_text.insert(END, text1)
            combo_text['state'] = 'disabled'


        # function-16
        def menu_1():
            menu_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            menu_frame.place(x = 205, y = 40)

            menu_label = Label(menu_frame, text = 'Menu', bg = '#fff', font = 'Calibri 14 bold')
            menu_label.place(x = 140, y = 10)

            text1 = '''Для создания иерархического меню в tkinter применяется виджет Menu. Основные параметры Menu:
● activebackground: цвет активного пункта меню;
● activeborderwidth: толщина границы активного пункта меню;
● activeforeground: цвет текста активного пункта меню;
● background / bg: фоновый цвет;
● bd: толщина границы;
● cursor: курсор указателя мыши при наведении на меню;
● disabledforeground: цвет, когда меню находится в состоянии DISABLED;
● font: шрифт текста;
● foreground / fg: цвет текста;
● tearoff: меню может быть отсоединено от графического окна. В частности, при создании подменю а скриншоте можно увидеть прерывающуюся линию в верху подменю, за которую его можно отсоединить. Однако при значении tearoff=0 подменю не сможет быть отсоединено.
Меню может содержать много элементов, причем эти элементы сами могут представлять меню и содержать другие элементы. В зависимости от того, какой тип элементов мы хотим добавить в меню, будет отличаться метод, используемый для их добавления. В частности, нам доступны следующие методы:
● add_command(options): добавляет элемент меню через параметр options;
● add_cascade(options): добавляет элемент меню, который в свою очередь может представлять подменю;
● add_separator(): добавляет линию-разграничитель;
● add_radiobutton(options): добавляет в меню переключатель;
● add_checkbutton(options): добавляет в меню флажок.'''

            menu_text = Text(menu_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 26)
            menu_text.place(x = 20, y = 50)
            menu_text.insert(END, text1)
            menu_text['state'] = 'disabled'


        # function-17
        def note():
            note_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            note_frame.place(x = 205, y = 40)

            note_label = Label(note_frame, text = 'Notebook', bg = '#fff', font = 'Calibri 14 bold')
            note_label.place(x = 140, y = 10)

            text1 = '''Виджет Notebook представляет набор вкладок. Среди параметров виджета следует выделить следующие:
● width: ширина виджета;
● height: высота виджета;
● cursor: курсор при наведении на виджет;
● padding: отступы от границ виджета до его содержимого;
● style: стиль виджета.
Для управления вкладками Notebook предоставляет ряд методов, в частности, для добавления вкладки применяется метод add().Параметры метода:
● child: добавляемый виджет, для которого собственно и создается вкладка. Обычно это Frame, который затем добавляет другие виджеты;
● state: состояние вкладки. Возможные значения: "normal", "disabled", "hidden";
● sticky: определяет прикрепление виджета к определенной стороне вкладки;
● padding: отступы от границ вкладки до внутреннего содержимого;
● text: заголовок вкладки;
● image: изображение в заголовке вкладке;
● compound: управляет расположением изображения и текста в заголовке вкладки;
● underline: определяет номер подчеркнутого символа в заголовке вкладки.'''

            note_text = Text(note_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 27)
            note_text.place(x = 20, y = 50)
            note_text.insert(END, text1)
            note_text['state'] = 'disabled'


        # function-18
        def canvas():
            canvas_frame = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#fff')
            canvas_frame.place(x = 205, y = 40)

            canvas_label = Label(canvas_frame, text = 'Canvas', bg = '#fff', font = 'Calibri 14 bold')
            canvas_label.place(x = 140, y = 10)
        
            text1 = '''Виджет Canvas предоставляет возможности рисования двухмерных фигур. Стоит отметить, что Canvas есть только в пакете tkinter, а в пакете tkinter.ttk аналог отсутствует.Некоторые основные параметры Canvas:
● bg / background: фоновый цвет;
● bd / border: граница;
● borderwidth: толщина границы;
● cursor: курсор;
● height: высота виджета;
● width: ширина виджета.
Для двухмерного рисования Canvas предоставляет ряд методов:
● create_line(): рисует линию;
● create_rectangle(): рисует прямоугольник;
● create_oval(): рисует овал;
● create_arc(): рисует дугу;
● create_polygon(): рисует многоугольник;
● create_text(): добавляет текст;
● create_image(): добавляет изображение;
● create_window(): добавляет виджет.'''

            canvas_text = Text(canvas_frame, bd = 0, bg = '#fff', fg = 'black', font = 'Calibri 12 normal', wrap = 'word', width = 45, height = 27)
            canvas_text.place(x = 20, y = 50)
            canvas_text.insert(END, text1)
            canvas_text['state'] = 'disabled'


        root.title('Руководство по Tkinter')
        root.iconphoto(0, PhotoImage(file = 'icon_python.png'))

        new_frame = Frame(root, width = 600, height = 640, bg = '#003D51')
        new_frame.place(x = 0, y = 0)

        py_frame = Frame(new_frame, width = 600, height = 40, bg = '#003D51', bd = 0)
        py_frame.place(x = 0, y = 0)


        lbl_py = Label(py_frame, text = 'Учим PYTHON', bg = '#003D51', bd = 0, fg = '#fff', font = 'Calibri 14 bold')
        lbl_py.place(x = 20, y = 8)

        lbl_p = Label(py_frame, text = 'Tkinter', bg = '#003D51', bd = 0, fg = '#fff', font = 'Calibri 14 bold')
        lbl_p.place(x = 280, y = 8)

        menubutton = Menubutton(py_frame, text = 'Настройки ⁝', bg = '#003D51', fg = '#fff',
                          font = 'Calibri 14 bold', bd = 0, activebackground='#003D51',
                          activeforeground='#fff', cursor = 'hand2')
        menubutton.place(x = 490, y = 5)

        menu = Menu(menubutton, tearoff=0, bg = '#fff', bd = 0, cursor = 'hand2', font = 'Calibri 12 normal', 
                    activebackground='blue')
        menu.add_command(label='Мой аккаунт', command = Info)
        menu.add_command(label='О программе', command = Program)
        menu.add_command(label='Помощь', command = Help)
        menu.add_command(label='Выход аккаунт', command = Destroy)
        menu.add_command(label='Удалить аккаунт', command = Delete)
        menu.add_command(label='Закрыть', command = Close)

        menubutton.config(menu=menu)


        new_win_1 = Frame(new_frame, width = 200, height = 570, bg = '#fff')
        new_win_1.place(x = 0, y = 40)

        # button-1
        btn_tk = Button(new_win_1, text = '1.Введение Tkinter ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = tk_info)
        btn_tk.place(x = 10, y = 10)
        
        # button-2
        btn_win = Button(new_win_1, text = '2.Создание окна ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = win_info)
        btn_win.place(x = 10, y = 40)

        #button-3
        btn_widget = Button(new_win_1, text = '3.Виджеты ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = widget)
        btn_widget.place(x = 10, y = 70)

        #button-4
        btn_but = Button(new_win_1, text = '4.Кнопки ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = button)
        btn_but.place(x = 10, y = 100)

        #button-5
        btn_pack = Button(new_win_1, text = '5.Метод .pack() ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = pack_1)
        btn_pack.place(x = 10, y = 130)

        #button-6
        btn_place = Button(new_win_1, text = '6.Метод .place() ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = place_1)
        btn_place.place(x = 10, y = 160)

        #button-7
        btn_grid = Button(new_win_1, text = '7.Метод .grid() ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = grid_1)
        btn_grid.place(x = 10, y = 190)

        #button-8
        btn_label = Button(new_win_1, text = '8.Виджет Label ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = label)
        btn_label.place(x = 10, y = 220)

        #button-9
        btn_entry = Button(new_win_1, text = '9.Виджет Entry ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = entry)
        btn_entry.place(x = 10, y = 250)

        #button-10
        btn_text = Button(new_win_1, text = '10.Виджет Text ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = text)
        btn_text.place(x = 10, y = 280)

        #button-11
        btn_check = Button(new_win_1, text = '11.Checkbutton ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = check)
        btn_check.place(x = 10, y = 310)

        #button-12
        btn_radio = Button(new_win_1, text = '12.Radiobutton ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = radio)
        btn_radio.place(x = 10, y = 340)

        #button-13
        btn_frame = Button(new_win_1, text = '13.Frame ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = frame)
        btn_frame.place(x = 10, y = 370)

        #button-14
        btn_list = Button(new_win_1, text = '14.Listbox ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = List)
        btn_list.place(x = 10, y = 400)

        #button-15
        btn_combo = Button(new_win_1, text = '15.Combobox ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = combo)
        btn_combo.place(x = 10, y = 430)

        #button-16
        btn_menu = Button(new_win_1, text = '16.Menu ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = menu_1)
        btn_menu.place(x = 10, y = 460)

        #button-17
        btn_note = Button(new_win_1, text = '17.Notebook ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = note)
        btn_note.place(x = 10, y = 490)

        #button-18
        btn_canvas = Button(new_win_1, text = '18.Canvas ▶', bd = 0, fg = 'blue', bg = '#fff', 
                            font = 'Calibri 14 bold', activebackground = '#fff', cursor = 'hand2',
                            activeforeground = 'blue', command = canvas)
        btn_canvas.place(x = 10, y = 520)


        new_win_2 = Frame(new_frame, width = 400, height = 570, bd = 0, bg = '#003D51')
        new_win_2.place(x = 200, y = 40)
        
        lbl_phone = Label(new_frame, text = 'Контактный номер: 8 771 585 62 25 \t Github:', 
                          bg = '#003D51', bd = 0, fg = '#fff', font = 'Calibri 10 bold', )
        lbl_phone.place(x = 10, y = 616)


        git = Label(new_frame, text = 'https://github.com/Erezhep', 
                          bg = '#003D51', bd = 0, fg = '#fff', font = 'Calibri 10 bold')
        git.place(x = 280, y = 616)

        frame_tk = Frame(new_win_2, width = 395, height = 570, bg = '#fff', bd = 0)
        frame_tk.place(x = 5, y = 0)

    # Второй окно внутр главного окна
    new_Frame = Frame(root, width = 600, height = 640, bg = '#E9EDF6', bd = 0)
    new_Frame.place(x = 0, y = 0)
    root.title('Авторизация')

    icon_img = PhotoImage(file = 'reistr.png')
    root.iconphoto(0, icon_img)
     
    login_frame = Frame(new_Frame, width = 550, height = 500, bg = '#fff', bd = 0)
    login_frame.place(x = 25, y = 60)

    avto_lbl = Label(login_frame, text = 'Авторизация', fg = 'black', bg = '#fff', font = 'Calibri 30 bold')
    avto_lbl.pack(padx = 50, pady=10)

    entry_name = Entry(login_frame, width = 22, bd = 0, font = 'Calibri 20 normal', fg = '#B3B3B3')
    entry_name.pack(padx = 150, pady = 70)
    entry_name.insert(0, 'Логин')
    entry_name.bind('<FocusIn>', on_focus)
    entry_name.bind('<FocusOut>', off_focus)

    frame_hr = Frame(login_frame, width=250, height = 2, bg = 'black')
    frame_hr.place(x = 150, y = 180)

    entry_password = Entry(login_frame, width = 22, bd = 0, show = '',
                            font = 'Calibri 20 normal', fg = '#B3B3B3')
    entry_password.pack(padx = 150, pady = 0)
    entry_password.insert(0, 'Пароль')
    entry_password.bind('<FocusIn>', on_pass)
    entry_password.bind('<FocusOut>', off_pass)

    frame1_hr = Frame(login_frame, width=250, height = 2, bg = 'black')
    frame1_hr.place(x = 150, y = 285)

    account = Label(login_frame, text = 'У вас нет аккаунт?', bg = '#fff', font = 'Calibri 12 normal')
    account.place(x = 150, y = 300)

    btn_registr = Button(login_frame, text = 'Регистрация', font = 'Calibri 12 normal', cursor = 'hand2',
                          bg = '#fff', bd = 0, activebackground = '#fff', fg = 'blue', 
                          activeforeground = 'blue', command = reg)
    btn_registr.place(x = 285, y = 298)

    btn_sign_in = Button(login_frame, text = 'Войти', font = 'Calibri 14 normal', 
                          bg = 'gray', activebackground = 'gray', fg = 'blue', cursor = 'hand2',
                          activeforeground = 'blue', bd = 0, width=30, command = test)
    btn_sign_in.place(x = 120, y = 350)

    thank_you = Label(login_frame, text = 'Спасибо, что выбрали нас!', bg = '#fff', bd = 0, font = 'Arial 14 normal')
    thank_you.place(x = 150, y = 425)

    login_frame.pack_propagate(0)

    help = Label(new_Frame, text = 'Помощь и поддержка:', bd = 0, bg = '#E9EDF6', font = 'Arial 10 bold')
    help.place(x = 110, y = 590)

    help_url = Label(new_Frame, text="bekaryserezep05@gmail.com", font = 'Arial 10 bold', bd = 0, bg = '#E9EDF6', fg = 'blue', cursor = 'hand2')
    help_url.place(x = 260,y = 590)

def on_closing(): 
    if askokcancel("Выход", "Вы действительно хотите закрыть окно?"):
        root.destroy()

# Главная окна для запуска
root = Tk()
root.title('Руководство по Tkinter')
root.geometry('600x640+50+40')
root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", on_closing)
root['bg'] = '#fff'

icon = PhotoImage(file = 'icon_python.png')
root.iconphoto(1, icon)

logo_python = PhotoImage(file = 'logo_python.png')

lbl_python = Label(root, text = 'Python', bg = '#fff', font = 'Calibri 60 bold')
lbl_python.place(x = 180, y = 50)

lbl = Label(root, image = logo_python, bg = '#fff')
lbl.pack(padx = 120, pady = 165)

lbl_tk = Label(root, text = 'Руководство по Tkinter', font = 'Calibri 20 normal', bg = '#fff')
lbl_tk.place(x = 160, y = 450)

root.after(2000, new_window)

root.mainloop()
