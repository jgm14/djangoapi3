# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

""" class Customer(models.Model):
    first_name = models.CharField(db_column='FIRST_NAME', max_length=40)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=40)  # Field name made lowercase.
    customer_id = models.AutoField(db_column='CUSTOMER_ID', primary_key=True)  # Field name made lowercase.
    phone_num = models.CharField(db_column='PHONE_NUM', max_length=11)  # Field name made lowercase.
    email_add = models.CharField(db_column='EMAIL_ADD', max_length=40)  # Field name made lowercase.

    class Meta:
        db_table = 'customer' """

class Users(models.Model):
    email = models.CharField(db_column='email', max_length=500, default=None)  # Field name made lowercase.
    userID = models.AutoField(db_column='user_id', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='passwd', max_length=1000, null=True)  # Field name made lowercase.
    firstName = models.CharField(db_column='fname', max_length=1000, null=True)  # 
    lastName = models.CharField(db_column='lname', max_length=1000, null=True)  # 

    class Meta:
        db_table = 'users'
        unique_together = (('email', 'userID'),)


class AllQueues(models.Model):
    queue_id = models.AutoField(db_column='QUEUE_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey(Users, default=None, on_delete=models.CASCADE, db_column='USER_ID')  # Field name made lowercase.
    queue_name = models.CharField(db_column='QUEUE_NAME', max_length=100, default="Your Queue")  # Field name made lowercase.
    queue_desc = models.CharField(db_column='QUEUE_DESC', max_length=100, default="Add a Description")  # Field name made lowercase.
    estimated_wait = models.IntegerField(db_column='ESTIMATED_WAIT', default=5)  # Field name made lowercase.

    class Meta:
        db_table = 'all_queues'


class Guest(models.Model):
    guest_id = models.AutoField(db_column='GUEST_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'guest'


class InQueue(models.Model):
    queue_id = models.ForeignKey(AllQueues, default=None, on_delete=models.CASCADE, db_column='QUEUE_ID')  # Field name made lowercase.
    guest_id = models.OneToOneField(Guest, default=None, on_delete=models.CASCADE, primary_key=True, db_column='GUEST_ID')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP', auto_now_add=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'in_queue'
