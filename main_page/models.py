from django.db import models
import uuid
import os
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.title}: {self.position}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/dishes', f'{uuid.uuid4()}.{ext}')

    title = models.CharField(max_length=50, unique=True, db_index=True)
    ingredients = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=False)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.position}'

    class Meta:
        ordering = ('position',)


class Event(models.Model):
    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join("images/event", f'{uuid.uuid4()}.{ext}')

    title = models.CharField(max_length=50, unique=True, db_index=True)
    price = models.PositiveSmallIntegerField()
    desc = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join("images/gallery", f'{uuid.uuid4()}.{ext}')

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    title = models.CharField(max_length=50, unique=True, db_index=True)


class Chef(models.Model):
    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join("images/chef", f'{uuid.uuid4()}.{ext}')

    name = models.CharField(max_length=20, unique=True, db_index=True)
    surname = models.CharField(max_length=20, unique=True, db_index=True)
    staff = models.CharField(max_length=20, unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Response(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join("images/response", f'{uuid.uuid4()}.{ext}')

    def validate_even(stars: int):
        if not 0 < stars <= 5:
            raise ValidationError(
                _('Для відгуку повинно поставити від 1 до 5 зірочок'),
                params={'stars': stars},
            )

    name = models.CharField(max_length=20, unique=True, db_index=True)
    surname = models.CharField(max_length=20, unique=True, db_index=True)
    prof = models.CharField(max_length=20, unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    resp = models.TextField(max_length=200, blank=True)
    stars = models.PositiveSmallIntegerField(validators=[validate_even], default=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Why_us(models.Model):
    num = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.TextField(max_length=200, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}: {self.num}'

    class Meta:
        ordering = ('num',)


class About(models.Model):

    def get_file_name1(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join("images/about_us/background_img", f'{uuid.uuid4()}.{ext}')

    def get_file_name2(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join("images/about_us/img", f'{uuid.uuid4()}.{ext}')

    mobile_phone_re = RegexValidator(regex=r'(^\+380)(-|\s)?(\d{2})(-|\s)?(\d{3})(-|\s)?(\d{2})(-|\s)?(\d{2})',
                                     message='Некоректно введено номер телефону.')
    back_img = models.ImageField(upload_to=get_file_name1)
    phone_num = models.CharField(max_length=20, validators=[mobile_phone_re])
    desc = models.TextField(max_length=500, blank=True)
    img = models.ImageField(upload_to=get_file_name2)
    video_link = models.CharField(max_length=1000)
    is_visible = models.BooleanField(default=True)


class Footer(models.Model):
    mobile_phone_re = RegexValidator(regex=r'(^\+380)(-|\s)?(\d{2})(-|\s)?(\d{3})(-|\s)?(\d{2})(-|\s)?(\d{2})',
                                     message='Некоректно введено номер телефону.')
    email_re = RegexValidator(regex=r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$',
                              message='Некоректно введено пошту.')
    address = models.CharField(max_length=250)
    name_city = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20, validators=[mobile_phone_re])
    email = models.CharField(max_length=100, validators=[email_re])
    work_time = models.CharField(max_length=100)
    close_time = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address}: {self.name_city}: {self.phone_num}: : {self.email}'
