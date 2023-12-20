from django.db import models
from django.contrib.auth.models import User  # Вы можете использовать стандартную модель пользователя


class Profile(models.Model):  # Используйте отдельную модель профиля
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с пользователем
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    phone = models.DecimalField('Номер Тел:', max_digits=18, decimal_places=10)
    email = models.EmailField('Электронная почта')
    photo = models.ImageField('Аватар', upload_to='photo/')  # Удалите начальную точку
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"