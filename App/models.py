# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=30, blank=True, null=True)
    user_pwd = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class WorkBook(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    row_record = models.CharField(max_length=255)
    author = models.CharField(max_length=30)
    ymd = models.DateField(db_column='Ymd')  # Field name made lowercase.
    is_use = models.IntegerField()
    add_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_book'
        unique_together = (('row_record', 'author', 'ymd'),)
