from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Uploader', 'Title', 'Category', 'BookPrice', 'Image']

    def clean_Uploader(self):
        uploader = self.cleaned_data.get('Uploader')
        # Add custom validation for the Uploader field if needed
        return uploader

    def clean_Title(self):
        title = self.cleaned_data.get('Title')
        # Add custom validation for the Title field if needed
        return title

    def clean_Category(self):
        category = self.cleaned_data.get('Category')
        # Add custom validation for the Category field if needed
        return category

    def clean_BookPrice(self):
        book_price = self.cleaned_data.get('BookPrice')
        if book_price <= 0:
            raise forms.ValidationError("Book price must be a positive integer.")
        # Add any other custom validation for the BookPrice field if needed
        return book_price

    def clean_Image(self):
        image = self.cleaned_data.get('Image')
        # Add custom validation for the Image field if needed
        return image

    # You can also override the clean() method for general form-level validation
    def clean(self):
        cleaned_data = super().clean()
        # Your custom validation logic here
        return cleaned_data
