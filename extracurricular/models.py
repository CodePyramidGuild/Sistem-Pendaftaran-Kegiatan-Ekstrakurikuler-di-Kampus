from django.db import models

class Kegiatan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
