from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)  # 使用 db_column 参数
    catchphrase = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'people'