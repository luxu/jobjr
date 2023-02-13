import pytest

from core.models import Job


@pytest.fixture
def job(db):
    return Job.objects.create()


def test_default(job):
    assert job.titulo == 'Alexa'
    assert job.url == ''
