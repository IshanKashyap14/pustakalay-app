from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Dukandar,Book,Question,Borrower
from .form import BookForm
from django.core.files import File 
from django.core.files.storage import FileSystemStorage
from datetime import datetime,date
# Create your views here.
class AllFuncs():
    SHOPID = None
    STUDENTID = None
    BOOKNAME = None
    USERTYPE = None
    StudName = None
    IsBorrowed = None
    POINTS = None
    PAYED = None
    BorrowedBook = None
    def home_page(self,request):
        return render(request,'home_page.html')


    def main_page(self,request):
        #who logins checker
        self.USERTYPE = ''
        #Seller Details
        Seller_Fullname = request.POST.get('FullName')
        self.SHOPID = request.POST.get('ShopID')
        print(self.SHOPID)
        Seller_Password = request.POST.get('Password')
        #Student Details
        Student_Fullname = request.POST.get('FullNameS')
        self.StudName = Student_Fullname
        # print(Student_Fullname)
        self.STUDENTID = request.POST.get('StudentID')
        Student_Password = request.POST.get('PasswordS')
        #check if blank
        if Seller_Fullname == '' and Student_Fullname == '':
            pass
        elif self.SHOPID == '' and self.STUDENTID == '':
            pass
        elif Seller_Password == '' and Student_Password == '':
            pass
        else:
            if Student_Fullname == None : 
                self.USERTYPE = 'Seller'
            else:
                self.USERTYPE = 'Borrower'
            # print(UserType)
        #Accessing Data
        if self.USERTYPE == 'Seller':
            dukandar = Dukandar.objects.all()           
            try:
                if dukandar.get(Fullname=Seller_Fullname).ShopID == self.SHOPID and dukandar.get(Fullname=Seller_Fullname).Password == Seller_Password:
                    books = Book.objects.all()
                    SellerKiBooks = books.filter(Uploader=Seller_Fullname)
    
                    # print(SellerKiBooks.get(Category='Self-Help').Title)
                    data = {"Dukandar":dukandar,'img_url':dukandar.get(Fullname=Seller_Fullname).Dukan_Image,'username':Seller_Fullname,'books':SellerKiBooks,'shopid':self.SHOPID}
                    return render(request,'main_page.html',data)
                else:
                    return HttpResponse('Wrong Credentials')
            except:
                return HttpResponse('Wrong Credentials')
        else:
            borrower = Borrower.objects.all()
            self.POINTS = borrower.get(StudentID=self.STUDENTID).Points  
            self.BorrowedBook = borrower.get(StudentID=self.STUDENTID).BorrowedBook
            print('Points : ',self.POINTS)         
            borrowdate =  borrower.get(StudentID=self.STUDENTID).BorrowDate
            # print('Borrowing Date',borrowdate)
            print('Current Date',datetime.now().date())
            datebetween= datetime.now().date()-borrowdate
            daysbetween = datebetween.days
            # print(daysbetween)
            if daysbetween < 15524:
                print('Days Passed after Borrow',daysbetween)
                self.IsBorrowed = True
                if daysbetween > 6:
                    self.PAYED = False
                    print('paisa kab doge!!!')
            else:
                # print('Days Passed after Borrow',daysbetween)
                self.IsBorrowed = False
                print('no book borrowed')
            if borrower.get(Fullname=Student_Fullname).StudentID == self.STUDENTID and borrower.get(Fullname=Student_Fullname).Password == Student_Password:

                books = Book.objects.all()
                BookwithQ = []
                question = Question.objects.all()
                for item in books:
                    if question.filter(Bookname=item).exists():
                        BookwithQ.append(item)
                
                # print(BookwithQ)
                # StudKiBooks = books.filter(Uploader=Seller_Fullname)
                # print(SellerKiBooks.get(Category='Self-Help').Title)

                data = {"User":borrower,'img_url':borrower.get(Fullname=Student_Fullname).User_Image,'username':Student_Fullname,'books':BookwithQ,'studentid':self.STUDENTID}
                return render(request,'user_page.html',data)
            else:
                return HttpResponse('Wrong Credents')
          
            


    def newbook(self,request):
        # print(self.SHOPID)
        return render(request,'newbook.html')


    def bookscreated(self,request):


        self.BOOKNAME = request.POST.get('Bookname')
        bookCategory = request.POST.get('Cat')
        bookPrice = request.POST.get('Bookprice')
        

        
        print(self.SHOPID)
        dukandar = Dukandar.objects.all()
        user = dukandar.get(ShopID=self.SHOPID).Fullname
        # print(user)
        # print(image)
        CreateBook = Book(Uploader = user,Title=self.BOOKNAME,Category=bookCategory,BookPrice=bookPrice,Image=request.FILES.get('Bookimage'),PDF=request.FILES.get('Bookpdf'))
        CreateBook.save()
        # book = Book(Uploader=user,Title=bookName,Category=bookCategory,BookPrice=bookPrice,Image=image)
        return render(request,"bookcreated.html",{"Book":Book})
        # return render(request, 'hotel_image_form.html', {'form': form})

        

        # return render(request,'bookcreated.html',data)
        
    def questions(self,request):
        dukandar = Dukandar.objects.all()
        book = Book.objects.all()
        question = Question.objects.all()
        existingObject = []
        printObjlist = []
        imgurls = []
        # self.SHOPID = request.POST.get('self.SHOPID')
        # print(self.SHOPID)
        user = dukandar.get(ShopID=self.SHOPID).Fullname
        print(user)   
        # Titles = []
        for item in book.filter(Uploader=user):
            # print(item)
            try:
                existingObject.append(question.get(Bookname=item))
            except:
                printObjlist.append(book.get(Title=item.Title))
                #do this to trigger printObjlist as a non-string so that you can extract things from it.
                imgurls.append(book.get(Title=item.Title).Image) 
                # print(printObjlist)
        
            

        data = {"printObjlist":printObjlist,'imgurls':imgurls}
        # print(printObjlist)
        return render(request,'questions.html',data)


    def qcreate(self,request):
        self.BOOKNAME = request.POST.get('bookname')
        Q1 = request.POST.get('q1')
        A1 = request.POST.get('a1')
        Q2 = request.POST.get('q2')
        A2 = request.POST.get('a2')
        Q3 = request.POST.get('q3')
        A3 = request.POST.get('a3')
        Q4 = request.POST.get('q4')
        A4 = request.POST.get('a4')
        Q5 = request.POST.get('q5')
        A5 = request.POST.get('a5')
        Q6 = request.POST.get('q6')
        A6 = request.POST.get('a6')
        Q7 = request.POST.get('q7')
        A7 = request.POST.get('a7')
        Q8 = request.POST.get('q8')
        A8 = request.POST.get('a8')
        Q9 = request.POST.get('q9')
        A9 = request.POST.get('a9')
        Q10 = request.POST.get('q10')
        A10 = request.POST.get('a10')
            # print(bookName,Q1,A1,Q2,A2,Q3,A3,Q4,A4,Q5,A5,Q6,A6,Q7,A7,Q8,A8,Q9,A9,Q10,A10)
        
        new_question = Question(Bookname=self.BOOKNAME,question1=Q1,question2=Q2,question3=Q3,question4=Q4,question5=Q5,question6=Q6,question7=Q7,question8=Q8,question9=Q9,question10=Q10,answer1=A1,answer2=A2,answer3=A3,answer4=A4,answer5=A5,answer6=A6,answer7=A7,answer8=A8,answer9=A9,answer10=A10)

        new_question.save()




        return render(request,'bookcreated.html')


    def bookpage(self,request):
        book = Book.objects.all()
        question = Question.objects.all()
        existingObject = []
        printObjlist = []
        imgurls = []
        # Titles = []
        for item in book:
        # print(item)
           
            try:
                bookname=request.POST.get('hidden_bookname')
                print(bookname)
                print(question.filter(Bookname=bookname).exists())
                if question.filter(Bookname=bookname).exists():
                    existingObject.append(question.get(Bookname=item))
                    imgurls.append(book.get(Title=item.Title).Image) 
                # printObjlist.append(book.get(Title=item.Title))
                    books = book.filter(Title=bookname)
                    questions = question.get(Bookname=bookname)
                    print(books)
                    data = {"printObjlist":existingObject,'imgurls':imgurls,'books':books,'q':questions}
                    bookname=request.POST.get('hidden_bookname')
                    print(bookname) 

                    return render(request,'bookpage.html',data)
                else:
                    bookname=request.POST.get('hidden_bookname')
                    data = {"printObjlist":printObjlist,'imgurls':imgurls,'bookname':bookname}
                    return render(request,'bookerror.html',data)
            except:
                return render(request,'bookerror.html')
        # print(bookname) 
                #do this to trigger printObjlist as a non-string so that you can extract things from it.
                # print(printObjlist)


    def bookerror(self,request):
        return render(request,'bookerror.html')
    
    def borrowpage(self,request):
        borrower = Borrower.objects.all()
        book = Book.objects.all()
        question = Question.objects.all()
        print(self.IsBorrowed)


      
        # Titles = []
      
        # print(item)
            # try:
        bookname=request.POST.get('hidden_bookname')
        self.BOOKNAME = bookname
        # print(self.BOOKNAME)
            # print(bookname)
            # print(question.filter(Bookname=bookname).exists())
        item = book.get(Title=self.BOOKNAME)
        data = {'item':item,'IsBorrowed':self.IsBorrowed,'POINTS':self.POINTS, 'BorrowedBook':self.BorrowedBook,'books':book}
        return render(request,'borrowpage.html',data)
            
       

    def readbook(self,request):
        # self.IsBorrowed = True
        if self.PAYED == True:
            book = Book.objects.all()
            borrower = Borrower.objects.all().get(StudentID=self.STUDENTID)
            borrower.BorrowDate = datetime.now().date()
            borrower.save()
            print(borrower.BorrowDate)

            pdfurls = []
            # Titles = []
            currbook= book.get(Title=self.BOOKNAME).PDF
            print(currbook)
            pdfurls.append(currbook)
            print(pdfurls)
            
            return render(request,'readbook.html',{'pdfurls':pdfurls,'book':currbook,})
        else:
            return redirect('/payment')
    def answerit(self,request):
        return render(request,'answerit.html')
 
    def payment_page(self,request):
        return render(request,'payment.html')
    def paydone_page(self,request):
        self.PAYED = True
        self.IsBorrowed = True
        self.BorrowedBook = self.BOOKNAME
        borrower = Borrower.objects.all()
        item = borrower.get(StudentID=self.STUDENTID)
        item.BorrowedBook = self.BOOKNAME
        item.BorrowDate = datetime.now()
        print(item.BorrowDate)
        item.save()
        return render(request,'paydone.html')
    
    def returnbook(self,request):
        self.IsBorrowed = False
        self.PAYED = False
        self.BorrowedBook = None
        borrower = Borrower.objects.all()
        item = borrower.get(StudentID=self.STUDENTID)
        item.BorrowedBook = 'nobook'
        item.BorrowDate = datetime(1981,9,15)
        item.save()
        return HttpResponse("Book Returned...... <a href='/'>return to home</a>")