from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by EtcallmomZ')
GUI.geometry('500x500+20+20')

##############Menu################################
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
#tearoof=การนำกล่องฟังค์ชั่นออก
menubar.add_cascade(label='Flie',menu=filemenu)
filemenu.add_command(label='Impoet csv')
#คือการสั่งให้ใส่ชื่อเมนูเข้าไป
#Help menu
def About():
    messagebox.showinfo('About','สวัสดีผู้มีอุปการะคุณทุกท่านโปรดทราบ\nไม่มีอะไรมากเดี้ยนแค่เหงาฮ้า')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
#donate menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
###################################################


Tab=ttk.Notebook(GUI)
T1=Frame(Tab)
T2=Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1=PhotoImage(file='dollar-icon.png')
icon_t2=PhotoImage(file='t_2icon.png')

Tab.add(T1,text=f'{"เพิ่มค่าใช้จ่าย":^{50}}',image=icon_t1,compound='right')
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด":^{50}}',image=icon_t2,compound='right')

F1 = Frame(T1)
#F1.place(x=520, y=50)
F1.pack()

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    piece = v_piece.get()

    if expense =='':
    	print('No data')
    	messagebox.showwarning('Error','กรุณากรอกข้อมูลรายการค่าใช้จ่าย')
    	return
    elif price =='':
    	print('No data')
    	messagebox.showwarning('Error','กรุณากรอกราคา')
    	return
    elif piece =='':
    	print('No data')
    	messagebox.showwarning('Error','กรุณากรอกจำนวนสินค้า')
    	return

     	
    try:
        total =float(price) * float(piece)
        dt = datetime.now()
        print(f'รายการ:{expense} ราคา:{price} บาท ทั้งหมด:{piece} ชิ้น รวมทั้งหมด:{total}บาท เวลา:{dt}')
        text=f'รายการ:{expense} ราคา:{price} บาท ทั้งหมด:{piece} ชิ้น\n'
        text=text+f'รวมทั้งหมด:{total}บาท เวลา:{dt}'
        v_output.set(text)
        v_expense.set('')
        v_price.set('')
        v_piece.set('')
        with open('snsd.csv', 'a', encoding='utf-8', newline='') as f:
            fw = csv.writer(f)
            data = [expense, price, piece, total, dt]
            fw.writerow(data)
        E1.focus()
        update_table()     
    except Exception as e: 
	        print('ERROR',e)
	        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
	        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
	        #messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
	        #สัญลักษณ์จะแต่งต่างกันไปในแต่ละคำสั่ง
	        v_expense.set('')
	        v_price.set('')
	        v_piece.set('')


GUI.bind('<Return>',Save)

Font1 = (None, 20)

moneyicon=PhotoImage(file='Money-icon.png')
money_icon=Label(F1,image=moneyicon).pack()
#----------------------------------------------------------
L = ttk.Label(F1, text='รายการค่าใช้จ่าย:', font=Font1).pack()
v_expense = StringVar()
E1 = ttk.Entry(F1, textvariable=v_expense,font=Font1)
E1.pack()
#----------------------------------------------------------
L = ttk.Label(F1, text='ราคา(บาท):', font=Font1).pack()
v_price = StringVar()
E2 = ttk.Entry(F1, textvariable=v_price,font=Font1).pack()
#----------------------------------------------------------
L = ttk.Label(F1, text='จำนวน(ชิ้น):', font=Font1).pack()
v_piece = StringVar()
E3 = ttk.Entry(F1, textvariable=v_piece,font=Font1).pack()


b1_icon=PhotoImage(file='Floppy-icon.png')
B1 = ttk.Button(F1, text='save',image=b1_icon,compound='left',command=Save)
B1.pack(ipadx=20, ipady=10)

v_output=StringVar()
v_output.set('---------ผลลัพธ์---------')
output=Label(F1,textvariable=v_output,font=Font1,foreground='red')
output.pack(ipady=20)
#-----------------------------------------------------------------
def read_csv():
    with open('snsd.csv',newline='',encoding='utf-8')as f:
        fr = csv.reader(f)
        data = list(fr)
        #print(fr)
    return data    
        #print(data)
        #for d in data:
        # print(d)

#rs=read_csv()
#print(rs)

L = ttk.Label(T2, text='ตารางแสดงผลลัพธ์ทั้งหมด', font=Font1).pack(ipady=10)

header =['รายการค่าใช้จ่าย','ราคา','จำนวน','รวมทั้งหมด','วัน-เวลา']
result= ttk.Treeview(T2,columns=header,show='headings',height=10)
result.pack()

#for i in range(len(header)):
#   result.heading(header[i],text=header[i])
#การแสดงบนคอลัมน์แบบที่1

for h in header:
    result.heading(h,text=h)

headerwidth = [90,80,80,130,170]
for h,w in zip (header,headerwidth):
    result.column(h,width=w)




def update_table():
    result.delete(*result.get_children())
    #get_children = แทนค่าข้อมูลลงไป
    data = read_csv()
    for d in data:
       result.insert('',0,value=d)
       #value = ข้อมูลที่ต้องการจะใส่ลงไป
       # 0 = ลำดับของข้อมูลที่ต้องการจะใส่ลงไป
   



update_table()


GUI.mainloop()
