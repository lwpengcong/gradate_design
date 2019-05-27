from tkinter import *
from tkinter import filedialog

import tkinter.messagebox
import os
import pandas as pd

import mlxtend_apriori
import sklearn_kmeans

def LoadingPage():

    top.title('基于大数据平台的故障态势分析软件')
    # top.geometry('300x300')
    photo = PhotoImage(file="d:\\py3.7_workspace\\gif\\test.gif") 
    Lab= Label(top,image= photo)
    Lab.pack()#设置主界面

    # 创建一个菜单项，类似于导航栏
    menubar=Menu(top)
    # 创建菜单项
    fmenu1=Menu(top,tearoff=0)
    fmenu1.add_command(label='导入',command=dataloading)
    fmenu1.add_separator()
    fmenu1.add_command(label='退出',command=top.quit)
    

    fmenu2=Menu(top,tearoff=0)
    fmenu2.add_command(label='查看编码结果',command=fault_identification_encoding)
    fmenu2.add_command(label='查看统计结果',command=fault_identification_counting)
    fmenu2.add_command(label='查看聚类结果',command=fault_identification_kmeans)
    fmenu2.add_command(label='查看分解结果',command=fault_identification_main)
    
    fmenu3=Menu(top,tearoff=0)
    fmenu3.add_command(label='查看频繁项集',command=fault_analysis_itemsets)
    fmenu3.add_command(label='查看关联规则',command=fault_analysis_rules)
    # add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
    # 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
    menubar.add_cascade(label="数据导入",menu=fmenu1)
    menubar.add_cascade(label="数据预处理",menu=fmenu2)
    menubar.add_cascade(label="关联规则分析",menu=fmenu3)

    # 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
    top.configure(menu=menubar)
    top.mainloop()

def dataloading():
    # second = Toplevel()
    # second.title('载入数据')
    file_path = filedialog.askopenfilename(title='打开文件', filetypes=[('csv', '*.csv'), ('All Files', '*')])
    
    if os.path.exists(file_path):
        kmeans.load_data(file_path)
        # second = Toplevel()
        # second.title('载入数据')
        tkinter.messagebox.showinfo('提示', '载入数据成功')
        # l = Label(top,text='成功')
        # l.pack(side='top')
        # tk.messagebox.showinfo(title='导入', message='成功导入')
        # pf = pd.read_csv(file_path)
        # text1 = Text(second)
        # text1.insert(INSERT,pf)
        # text1.pack()
    
    # text1 = Text(second)    
    # text1.insert(INSERT,mlxtend_apriori.frequent_itemsets)
    # text1.pack()

def fault_identification_encoding():
    second = Toplevel()
    second.title('查看编码结果')
    text1 = Text(second)    
    # filepath = 'd:/py3.7_workspace/data/encodering1.csv'
    text1.insert(INSERT,kmeans.encoding())
    text1.pack()

def fault_identification_counting():
    kmeans.account()
    # text1 = Text(second)    
    # text1.insert(INSERT,kmeans.account())
    # text1.pack()

def fault_identification_kmeans():
    second = Toplevel()
    second.title('查看聚类结果')
    Lab= Label(second,image= photo1)
    Lab.pack()#设置主界面

def fault_identification_main():
    second = Toplevel()
    second.title('查看分解结果')
    text1 = Text(second)    
    # filepath = 'd:/py3.7_workspace/data/encodering1.csv'
    text1.insert(INSERT,kmeans.faultdiv())
    text1.pack()
    apriori.load_data(kmeans.encoding_path)

def fault_analysis_itemsets():
    second = Toplevel()
    second.title('频繁项集')
    text1 = Text(second)    
    # filepath = 'd:/py3.7_workspace/data/encodering1.csv'
    text1.insert('end',apriori.itemsets())
    text1.pack()

def fault_analysis_rules():
    second = Toplevel()
    second.title('关联规则')
    text1 = Text(second)
    text1.insert('insert', '关联规则')    
    # filepath = 'd:/py3.7_workspace/data/encodering1.csv'
    text1.insert('end',apriori.rules())
    text1.pack()
 

if __name__ == "__main__":
    top = Tk()
    photo1 = PhotoImage(file="d:\\py3.7_workspace\\gif\\k-means.1.gif")
    kmeans = sklearn_kmeans.faultidentify()
    apriori = mlxtend_apriori.fault_analysis()
    LoadingPage()
    