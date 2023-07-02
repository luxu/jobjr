from http import HTTPStatus

import pytest
from django.urls import reverse_lazy, reverse

from core.models import Job
import json

CT_JSON = 'application/json'


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


def test_salvar_api(client, db):
    data = {
        'titulo': 'Desenvolvedor(a) Python Sênior',
        'url': 'https://programathor.com.br/jobs//28102-desenvolvedor-a-node-js-pleno'
    }
    resp = client.post(reverse('salvar_api'), data=data)
    assert resp.status_code == HTTPStatus.CREATED
    response_data = resp.json()
    assert response_data['titulo'] == 'Desenvolvedor(a) Python Sênior'
    assert response_data['url'] == 'https://programathor.com.br/jobs//28102-desenvolvedor-a-node-js-pleno'


def test_listar_api(client, Vaga):
    resp = client.get(reverse_lazy('listar_api'))
    assert resp.status_code == 200
    assert len(resp.json()['data']) == 2


def test_listar_api_github(client, db):
    client.get(reverse_lazy('crawler_api_github'))
    jobs = Job.objects.all()
    assert jobs is not None
    jobs = None
    resp = client.get(reverse_lazy('index'))
    assert resp.status_code == 200


def test_deletar_banco_vazio(client, db):
    resp = client.get(reverse_lazy('excluir_api'))
    assert resp.json()['msg'] == 'Não há vagas a serem apagadas!'


def test_deletar_banco_com_dados(client, Vaga):
    resp = client.get(reverse_lazy('excluir_api'))
    assert resp.json()['msg'] == 'OK'
