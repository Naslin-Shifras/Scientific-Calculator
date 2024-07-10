from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title('seintific calculator')
        master.geometry('406x324')
        master.config(bg='gray15')
        master.resizable(True, True)

        self.equation = StringVar()
        self.entry_value = ''

#____________________________________entry________________________________________________

        entryField=Entry(root,font=('arial',20,'bold'),bg='cornsilk3',relief='sunken', bd=5,width=23, textvariable=self.equation)
        entryField.grid(row=0,column=0,columnspan=7)




#__________________________________first row______________________________________________

        root.rowconfigure(1,minsize=4)#space between row



        button=Button(root,width=3,text='C',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='Orange',activebackground='dimgray',command=self.clear)
        button.grid(row=2,column=0)

        button=Button(root,width=3,text='CE',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='orange',activebackground='dimgray',command=self.delete)
        button.grid(row=2,column=1)
        
        button=Button(root,width=3,text='(',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('('))
        button.grid(row=2,column=2)

        button=Button(root,width=3,text=')',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show(')'))
        button.grid(row=2,column=3)

        button=Button(root,width=3,text='MC',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('MC'))
        button.grid(row=2,column=4)

        button=Button(root,width=3,text='M+',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('M+'))
        button.grid(row=2,column=5)

        button=Button(root,width=3,text='M-',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('M-'))
        button.grid(row=2,column=6)

        button=Button(root,width=3,text='MR',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('MR'))
        button.grid(row=2,column=7)

    #_________________________________second row______________________________________________
    
        root.rowconfigure(3,minsize=4)#row space



        button=Button(root,width=3,text='1/x',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('1/x'))
        button.grid(row=4,column=0)

        button=Button(root,width=3,text='x\u00B2',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('x\u00B2'))
        button.grid(row=4,column=1)
        
        button=Button(root,width=3,text='x\u00B3',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('x\u00B3'))
        button.grid(row=4,column=2)

        button=Button(root,width=3,text='x\u02B8',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('x\u02B8'))
        button.grid(row=4,column=3)

        button=Button(root,width=3,text=chr(177),font=('arial',15,'bold'),relief='groove',bg='brown4',
              fg='white',activebackground='brown4',command=lambda : self.show('chr(177)'))
        button.grid(row=4,column=4)

        button=Button(root,width=3,text='%',font=('arial',15,'bold'),relief='groove',bg='brown4',
              fg='white',activebackground='brown4',command=lambda : self.show('%'))
        button.grid(row=4,column=5)

        button=Button(root,width=3,text=chr(247),font=('arial',15,'bold'),relief='groove',bg='brown4',
              fg='white',activebackground='brown4',command=lambda : self.show('chr(247)'))
        button.grid(row=4,column=6)

        button=Button(root,width=3,text='*',font=('arial',15,'bold'),relief='groove',bg='brown4',
              fg='white',activebackground='brown4',command=lambda : self.show('*'))
        button.grid(row=4,column=7)


#_________________________________3rd row______________________________________________
    
        root.rowconfigure(5,minsize=4)#row space


        button=Button(root,width=3,text='x!',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('x!'))
        button.grid(row=6,column=0)

        button=Button(root,width=3,text='√',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('√'))
        button.grid(row=6,column=1)
        
        button=Button(root,width=3,text='\u221B',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('\u221B'))
        button.grid(row=6,column=2)

        button=Button(root,width=3,text='log',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('log'))
        button.grid(row=6,column=3)

        button=Button(root,width=3,text='7',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(7))
        button.grid(row=6,column=4)

        button=Button(root,width=3,text='8',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(8))
        button.grid(row=6,column=5)

        button=Button(root,width=3,text='9',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(9))
        button.grid(row=6,column=6)

        button=Button(root,width=3,text='-',font=('arial',15,'bold'),relief='groove',bg='brown4',
              fg='white',activebackground='brown4',command=lambda : self.show('-'))
        button.grid(row=6,column=7)




#_________________________________4th row______________________________________________
    
        root.rowconfigure(7,minsize=4)#row space

        
        button=Button(root,width=3,text='sin',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('sin'))
        button.grid(row=8,column=0)

        button=Button(root,width=3,text='cos',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('cos'))
        button.grid(row=8,column=1)
        
        button=Button(root,width=3,text='tan',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('tan'))
        button.grid(row=8,column=2)

        button=Button(root,width=3,text='ln',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('ln'))
        button.grid(row=8,column=3)

        button=Button(root,width=3,text='4',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(4))
        button.grid(row=8,column=4)

        button=Button(root,width=3,text='5',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(5))
        button.grid(row=8,column=5)

        button=Button(root,width=3,text='6',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(6))
        button.grid(row=8,column=6)

        button=Button(root,width=3,text='+',font=('arial',15,'bold'),relief='groove',bg='brown4',
              fg='white',activebackground='brown4',command=lambda : self.show('+'))
        button.grid(row=8,column=7)
        

#_________________________________5th row______________________________________________
    
        root.rowconfigure(9,minsize=4)#row space

        
        
        button=Button(root,width=3,text='sinh',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('sinh'))
        button.grid(row=10,column=0)

        button=Button(root,width=3,text='cosh',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('cosh'))
        button.grid(row=10,column=1)
        
        button=Button(root,width=3,text='tanh',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('tanh'))
        button.grid(row=10,column=2)

        button=Button(root,width=3,text='e\u207Ex',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('e\u207Ex'))
        button.grid(row=10,column=3)

        button=Button(root,width=3,text='1',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(1))
        button.grid(row=10,column=4)

        button=Button(root,width=3,text='2',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(2))
        button.grid(row=10,column=5)

        button=Button(root,width=3,text='3',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show(3))
        button.grid(row=10,column=6)

        button=Button(root,width=3,height=3, text='=',font=('arial',15,'bold'),relief='groove',bg='red2',
              fg='white',activebackground='red3',command=self.solve)
        button.grid(row=10,column=7, rowspan=3)

        
#_________________________________6th row______________________________________________
    
        root.rowconfigure(11,minsize=4)#row space


        button=Button(root,width=3,text='rad',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('rad'))
        button.grid(row=12,column=0)

        button=Button(root,width=3,text='π',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('π'))
        button.grid(row=12,column=1)
        
        button=Button(root,width=3,text='2π',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('2π'))
        button.grid(row=12,column=2)

        button=Button(root,width=3,text='deg',font=('arial',15,'bold'),relief='groove',bg='dimgray',
              fg='white',activebackground='dimgray',command=lambda : self.show('deg'))
        button.grid(row=12,column=3)

        button=Button(root,width=8,text='0',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show('0'))
        button.grid(row=12,column=4, columnspan=2)

        button=Button(root,width=3,text='.',font=('arial',15,'bold'),relief='groove',bg='gray8',
              fg='white',activebackground='gray8',command=lambda : self.show('.'))
        button.grid(row=12,column=6)

    



    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def delete(self):
        if self.entry_value:
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.entry_value = str(result)
            self.equation.set(self.entry_value)
        except Exception as e:
            self.equation.set("Error")


root = Tk()
calculator = Calculator(root)
root.mainloop()
