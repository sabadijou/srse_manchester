"""
data_collector.py

Main Module

Description: Module for collecting data from an ontology endpoint and exploring ontology data.

Author: Sadegh Abadijou
Email: s.abadijou@gmail.com
Created: 22/1/2024
"""

from .an_ontology import AnOntology
import requests
import logging
import yaml
import os


class DataCollector:
    def __init__(self, ontology_endpoint, **kwargs):
        """
        :param ontology_endpoint: the base URI for the ontology endpoint
        :param kwargs: Arbitrary keyword arguments, typically includes 'ontology_id'.
        """
        self.uri = ontology_endpoint

        self.kwargs = kwargs

    def fetch_data(self):
        """
        Fetch data from the ontology endpoint. Handle HTTP and general errors.
        :return: The JSON response data from the ontology endpoint or None if an error occurs.
        """
        # ToDo The api return 500 instead of 404 when ontology not exists
        try:
            response = requests.get(os.path.join(self.uri, self.kwargs.get('ontology_id')))
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
            raise http_err
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
            raise err


def explore_ontology(ontology_id, **kwargs):
    """
    Explore and return an instance of AnOntology based on the provided ontology_id and other parameters.

    :param ontology_id: The ID of the ontology to be fetched and explored.
    :param kwargs: Arbitrary keyword arguments used for additional arguments.
    :return: An instance of specific Ontology
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(current_dir, 'config.yml')

    with open(config_path, "r") as config:
        cfg = yaml.load(config, yaml.Loader)

    collector = DataCollector(ontology_endpoint=cfg["api"]["ontology_uri"],
                              ontology_id=ontology_id)
    data = collector.fetch_data()
    if data is not None:
        ontology_instance = AnOntology(**data)
        return ontology_instance
    else:
        print("Failed to retrieve data.")