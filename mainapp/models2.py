from django.db import models


class Animal(models.Model):
    record_card = models.CharField(max_length=20)
    kind = models.CharField(max_length=7)
    year_of_birth = models.DateField
    weight = models.IntegerField
    nickname = models.CharField(max_length=20)
    sex = models.BinaryField
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    wool = models.CharField(max_length=10)
    ears = models.CharField(max_length=20)
    tail = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    signs = models.BinaryField
    area = models.IntegerField


class Additional_dates(models.Model):
    id_label = models.CharField(max_length=20)
    sterilization_date = models.CharField(max_length=40)
    doctor = models.CharField(max_length=50)
    socialized = models.BinaryField


class Catch_info(models.Model):
    act_of_adm = models.CharField(max_length=20)
    act_of_adm_data = models.DateField
    district = models.CharField(max_length=10)
    catch_act = models.CharField(max_length=20)
    catch_address = models.CharField(max_length=100)


class New_owner(models.Model):
    entity = models.CharField(max_length=50)
    trustee = models.CharField(max_length=50)
    individual = models.CharField(max_length=50)


class Animal_move(models.Model):
    shelter_add_date = models.DateField
    shelter_add_act = models.CharField(max_length=20)
    shelter_leave_date = models.DateField
    reason = models.CharField
    shelter_leave_act = models.CharField(max_length=20)


class Response(models.Model):
    shelter_address = models.CharField
    organization_name = models.CharField(max_length=20)
    org_lead_name = models.CharField(max_length=50)
    worker_name = models.CharField(max_length=50)


class Ecto_endo_info(models.Model):
    ecto_no_p_p = models.IntegerField
    ecto_endo_data = models.DateField
    drugs_name = models.CharField(max_length=50)
    drugs_dose = models.IntegerField


class Vaccination(models.Model):
    vac_no_p_p = models.IntegerField
    vac_date = models.CharField
    vac_type = models.CharField
    vac_no = models.CharField


class Health(models.Model):
    view_date = models.DateField
    anamnez = models.CharField[50]
# Create your models here.
