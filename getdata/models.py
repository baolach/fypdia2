from django.db import models

# Create your models here.
class GetClient(models.Model):
    client_name = models.TextField(default=None)
    client_phone = models.CharField(default=None,max_length=10)
    client_address = models.TextField(default=None)
    log_no = models.TextField(default=None, max_length = 9)
    driver_no = models.TextField(default=None, max_length = 5)
    dob = models.TextField(default=None)
    no_of_lessons = models.CharField(default=None, max_length = 3)
    balance_due = models.CharField(default=None, max_length = 3)
    comments = models.TextField(default=None)

    def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
        return self.client_name

class GetLesson(models.Model):
    lesson_name = models.TextField(default=None,)
    lesson_date = models.DateField(default=None)
    lesson_time = models.TimeField(default=None)
    lesson_location = models.TextField(default=None)
    lesson_comments = models.TextField(default=None)




class GetLocation(models.Model):
    location_type = models.TextField(default=None)
    location_x = models.CharField(default=None, max_length=30)
    location_y = models.CharField(default=None, max_length=30)
    location_detail = models.TextField(default=None)


    def __str__(self):  # rather than just saying post object, we can name the posts
        return self.type


class GetExpense(models.Model):
    expense_name = models.TextField(default=None,)
    expense_amount = models.CharField(default=None, max_length=6)
    expense_date = models.DateField(default=None)

    def __str__(self):
        return self.expense_name


class GetUser(models.Model):
    username = models.TextField(default=None,)
    password= models.TextField(default=None)

    def __str__(self):
        return self.username