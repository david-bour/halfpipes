import pytest
from main import metadata_service

def test_can_fetch_metadata():
    expected = {'Metadata': {'version': '', 'environment': '', 'region': ''}}
    assert expected == metadata_service()