from django.db import models


class Animals(models.Model):
    SEX_ANIMAL = (
        ('M', 'Кабель'),
        ('Ж', 'Сучка'),
    )
    record_card = models.CharField(null=True, max_length=20, verbose_name="Карточка учета")
    kind = models.CharField(null=True, max_length=7, verbose_name="Вид")
    year_of_birth = models.DateField(null=True, verbose_name="Дата рождения")
    weight = models.IntegerField(null=True, verbose_name="Вес")
    nickname = models.CharField(null=True, max_length=20, verbose_name="Кличка")
    sex = models.BinaryField(choices=SEX_ANIMAL, verbose_name="Пол")
    breed = models.CharField(null=True, max_length=50, verbose_name="Порода")
    color = models.CharField(null=True, max_length=20, verbose_name="Цвет")
    wool = models.CharField(null=True, max_length=10, verbose_name="Шерсть")
    ears = models.CharField(null=True, max_length=20, verbose_name="Уши")
    tail = models.CharField(null=True, max_length=20, verbose_name="Хвост")
    size = models.CharField(null=True, max_length=10, verbose_name="Размер")
    signs = models.BinaryField(null=True, verbose_name="Особые приметы")
    area = models.IntegerField(null=True, verbose_name="Вольер №")


class Additional_dates(models.Model):
    sterilization_date = models.CharField(null=True, max_length=40, verbose_name="Дата стерилизации")
    doctor = models.CharField(null=True, max_length=50, verbose_name="ФИО вет врача")
    socialized = models.BinaryField(null=True, verbose_name="Социализировано (да/нет)")


class Catch_info(models.Model):
    act_of_adm_data = models.DateField(null=True, verbose_name="Акт о поступлении животного, дата")
    district = models.CharField(null=True, max_length=10, verbose_name="Административный округ")
    catch_act = models.CharField(null=True, max_length=20, verbose_name="Акт отлова №")
    catch_address = models.CharField(null=True, max_length=100, verbose_name="Адоес места отлова")


class New_owner(models.Model):
    entity = models.CharField(null=True, max_length=50, verbose_name="Юридическое лицо")
    trustee = models.CharField(null=True, max_length=50, verbose_name="ФИО опекунов")
    individual = models.CharField(null=True, max_length=50, verbose_name="Физическое лицо")


class Animal_move(models.Model):
    shelter_add_date = models.DateField(null=True, verbose_name="Дата поступления в приют")
    shelter_add_act = models.CharField(max_length=100, null=True, verbose_name="Акт №")
    shelter_leave_date = models.DateField(null=True, verbose_name="Дата выбития из приюта")
    reason = models.CharField(max_length=100, null=True, verbose_name="Причина выбытия")
    shelter_leave_act = models.CharField(null=True, max_length=20, verbose_name="Акт/договор №")


class Response(models.Model):
    shelter_address = models.CharField(max_length=100, null=True, verbose_name="Адрес приюта")
    organization_name = models.CharField(null=True, max_length=20, verbose_name="Эксплотирующая организация")
    org_lead_name = models.CharField(null=True, max_length=50, verbose_name="ФИО руководителя приюта")
    worker_name = models.CharField(null=True, max_length=50, verbose_name="ФИО сотрудника по уходу за животным")


class Ecto_endo_info(models.Model):
    ecto_endo_data = models.DateField(null=True, verbose_name="Дата")
    drugs_name = models.CharField(null=True, max_length=50, verbose_name="Название препарата")
    drugs_dose = models.IntegerField(null=True, verbose_name="Доза")


class Vaccination(models.Model):
    vac_date = models.CharField(null=True, verbose_name="Дата", max_length=100)
    vac_type = models.CharField(null=True, verbose_name="Вид вакцины", max_length=100)
    vac_no = models.CharField(null=True, verbose_name="№ серии", max_length=100)


class Health(models.Model):
    view_date = models.DateField(null=True, verbose_name="Дата осмотра")
    anamnez = models.CharField(max_length=50, null=True, verbose_name="Анамнез")
# Create your models here.
