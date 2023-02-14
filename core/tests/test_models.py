import pytest

from core.models import Job


@pytest.fixture
def job(db):
    resultado = 'Programador - Delphi' \
                'https://www.adzuna.com.br/land/ad/' \
                '3875702246?se=QsRX1Eqs7RGIFziLgkel0A&v=FA4B9D64EAF9663C0668E522D547EE10C2323B36'

    return Job.objects.create(
        titulo=resultado.split('http')[0],
        url=resultado.split('//')[1]
    )


def test_default(job):
    assert job.titulo == 'Programador - Delphi'
    assert job.url == 'www.adzuna.com.br/land/ad/3875702246?se=QsRX1Eqs7RGIFziLgkel0A&v=FA4B9D64EAF9663C0668E522D547EE10C2323B36'
