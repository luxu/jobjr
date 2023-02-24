import pytest
from django.urls import reverse_lazy

from core.models import Job


@pytest.fixture
def jobs(db):
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

    for job in vagas:
        Job.objects.create(
            titulo=job['titulo'],
            url=job['url'],
        )

    return Job


def test_listar(client, jobs):
    resp = client.get(reverse_lazy('listar_api'))
    assert resp.status_code == 200
    assert resp.json()['count'] == 2


def test_deletar_tendo_vagas(client, jobs):
    resp = client.get(reverse_lazy('excluir_api'))
    assert resp.json()['msg'] == 'OK'
    assert len(jobs.objects.all()) == 0


def test_deletar_nao_tendo_vagas(client, db):
    resp = client.get(reverse_lazy('excluir_api'))
    assert resp.json()['msg'] == 'Não há vagas a serem apagadas!'
