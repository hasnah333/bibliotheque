from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from classBibleo import Book 
from connexion import connexion;
import io
mywin=Tk()
mywin.geometry("1000x650")
mywin.configure(bg="gray")
idlab=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="id book")
idlab.place(x=10,y=10);
Labeleautor=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="auteur")
Labeleautor.place(x=280,y=10);
labeltitle=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="title")
labeltitle.place(x=560,y=10);
labelanneparution=Label(mywin,fg="red" ,background="gray",font=('Calibri',13),text="year")
labelanneparution.place(x=880,y=10);
#getvalue()  
def GetValue(event):
    idbookentry.delete(0, END)
    aurorentry.delete(0, END)
    titleentry.delete(0, END)
    dateparutionentry.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    idbookentry.insert(0,select['idbook'])
    aurorentry.insert(0,select['autor'])
    titleentry.insert(0,select['title'])
    dateparutionentry.insert(0,select['anne parution'])


#entry

idbook=StringVar()
autor=StringVar()
title=StringVar()
dateparution=StringVar()

idbookentry=Entry(fg="red",font=(8),textvariable=idbook)
idbookentry.place(x=10,y=60)
aurorentry=Entry(fg="red",font=(8),textvariable=autor)
aurorentry.place(x=280,y=60)
titleentry=Entry(fg="red",font=(8),textvariable=title)
titleentry.place(x=540,y=60)
dateparutionentry=Spinbox(from_=1900,to=2500,textvariable=dateparution);
dateparutionentry.place(x=820,y=60)

#button

#insert datata
def removeall():
      x=listBox.get_children()
      if(x!='()'):
            for child in x:
              listBox.delete(child);

       
  

def exit():
    mywin.quit()
    

#add book
def add():
 
   booktoadd=Book(idbook.get(),autor.get(),title.get(),dateparution.get())
 

 
   try:
               c=filename
               connect=connexion()
               conn = connect.connectionWithmysql()
               cursor = conn.cursor()
               sqlQuery="INSERT INTO book (idbook,autor,title,anneParution,image) VALUES (%s,%s,%s,%s,%s)"
               values=(booktoadd.getidBook(),booktoadd.getauteur(),booktoadd.gettitle(), booktoadd.getdateparu(),c)
               cursor.execute( sqlQuery,values,)
               conn.commit()
               conn.close()
               messagebox.showinfo("book insertcorrectly")
               idbook.set("")
               autor.set("")
               title.set("")
               dateparution.set("1900")
               c=""
        
                
   except:
              messagebox.showerror("book already inserte")

def show():#afficher tout les livre
      removeall()
      try:
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlQuery="SELECT idbook,autor,title,anneParution FROM book"
         cursor.execute(sqlQuery)
         myresulte=cursor.fetchall()
         conn.commit()
         conn.close()
         for book in myresulte:
            listBox.insert("",END,values=book)
      except:
        messagebox.showerror("error")

def updateBook():
     
     booktochange=Book(idbook.get(),autor.get(),title.get(),dateparution.get())
     try:
         c=filename
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="Update book set autor=%s,title=%s,anneParution=%s,image=%s where idbook=%s"
         values=(booktochange.getauteur(),booktochange.gettitle(), booktochange.getdateparu(),c,booktochange.getidBook())
         cursor.execute(sqlquery,values,)
         conn.commit()
         conn.close()
         idbook.set("")
         autor.set("")
         title.set("")
         dateparution.set("1900")
         messagebox.showinfo("update is correctly done")
     except:
          messagebox.showerror("error to change something")

#searchbyname:
def shearch():
   removeall()
   booktofind=Book(idbook.get(),autor.get(),title.get(),dateparution.get())
   try:
        
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlQuery="SELECT idbook,autor,title,anneParution FROM book where title=%s"
         values=(booktofind.gettitle(),)
         cursor.execute(sqlQuery,values);
         myresulte=cursor.fetchall()
         conn.commit()
         conn.close()
         for book in myresulte:
            listBox.insert("",END,values=book)
         idbook.set("")
         autor.set("")
         title.set("")
         dateparution.set("1900")
   except:
        messagebox.showerror("error")  

def delete():
     booktodelete=Book(idbook.get(),autor.get(),title.get(),dateparution.get())
     try:
       
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="DELETE FROM book WHERE idbook = %s"
         val=(booktodelete.getidBook(),)
         cursor.execute(sqlquery,val)
         conn.commit()
         conn.close
         messagebox.showinfo("user deleted succesfully")
         idbook.set("")
         autor.set("")
         title.set("")
         dateparution.set("1900")
     except:
          messagebox.showerror("user is not in database")

updatebutoon= Button(mywin,bg="aqua",text="update",width=20,height=3,command=updateBook)
updatebutoon.place(x=100,y=200)
addbutton=Button(mywin,bg="aqua",text="add",width=20,height=3,command=add)
addbutton.place(x=330,y=200)
deletebutton=Button(mywin,bg="aqua",text="delete",width=20,height=3,command=delete)
deletebutton.place(x=530,y=200)
searchbtn=Button(mywin,bg="aqua",text="show all book",width=20,height=10,command=show)
searchbtn.place(x=730,y=200)





    


# Image upload and display
def upload_file(): 
    global filename,img1
    filename=filedialog.askopenfilename( filetypes=[("jpg files", "*.jpg"),("png files", "*.png")])
    
    
#getimage
def getImage():
      booktodeshowImages=Book(idbook.get(),autor.get(),title.get(),dateparution.get())
      global img;
      try:
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="select image from book where idbook=%s"
         val=(booktodeshowImages.getidBook(),);
         cursor.execute(sqlquery,val)
         myresult=cursor.fetchone()
        
         img=Image.open(myresult[0]);
           
         img=img.resize((140,140))
         img=ImageTk.PhotoImage(img);
         Lebel=tk.Label(mywin,image=img,width=140,height=140)
         Lebel.place(x=830,y=400)
         
         print(myresult[0])

         conn.commit();
         conn.close()
        
           
      except:
           messagebox.showerror("error images")
      
   
  

    

    
        
    


sharchbynamebtn=Button(mywin,bg="aqua",text="search by title",width=20,height=3,command=shearch);
sharchbynamebtn.place(x=100,y=300)
uploadimg=Button(mywin,bg="aqua",text="upload image",width=20,height=3,command=upload_file)
uploadimg.place(x=530,y=300)
getImagesValue=Button(mywin,bg="aqua",text="get img",width=20,height=3,command=getImage)
getImagesValue.place(x=330,y=300)


#treview

cols = ('idbook', 'autor', 'title','anne parution')
listBox = ttk.Treeview(mywin, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=400)
 


listBox.bind('<Double-Button-1>',GetValue)




mywin.mainloop()