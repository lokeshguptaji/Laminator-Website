from django.db import models

# Create your models here.

class Items(models.Model):
    item_name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField(upload_to="manufacture/images")


    def __str__(self):
        return self.item_name

class Contact(models.Model):
    

    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    website=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    your_enquiry=models.TextField()
    industry=models.CharField(max_length=30)
    product_type=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
    
    