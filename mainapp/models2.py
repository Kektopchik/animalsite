from django.db import models


class Animal(models.Model):
    SEX_ANIMAL = (
        ('M', 'Кабель'),
        ('Ж', 'Сучка'),
    )
    record_card = models.CharField(null=True, max_length=20, verbose_name="Карточка учета", default="")
    kind = models.CharField(null=True,max_length=7, verbose_name="Вид", default="")
    year_of_birth = models.DateField(null=True, verbose_name="Дата рождения", default="")
    weight = models.IntegerField(null=True, verbose_name="Вес", default="")
    nickname = models.CharField(null=True,max_length=20, verbose_name="Кличка", default="")
    sex = models.BinaryField(choices=SEX_ANIMAL, verbose_name="Пол", default="")
    breed = models.CharField(null=True,max_length=50, verbose_name="Порода", default="")
    color = models.CharField(null=True,max_length=20, verbose_name="Цвет", default="")
    wool = models.CharField(null=True,max_length=10, verbose_name="Шерсть", default="")
    ears = models.CharField(null=True,max_length=20, verbose_name="Уши", default="")
    tail = models.CharField(null=True,max_length=20, verbose_name="Хвост", default="")
    size = models.CharField(null=True,max_length=10, verbose_name="Размер", default="")
    signs = models.BinaryField(null=True, verbose_name="Особые приметы", default="")
    area = models.IntegerField(null=True, verbose_name="Вольер №", default="")


class Additional_dates(models.Model):
    id_label = models.CharField(null=True,max_length=20, verbose_name="Идентификационная метка", default="")
    sterilization_date = models.CharField(null=True,max_length=40, verbose_name="Дата стерилизации", default="")
    doctor = models.CharField(null=True,max_length=50, verbose_name="ФИО вет врача", default="")
    socialized = models.BinaryField(null=True, verbose_name="Социализировано (да/нет)", default="")


class Catch_info(models.Model):
    act_of_adm = models.CharField(null=True,max_length=20, verbose_name="Акт о поступлении животного №", default="")
    act_of_adm_data = models.DateField(null=True, verbose_name="Акт о поступлении животного, дата", default="")
    district = models.CharField(null=True,max_length=10, verbose_name="Административный округ", default="")
    catch_act = models.CharField(null=True,max_length=20, verbose_name="Акт отлова №", default="")
    catch_address = models.CharField(null=True,max_length=100, verbose_name="Адоес места отлова", default="")


class New_owner(models.Model):
    entity = models.CharField(null=True,max_length=50, verbose_name="Юридическое лицо", default="")
    trustee = models.CharField(null=True,max_length=50, verbose_name="ФИО опекунов", default="")
    individual = models.CharField(null=True,max_length=50, verbose_name="Физическое лицо", default="")


class Animal_move(models.Model):
    shelter_add_date = models.DateField(null=True, verbose_name="Дата поступления в приют", default="")
    shelter_add_act = models.CharField(max_length=100, null=True, verbose_name="Акт №", default="")
    shelter_leave_date = models.DateField(null=True, verbose_name="Дата выбития из приюта", default="")
    reason = models.CharField(max_length=100,null=True, verbose_name="Причина выбытия", default="")
    shelter_leave_act = models.CharField(null=True,max_length=20, verbose_name="Акт/договор №", default="")


class Response(models.Model):
    shelter_address = models.CharField(max_length=100,null=True, verbose_name="Адрес приюта", default="")
    organization_name = models.CharField(null=True,max_length=20, verbose_name="Эксплотирующая организация", default="")
    org_lead_name = models.CharField(null=True,max_length=50, verbose_name="ФИО руководителя приюта", default="")
    worker_name = models.CharField(null=True,max_length=50, verbose_name="ФИО сотрудника по уходу за животным", default="")


class Ecto_endo_info(models.Model):
    ecto_no_p_p = models.IntegerField(null=True, verbose_name="№ п/п", default="")
    ecto_endo_data = models.DateField(null=True, verbose_name="Дата", default="")
    drugs_name = models.CharField(null=True,max_length=50, verbose_name="Название препарата", default="")
    drugs_dose = models.IntegerField(null=True, verbose_name="Доза", default="")


class Vaccination(models.Model):
    vac_no_p_p = models.IntegerField(null=True, verbose_name="№ п/п", default="")
    vac_date = models.CharField(null=True, verbose_name="Дата", default="")
    vac_type = models.CharField(null=True, verbose_name="Вид вакцины", default="")
    vac_no = models.CharField(null=True, verbose_name="№ серии", default="")


class Health(models.Model):
    view_date = models.DateField(null=True, verbose_name="Дата осмотра", default="")
    anamnez = models.CharField(max_length=50 ,null=True, verbose_name="Анамнез", default="")
# Create your models here.
