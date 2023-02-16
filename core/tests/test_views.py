import pytest
from django.urls import reverse_lazy

from core.django_assertions import assert_contains


def test_crawler(client, db):
    resp = client.get(reverse_lazy('crawler'))
    assert resp.status_code == 200
    assert resp.content == b'Bora Bill'
    data = {
        'r': 'w'
    }
    resp = client.post(reverse_lazy('crawler'), data)
    assert assert_contains(resp.content, '<title>')
