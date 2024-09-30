from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=150)
    page = models.IntegerField(default=15)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def _str_(self):
        return self.title

class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review')
    review=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'Review for {self.book.title}'