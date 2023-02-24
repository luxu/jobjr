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

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'url': self.url,
        }

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['titulo']
