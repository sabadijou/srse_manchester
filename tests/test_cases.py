from srse_manchester.srse_manchester import DataCollector, explore_ontology
from unittest.mock import patch, Mock, mock_open
from .mock_response import mock_response as MR
import requests
import pytest


@pytest.fixture
def mock_response():
    mock = Mock(spec=requests.Response)
    mock.json.return_value = MR
    mock.status_code = 200
    return mock


@pytest.fixture
def mock_config():
    return {"api": {"ontology_uri": "http://www.ebi.ac.uk/ols4/api/ontologies/"}}


def test_data_collector_initialization():
    """
    Test : Ensures that the DataCollector instance is correctly initialized with a specified URI and ontology_id.
    """
    collector = DataCollector("http://www.ebi.ac.uk/ols4/api/ontologies/", ontology_id="hp")
    assert collector.uri == "http://www.ebi.ac.uk/ols4/api/ontologies/"
    assert collector.kwargs.get('ontology_id') == "hp"


@patch('requests.get')
def test_fetch_data_valid(mock_get, mock_response):
    """
    Test : fetch_data function in DataCollector with a valid response.
    """
    mock_get.return_value = mock_response
    collector = DataCollector("http://www.ebi.ac.uk/ols4/api/ontologies/", ontology_id="hp")
    response = collector.fetch_data()
    assert response == MR


@patch('requests.get', side_effect=requests.HTTPError("HTTP Error"))
def test_fetch_data_http_error(mock_get):
    """
    Test : fetch_data function in DataCollector for handling HTTP errors.
    """
    collector = DataCollector("http://www.ebi.ac.uk/ols4/api/ontologies/", ontology_id="invalid_ontology")
    with pytest.raises(requests.HTTPError):
        collector.fetch_data()


@patch('requests.get', side_effect=Exception("General Error"))
def test_fetch_data_general_error(mock_get):
    """
        Test : fetch_data function in DataCollector for handling General errors.
    """
    collector = DataCollector("http://www.ebi.ac.uk/ols4/api/ontologies/", ontology_id="hp")
    with pytest.raises(Exception):
        collector.fetch_data()


@patch('builtins.open', new_callable=mock_open,
       read_data="api: {ontology_uri: 'http://www.ebi.ac.uk/ols4/api/ontologies/'}")
@patch('requests.get')
def test_explore_ontology_valid(mock_get, mock_file, mock_response, mock_config):
    """
    Test : explore_ontology function with valid parameters.
    """
    mock_get.return_value = mock_response
    ontology = explore_ontology("hp", **mock_config)
    assert ontology is not None


@patch('builtins.open', new_callable=mock_open, read_data="api: {ontology_uri: "
                                                          "'http://www.ebi.ac.uk/ols4/api/ontologies/'}")
@patch('requests.get', side_effect=requests.HTTPError("HTTP Error"))
def test_explore_ontology_invalid(mock_get, mock_file):
    """
    Test : explore_ontology function with invalid parameters.
    """
    with pytest.raises(requests.HTTPError):
        explore_ontology("invalid_id")
