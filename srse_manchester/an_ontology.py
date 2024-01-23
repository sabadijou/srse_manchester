from abc import ABC

from ontology_abstract import Ontology


class AnOntology(Ontology, ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def print_content(self):
        print('Ontology title : {ontology_title} \n '
              'Ontology description : {ontology_description} \n '
              'Number of terms : {number_of_terms} \n '
              'Current status : {current_status} '.format(ontology_title=self.config.title,
                                                          ontology_description=self.config.description,
                                                          number_of_terms=self.number_of_terms,
                                                          current_status=self.status))
