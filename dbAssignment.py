import sqlite3 #necessary import to be able to manipulate the DB




def createDB(): #function to create the DB (if it doesn't already exist)
    conn = sqlite3.connect('files.db') #connect or creates DB file
    with conn: #loop while DB is open
        cur = conn.cursor() #used to manipulate DB
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT \
            )")
        conn.commit() #saves the DB

    #tuple of file names provided
    fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    
    for x in fileList:
        if x.endswith('.txt'): #checks for ends in .txt
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_txtFiles (col_fname) VALUES (?)", (x,))
                print (x) #print command in console

    conn.commit() #saves the DB  
    conn.close #close DB



if __name__ == "__main__": #this is used to run the set of function we want.   
    createDB()
