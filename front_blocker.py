from tkinter import *
from tkinter import ttk
import time
from datetime import datetime as dt
import tkinter.messagebox
import sys, os, threading,psutil


global hI,hF,mI,mF, website_list

website_list=[]

def center_window_inicio(w,h):
    # get screen width and height
    ws = inicio.winfo_screenwidth()
    hs = inicio.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    inicio.geometry('%dx%d+%d+%d' % (w, h, x, y))

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple)
        print (selected_tuple)
    except IndexError:
        pass

def add_command():
    #backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),qtd_text.get(),path_text.get())
    #list1.delete(0,END)
    if  str(site_text.get()) and not site_text.get()=="":
        list1.insert(END,(site_text.get()))
        salvar()
        load()
    else:
        tkinter.messagebox.showwarning("Bloqueador de sites", "Informe um site")
    

def deletar():   
    try:
        global selected_tuple
        index=list1.curselection()[0]
        list1.delete(index)
        salvar()
        load()
    except IndexError: 
        pass

def pegar():

    try:
        # Pega as variáveis do front_blocker e encerra para rodar o exemplo.pyw
        global hI,hF,mI,mF
        hI=int(combo_hourI.get())
        hF=int(combo_hourF.get())
        mI=int(combo_minI.get())
        mF=int(combo_minF.get())

        with open(r"C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\12 Application 3 Building a Website Blocker\app3\lista.txt","r") as file:
            #print(file.read())
            global website_list
            website_list=file.read().splitlines()
            #print(website_list)
        
        sair()
    except ValueError:
       tkinter.messagebox.showwarning("Bloqueador de sites","Selecione os horários")
 
def salvar():
     with open(r"lista.txt","w") as file:
        #file.seek(0)
        for iten in range(0,list1.size()):
            selected_tuple = list1.get(iten)
            file.write(selected_tuple+"\n")

        
def load():
    with open(r"C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\12 Application 3 Building a Website Blocker\app3\lista.txt","r") as file:
        #print(file.read())
        list1.delete(0,END)
        website_list=file.read().splitlines()
        for site in range(0,len(website_list)):
            list1.insert(END,website_list[site])

        

def encerrar():
    lista=[]
    lista_PID=[]
    print("*** Iterate over all running process and print process ID & Name ***")
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            pinfo = proc.memory_info().vms / (1024 * 1024)
            if processName == "exemplo.exe":
                lista.append([processName,processID,pinfo])
                #print(processName , ' ::: ', processID,pinfo)
            if processName == "exemplo.exe":
                lista_PID.append(processID)
                #print(str(processID) + " background")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print('*** Create a list of all running processes ***')
    #print(lista_PID)
    #print(lista_PID2)
    for pid in lista_PID:
        p=psutil.Process(pid)
        print("Encerrando o processo " + str(pid))
        p.kill()
        

    
def limpar():

    lista=[]
    lista_PID=[]
    print("*** Iterate over all running process and print process ID & Name ***")
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            pinfo = proc.memory_info().vms / (1024 * 1024)
            if processName == "exemplo.exe":
                lista.append([processName,processID,pinfo])
                #print(processName , ' ::: ', processID,pinfo)
            if processName == "exemplo.exe":
                lista_PID.append(processID)
                #print(str(processID) + " background")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print('*** Create a list of all running processes ***')
    #print(lista_PID)
    #lista_PID2=lista_PID[1:len(lista_PID)-1]
    #print(lista_PID2)

    hosts_temp="hosts"
    hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
    redirect="127.0.0.1"

    with open(r"C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\12 Application 3 Building a Website Blocker\app3\lista.txt","r") as file:
            #print(file.read())
            global website_list
            website_list=file.read().splitlines()

    
    with open(hosts_path,'r+') as file:
        #content vira uma lista com readlines
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

    for pid in lista_PID:
        p=psutil.Process(pid)
        print("Encerrando o processo " + str(pid))
        p.kill()
       
def sair():
    print ("sair")
    inicio.destroy()

#inicia a janela
inicio=Tk()
inicio.wm_title("Bloqueador de sites")
inicio.resizable(0,0)


#chama a função para definir a geometria
#inicio.geometry("950x500")
center_window_inicio(500, 500) 


#loop para preencher box de horas e minutors 1 a 24 e 1 59
hour=[]
for i in range(1,25):
    hour.append(i)

minute=[]
for i in range(0,60):
    minute.append(i)

label_I=Label(inicio,text= "Início do trabalho")
label_I.place(x=60,y=10)
label_I=Label(inicio,text= "Horas")
label_I.place(x=50,y=30)
label_I=Label(inicio,text= "Minutos")
label_I.place(x=95,y=30)

# box_hour_I=StringVar(inicio)
# box=OptionMenu(inicio,box_hour_I,*hour)
# box.place(x=50,y=50)

combo_hourI=ttk.Combobox(inicio,values=hour)
combo_hourI.config(width=2)
combo_hourI.place(x=50,y=50)


hora_inicial=combo_hourI.get()
# box_minute_I=StringVar(inicio)
# box=OptionMenu(inicio,box_minute_I,*minute)
# box.place(x=100,y=50)

combo_minI=ttk.Combobox(inicio,values=minute)
combo_minI.config(width=5)
combo_minI.place(x=100,y=50)

label_F=Label(inicio,text= "Fim do trabalho")
label_F.place(x=210,y=10)

label_F=Label(inicio,text= "Horas")
label_F.place(x=200,y=30)
label_F=Label(inicio,text= "Minutos")
label_F.place(x=250,y=30)


combo_hourF=ttk.Combobox(inicio,values=hour)
combo_hourF.config(width=2)
combo_hourF.place(x=200,y=50)

combo_minF=ttk.Combobox(inicio,values=minute)
combo_minF.config(width=5)
combo_minF.place(x=250,y=50)


label_site=Label(inicio,text= "Digite o site:")
label_site.place(x=140,y=135)
site_text=StringVar()
e1=Entry(inicio, textvariable=site_text)
e1.config(width=30)
e1.place(x=80,y=160)

b1=Button (inicio, text="Adicionar site",width=12,command=add_command)
b1.place(x=380,y=160)

#Segunda lista - show
#Lista com somente os nomes dos produtos selecionados.
list1=Listbox(inicio, height=12, width=50)
#list11.grid(row=1,column=0,rowspan=6,columnspan=1)
list1.place(x=50,y=200)
list1.bind('<<ListboxSelect>>',get_selected_row)
list1['background']='white'

b3=Button (inicio, text="Remover site",width=12,command=deletar)
b3.place(x=380,y=250)

b2=Button (inicio, text="Ativar",width=12, bg="green", fg="white",command=pegar)
b2.place(x=80,y=450)

btn = Button(inicio, text="Limpar",width=12, bg="black", fg="white",command=limpar)
btn.place(x=200,y=450)

#carrega quando abre o formulário
load()

inicio.mainloop()
