from django.db import models


class Category_Unaa(models.Model):
    title = models.CharField("Наименование отделов", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "подраздиления"
        verbose_name_plural = "Подраздиление УНАА"

    def __str__(self):
        return self.title


class Category_Types(models.Model):
    title = models.CharField("Типы", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "типы"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.title


class Category_Number(models.Model):
    title = models.CharField("Номера", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "номера "
        verbose_name_plural = "Региональный номер"

    def __str__(self):
        return self.title


class Add_Numbers(models.Model):
    category_unaa = models.ForeignKey(Category_Unaa, verbose_name='Отделение', on_delete=models.CASCADE)
    category_types = models.ForeignKey(Category_Types, verbose_name='Типы', on_delete=models.CASCADE)
    category_number = models.ForeignKey(Category_Number, verbose_name='Гос номер', on_delete=models.CASCADE)
    number = models.CharField(verbose_name="Гос номер", max_length=50)
    application = models.CharField(verbose_name="Номер заявки", max_length=50)

    is_active = models.BooleanField("Активный", default=True)

    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Добовления номеров в базу"
        verbose_name_plural = "Общая база номеров"

    def __str__(self):
        return f'{self.category_types} - {self.category_unaa} - {self.category_number} - {self.application}'
