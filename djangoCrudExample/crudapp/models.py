# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Termscodes(models.Model):
    termsid = models.CharField(db_column='termsID', primary_key=True, max_length=12)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    allowance = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    daystoearndiscount = models.IntegerField(db_column='daysToEarnDiscount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'termscodes'

class Mastervendor(models.Model):
    vendorid = models.CharField(db_column='vendorId', primary_key=True, max_length=48)  # Field name made lowercase.
    contactname = models.CharField(db_column='contactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorname = models.CharField(db_column='vendorName', max_length=48)  # Field name made lowercase.
    country = models.CharField(max_length=48, blank=True, null=True)
    state = models.CharField(max_length=48, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    termsid = models.ForeignKey('Termscodes', models.DO_NOTHING, db_column='termsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mastervendor'


class Orderheader(models.Model):
    orderreceived = models.DateField(blank=True, null=True)
    vendorid = models.ForeignKey(Mastervendor, models.DO_NOTHING, db_column='vendorId', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField()
    orderid = models.AutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    shipdate = models.DateField(blank=True, null=True)
    cost = models.FloatField()
    termsid = models.ForeignKey('Termscodes', models.DO_NOTHING, db_column='termsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderheader'

class Masteritem(models.Model):
    itemid = models.CharField(db_column='itemID', primary_key=True, max_length=48)  # Field name made lowercase.
    lastpricechange = models.DateField(db_column='lastPriceChange', blank=True, null=True)  # Field name made lowercase.
    previouscost = models.FloatField(db_column='previousCost', blank=True, null=True)  # Field name made lowercase.
    vendorid = models.ForeignKey('Mastervendor', models.DO_NOTHING, db_column='vendorId')  # Field name made lowercase.
    cost = models.FloatField()
    intialpurchasedate = models.DateField(db_column='intialPurchaseDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masteritem'



class Inventory(models.Model):
    recordnum = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Masteritem', models.DO_NOTHING, db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    onhand = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'

    def __str__(self):
        return self.itemid


class Lineitem(models.Model):
    linekey = models.AutoField(primary_key=True)
    itemid = models.ForeignKey('Masteritem', models.DO_NOTHING, db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    lineid = models.IntegerField(db_column='lineID')  # Field name made lowercase.
    orderid = models.ForeignKey('Orderheader', models.DO_NOTHING, db_column='orderID', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lineitem'


class Masterinvoice(models.Model):
    invoiceid = models.CharField(db_column='invoiceID', primary_key=True, max_length=48)  # Field name made lowercase.
    datesent = models.DateField()
    paymentduedate = models.DateField()
    grossamount = models.FloatField()
    vendorid = models.ForeignKey('Mastervendor', models.DO_NOTHING, db_column='vendorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterinvoice'






