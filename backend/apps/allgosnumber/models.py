from django.db import models


class Category_Region(models.Model):
    title = models.CharField("Регионы", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "регион"
        verbose_name_plural = "Добавление региона"

    def __str__(self):
        return self.title


class Category_Unaa(models.Model):
    title = models.CharField("Отделение", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "подраздиления"
        verbose_name_plural = "Добавление отдела УНАА"

    def __str__(self):
        return self.title


class Category_Number(models.Model):
    title = models.CharField("Номера", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "номера "
        verbose_name_plural = "Добавить регионый номер"

    def __str__(self):
        return self.title


class Add_Numbers(models.Model):
    category_region = models.ForeignKey(Category_Region, verbose_name='Регион', on_delete=models.PROTECT)
    category_unaa = models.ForeignKey(Category_Unaa, verbose_name='Отделение', on_delete=models.PROTECT)
    category_number = models.ForeignKey(Category_Number, verbose_name='Гос номер', on_delete=models.PROTECT)
    title = models.CharField(verbose_name="ввод номера", max_length=200)
    is_active = models.BooleanField("Активный", default=True)

    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        ordering = ["created"]
        verbose_name = "Добовления номеров в базу"
        verbose_name_plural = "Общая база номеров"

    def __str__(self):
        return f'{self.category_region} - {self.category_unaa} - {self.category_number} - {self.title}'