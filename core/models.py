from django.db import models


class Job(models.Model):
    titulo = models.CharField(
        max_length=100
    )
    url = models.URLField(
        null=True, blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
