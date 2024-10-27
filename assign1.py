Book  = open("books.txt", "r")
# books.txt contains book id , name of the book , author of the book,  price of the book
# reading content from file
Content1 = Book.readlines()
Book_Data = []
"""
Storing the input of files in  dictionaries  so that we can commpare the values by using the keys of different file data
"""
"""

getting input from the books.txt file and rounding up the price to two decimal places

"""

for i in range(len(Content1)):
    Book_Id,Book_Name,Book_Author,Book_Price = (Content1[i].split('#'))
    round(float(Book_Price.strip("\n")),2)
    Book_Data.append({"Book_Id": Book_Id, "Book_Name": Book_Name,"Book_Author":Book_Author,"Book_Price": Book_Price})

Students = open("students.txt", "r")
Content2 = Students.readlines()
Student_Data = []

"""
getting input from the students.txt file and storing some relevant information for the comparison between two files input
stripping of the \n from the end of one line
"""
for i in range(len(Content2)):
    Student_Id,Student_Name,Student_Class = (Content2[i].split(','))
    Student_Class.strip("\n")
    Student_Data.append({"Student_Id":Student_Id,"Student_Name": Student_Name,"Student_Class":Student_Class})

# Content3 contains the data of  borrowers.txt that is id, name, Class of a student
"""
contains borrowers details book id , student id,, borrowed date and return date

"""
Borrowers = open("borrowers.txt", "r")
Content3 = Borrowers.readlines()
Borrower_Details = []

"""
"""

for i in range(len(Content3)):
    Borrowed_Book_Id,Student_Id,Borrowed_Date,Expected_Return_Date = (Content3[i].split(';'))
    Expected_Return_Date.strip("\n")
    Borrower_Details.append({"Book_Id":Borrowed_Book_Id,"Student_Id":Student_Id,"Borrowed_Date":Borrowed_Date,"Expected_Return_Date":Expected_Return_Date})
print(Borrower_Details)
"""
storing data of returns.txt data and storing certain data like Return_Book_Id which we will use to compare  the data between borrowers and returns
"""
Returns = open("returns.txt", "r")
Content4 = Returns.readlines()
Return_Data = []
Return_Book_Id = []
Condition = []
for i in range(len(Content4)):
    Book_Id_Return,Student_Id_Return,Return_Date,Book_Condition = (Content4[i].split(';'))
    Book_Condition.strip("\n")
    Condition.append(Book_Condition)
    Return_Book_Id.append(Book_Id_Return)
    Return_Data.append({"Book_Id":Book_Id,"Student_Id": Student_Id,"Return_Date":Return_Date,"Book_Condition":Book_Condition})
# month table ---- to convert number into string
Expected_Return_Month = ["jan","feb","Mar","Apr","jun","jul","Aug","Sep","Oct","Nov","Dec"]

# file inn which we will write our output

Output_File = open('standing.txt', 'w')
Borrowed_Name = []
Borrowed_Class = []
Borrowed_Book_Id = []
"""
getting the name of the students and the class whooo borrowed the books by comparing the  2 files data which is borrowers and Student respectively
"""
for key1 in Borrower_Details:
    for key2 in Student_Data:
        if key1["Student_Id"] == key2["Student_Id"] :
            Borrowed_Name.append(key2["Student_Name"])
            Borrowed_Class.append(key2["Student_Class"].strip("\n"))

Borrowed_Book_Price = []
Borrowed_Book_Name  = []
Borrowed_Book_Return_Date = []
"""
getting the Book and its relevant details from Books file and borrowers file by comparing their data
"""
for key3 in Borrower_Details:
    for key4 in Book_Data:
        if key3["Book_Id"] == key4["Book_Id"]:
            Borrowed_Book_Name.append(key4["Book_Name"])
            Borrowed_Book_Return_Date.append(key3["Expected_Return_Date"].strip("\n"))
            Borrowed_Book_Price.append(key4["Book_Price"].strip("\n"))
            Borrowed_Book_Id.append(key4["Book_Id"])
"""
drawing the table format
"""
Output_File.write("+------------------+-------------------------------------+--------------+\n")
Student = "Student"
DueDate = "DueDate"
book = "Book"
Output_File.write("| %-16s | %-35s |%-13s |\n" % (Student,book,DueDate))
Output_File.write("+------------------+-------------------------------------+--------------+\n")
Total = 0    # counting the number of books

"""
 checking whether the borrowed books have been returned by the students or not and if not printing them in the output file
"""
for i in range(len(Borrowed_Name)):
    if Borrowed_Book_Id[i] not in Return_Book_Id:
        Total+=1
        Year = int(Borrowed_Book_Return_Date[i][0:2])

        Month_Number = int(Borrowed_Book_Return_Date[i][2:4])

        Date = int(Borrowed_Book_Return_Date[i][4:6])
        write = ("| %-16s | %-35s | %s %i, 20%i |\n" % (Borrowed_Name[i],Borrowed_Book_Name[i],Expected_Return_Month[Month_Number - 1],Date,Year))
        Output_File.write(write)
Output_File.write("+------------------+-------------------------------------+--------------+\n")
Print_Output = "Total Books"
total_output = ("|%-52s    | %-12i |\n" % (Print_Output,Total))
Output_File.write(total_output)
Output_File.write("+------------------+-------------------------------------+--------------+\n")
#print(Borrowed_Book_Name,Borrowed_Book_Return_Date,Borrower_Name,Borrowed_Book_Price)








    #print(Data[i]["Book_Id"]   for Data in  Return_Data if Borrower_Details[i]["Book_Id"] == Data[i]["Book_Id"])









