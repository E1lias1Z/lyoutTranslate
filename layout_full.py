# данная программа подойдет для случаев, когда пишущий сообщение забыл 
# проверить раскладку клавиатуры, и после этого ему придется заново 
# переписывать набранное сообщение
# Данная программа переводит пока только английские символы на русские

from layout import coorrection, coorrection_shift
from tkinter import *
from tkinter import Text

#Класс основной программы MainProg--------------------------------------------
class MainProg:
    def __init__(self, height, width, title = 'Layout translate'):
        self.win = Tk()
        self.win.geometry('x'.join([str(width), str(height)]))
        self.win.title(title)
        self.win.resizable(width=False, height=False)
    def widgets(self):
        self.scrollText1()
        self.scrollText2()
        self.buttonTranslate()
        self.labels()
    def labels(self):
        Label(text="Ввод неправильной английской раскладки:", font="Arial 14").grid(row=0, column=0, padx = 20, pady=10)
        Label(text="Перевод на русскую раскладку:", font="Arial 14").grid(row=0, column=1, padx = 20, pady=10)
    def scrollText1(self):
        self.input_txt = StringVar()
        self.text1 = Text(self.win, width=25, height=8, font='Arial 14') #текстовое окно для ввода
        self.text1.grid(row=1, column=0, padx=5, pady=5)
        #scrollbar1 = Scrollbar(text1, orient=VERTICAL)
    def scrollText2(self):
        self.text2 = Text(self.win, width=25, height=8, state=DISABLED, font='Arial 14') #текстовое окно для вывода
        self.text2.grid(row=1, column=1, padx=27)
    def translateMesg(self):
        message = self.text1.get('1.0', END)
        for w in message:
            if(w in coorrection.keys()):
                message = message.replace(w, coorrection[w])
            elif(w in coorrection_shift.keys()):
                message = message.replace(w, coorrection_shift[w])
        self.text2.config(state='normal')
        self.text2.delete('1.0', END)
        self.text2.insert(END, message)
        self.text2.config(state=DISABLED)
    def clearLabels(self):
        self.text1.delete('1.0', END)
        self.text2.config(state='normal')
        self.text2.delete('1.0', END)
        self.text2.config(state=DISABLED)
    def buttonTranslate(self):
        butt_trans = Button(self.win, text='Перевести', command=self.translateMesg).place(x=360, y=240)
        butt_clear = Button(self.win, text='Очистить', command=self.clearLabels).place(x=364, y=280)
    def run(self):
        self.widgets()
        self.win.mainloop()
#-------------------------------------------------------------------------------------------------------
myApp = MainProg(320, 800, title='Layout Translator')
myApp.run()