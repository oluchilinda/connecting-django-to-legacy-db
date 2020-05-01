# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    product_cd = models.ForeignKey('Product', models.DO_NOTHING, db_column='product_cd')
    cust = models.ForeignKey('Customer', models.DO_NOTHING)
    open_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    last_activity_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    open_branch = models.ForeignKey('Branch', models.DO_NOTHING, blank=True, null=True)
    open_emp = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    avail_balance = models.FloatField(blank=True, null=True)
    pending_balance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account'


class Branch(models.Model):
    branch_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'branch'


class Business(models.Model):
    cust = models.OneToOneField('Customer', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=40)
    state_id = models.CharField(max_length=10)
    incorp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'business'


class Clv(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    cust_no = models.BigIntegerField(blank=True, null=True)
    clv = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clv'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    fed_id = models.CharField(max_length=12)
    cust_type_cd = models.CharField(max_length=1)
    address = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'


class Department(models.Model):
    dept_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Employee(models.Model):
    emp_id = models.SmallAutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    superior_emp = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    assigned_branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee'


class Individual(models.Model):
    cust = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'individual'


class Officer(models.Model):
    officer_id = models.SmallAutoField(primary_key=True)
    cust = models.ForeignKey(Business, models.DO_NOTHING)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    title = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'officer'


class Product(models.Model):
    product_cd = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    product_type_cd = models.ForeignKey('ProductType', models.DO_NOTHING, db_column='product_type_cd')
    date_offered = models.DateField(blank=True, null=True)
    date_retired = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductType(models.Model):
    product_type_cd = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_type'


class Transaction(models.Model):
    txn_id = models.AutoField(primary_key=True)
    txn_date = models.DateTimeField()
    account = models.ForeignKey(Account, models.DO_NOTHING)
    txn_type_cd = models.CharField(max_length=3, blank=True, null=True)
    amount = models.FloatField()
    teller_emp = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    execution_branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    funds_avail_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'
