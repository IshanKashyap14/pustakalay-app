from django.db import models
from datetime import datetime
# x = datetime.now()
# y =datetime(1981,9,15)
# z = x-y
# print(z)

# Create your models here.
class Dukandar(models.Model):
    DukanID = models.AutoField
    Fullname = models.CharField(max_length=50)
    ShopID = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Dukan_Image = models.ImageField(upload_to='dukanimages/', height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.Fullname
    

class Borrower(models.Model):
    # DukanID = models.AutoField
    Fullname = models.CharField(max_length=50)
    StudentID = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    User_Image = models.ImageField(upload_to='userimages/', height_field=None, width_field=None, max_length=None)
    Points = models.IntegerField(default=10)
    RegDate = models.DateField(default = datetime.now(),auto_now=False, auto_now_add=False)
    BorrowDate = models.DateField(default = datetime(1981,9,15) ,auto_now=False, auto_now_add=False)
    BorrowedBook = models.CharField(default='Atomic Habits',max_length=50)
    def __str__(self):
        return self.Fullname


class Book(models.Model):
    BookID = models.AutoField
    Uploader = models.CharField(default='Ramesh Dukanwala',max_length=50)
    Title = models.CharField(max_length=150)
    Category = models.CharField(max_length=50)
    BookPrice = models.IntegerField()
    Image = models.ImageField(upload_to='bookimages/', height_field=None, width_field=None, max_length=None)
    PDF = models.FileField(upload_to='bookpdfs/',default='mypdf.pdf')

    def __str__(self):
        return self.Title


class Question(models.Model):
    Bookname = models.CharField(max_length=50)
    question1 = models.CharField(max_length=250)
    answer1 = models.CharField(max_length=500)
    question2 = models.CharField(max_length=250)
    answer2 = models.CharField(max_length=500)
    question3 = models.CharField(max_length=250)
    answer3 = models.CharField(max_length=500)
    question4 = models.CharField(max_length=250)
    answer4 = models.CharField(max_length=500)
    question5 = models.CharField(max_length=250)
    answer5 = models.CharField(max_length=500)
    question6 = models.CharField(max_length=250)
    answer6 = models.CharField(max_length=500)
    question7 = models.CharField(max_length=250)
    answer7 = models.CharField(max_length=500)
    question8 = models.CharField(max_length=250)
    answer8 = models.CharField(max_length=500)
    question9 = models.CharField(max_length=250)
    answer9 = models.CharField(max_length=500,default='yes')
    question10 = models.CharField(max_length=250)
    answer10 = models.CharField(max_length=500)

    def __str__(self):
        return self.Bookname
    