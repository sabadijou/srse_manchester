from srse_manchester.srse_manchester import explore_ontology
import logging


def main():
    logging.basicConfig(level=logging.ERROR)

    while True:
        ontology_id = input("Enter ontology ID (or 'exit' to quit): ").strip()

        if ontology_id.lower() == 'exit':
            print("Exiting program.")
            break

        ontology = explore_ontology(ontology_id)

        if ontology is not None:
            ontology.print_content()


if __name__ == '__main__':
    main()
