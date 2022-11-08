#imports
import tkinter as tk
from tkinter import *
import webbrowser

#Frame class creation
class ParentWindow(Frame):
    def __init__(self,master): #basic __init__ function

        #variable creation
        self.varCustTxt = StringVar()

        #Frame Creation with title
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        #label for input
        self.lblCustom = Label(self.master,text="Enter custom text or click the Default HTML page button", font =("Helvetica", 12), fg="black")
        self.lblCustom.grid(row=0,column=0, columnspan=2,padx=(30,0),pady=(30,0), sticky=N+W)

        #input for text
        self.txtCustom = Entry(self.master, text=self.varCustTxt, font=("Helvetica", 12), width = 70, fg="black", bg="white")
        self.txtCustom.grid(row=1,column=0, columnspan=3, padx=(30,10),pady=(0,0), sticky=N+W)
        
        #default website button creation
        self.btn = Button(self.master, text="Custom HTML Page", width = 30, height = 2, command=self.customHTML)
        self.btn.grid(row=2, column = 1, padx=(10,10) , pady=(10,10), sticky = N+E)

        #custom website button creation
        self.btn = Button(self.master, text="Default HTML Page", width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(row = 2, column = 2, padx=(10,10) , pady=(10,10), sticky = N+E)


    #function to create default website
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #function to creat custom website
    def customHTML(self):
        htmlText = self.varCustTxt.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



#program control statement
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
