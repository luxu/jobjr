import pytest

from core.models import Job


@pytest.fixture
def Vaga(db):
    vagas = [
        {
            "titulo": "Desenvolvedor(a) Javascript Sênior",
            "url": "https://programathor.com.br/jobs//28111-desenvolvedor-a-javascript-senior"
        },
        {
            "titulo": "Desenvolvedor(a) Node.js Pleno",
            "url": "https://programathor.com.br/jobs//28102-desenvolvedor-a-node-js-pleno"
        }
    ]

    for vaga in vagas:
        Job.objects.create(
            titulo=vaga['titulo'],
            url=vaga['url'],
        )
    return Job


def test_titulo(Vaga):
    jobs = Vaga.objects.filter(id=1)
    for job in jobs:
        assert job.titulo == 'Desenvolvedor(a) Javascript Sênior'
        assert job.url == "https://programathor.com.br/jobs//28111-desenvolvedor-a-javascript-senior"


def test_deletar(Vaga):
    jobs = Vaga.objects.all()
    jobs.delete()
    assert len(jobs) == 0
