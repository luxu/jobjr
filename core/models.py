from django.db import models


class Job(models.Model):
    titulo = models.CharField(
        max_length=100,
        default=None
    )
    url = models.URLField(
        max_length=200
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
