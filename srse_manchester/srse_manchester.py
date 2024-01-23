
from an_ontology import AnOntology
import requests
import argparse
import logging
import yaml
import os


class DataCollector:
    def __init__(self, ontology_endpoint, **kwargs):

        self.uri = ontology_endpoint

        self.kwargs = kwargs

    def fetch_data(self):
        try:
            response = requests.get(os.path.join(self.uri, self.kwargs.get('ontology_id')))
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
        return None


def explore_ontology(ontology_id, **kwargs):
    with open("config.yml", "r") as config:
        cfg = yaml.load(config, yaml.Loader)

    collector = DataCollector(ontology_endpoint=cfg["api"]["ontology_uri"],
                              ontology_id=ontology_id)
    data = collector.fetch_data()
    if data is not None:
        ontology_instance = AnOntology(**data)
        return ontology_instance
    else:
        print("Failed to retrieve data.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    parser = argparse.ArgumentParser(description='Ontology Lookup Service')

    parser.add_argument('--ontology_id', type=str, help='The ID of the ontology to fetch data from')

    args = parser.parse_args()

    ontology = explore_ontology(args.ontology_id)

    if ontology is not None:
        ontology.print_content()
