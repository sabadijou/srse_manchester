"""
an_ontology.py

Description: Module to handle specific ontology operations.

Author: Sadegh Abadijou
Email: s.abadijou@gmail.com
Created: 22/1/2024

"""

from .ontology_abstract import Ontology
from abc import ABC


class AnOntology(Ontology, ABC):
    """
    Extend Ontology
    Represents a specific ontology with print functionality.
    """
    def __init__(self, **kwargs):
        """
        :param kwargs: Keyword arguments for Ontology parameters.
        """
        super().__init__(**kwargs)

    def print_content(self):
        """
        Overwrite print_content from abstract Ontology class
        Print : Ontology title
        Print : Ontology description
        Print : How many terms Ontology includes
        Print : Current status of Ontology
        :return:
        """
        print('Ontology title : {ontology_title} \n '
              'Ontology description : {ontology_description} \n '
              'Number of terms : {number_of_terms} \n '
              'Current status : {current_status} '.format(ontology_title=self.config.title,
                                                          ontology_description=self.config.description,
                                                          number_of_terms=self.number_of_terms,
                                                          current_status=self.status))
