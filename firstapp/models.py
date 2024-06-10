from django.db import models


class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default=None)
    # boolean_field = models.BooleanField(default=None)
    date_field = models.DateField(default=None)
    date_time_field = models.DateTimeField(default=None)
    duration_field = models.DurationField(default=None)
    email_field = models.EmailField(default=None)
    file_field = models.FileField(upload_to='files/',default=None)
    # file_path_field = models.FilePathField(path='/path/to/files/')
    float_field = models.FloatField(default=None)
    generic_ip_address_field = models.GenericIPAddressField(default=None)
    image_field = models.ImageField(upload_to='images/',default=None)
    integer_field = models.IntegerField(default=None)
    text_field = models.TextField(default=None)
    time_field = models.TimeField(default=None)
