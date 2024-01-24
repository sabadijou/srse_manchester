from srse_manchester.srse_manchester import explore_ontology
import sys
import argparse
import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)

    parser = argparse.ArgumentParser(description='Ontology Lookup Service')

    parser.add_argument('--ontology_id', type=str, help='The ID of the ontology to fetch data from')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    ontology = explore_ontology(args.ontology_id)

    if ontology is not None:
        ontology.print_content()

