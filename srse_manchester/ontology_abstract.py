"""
ontology_abstract.py

Description: Module to handle ontology abstract class.

Author: Sadegh Abadijou
Email: s.abadijou@gmail.com
Created: 22/1/2024

"""

from abc import abstractmethod, ABC


class Ontology(ABC):
    """
    Base module representing ontology abstract class.
    """
    def __init__(self, **kwargs):
        """
        :param kwargs: Keyword arguments for Ontology parameters.
        """
        self.languages = kwargs.get('languages', None)

        self.lang = kwargs.get('lang', None)

        self.ontology_id = kwargs.get('ontologyId', None)

        self.loaded = kwargs.get('loaded', None)

        self.updated = kwargs.get('updated', None)

        self.status = kwargs.get('status', None)

        self.message = kwargs.get('message', None)

        self.version = kwargs.get('version', None)

        self.fileHash = kwargs.get('fileHash', None)

        self.loadAttempts = kwargs.get('loadAttempts', None)

        self.number_of_terms = kwargs.get('numberOfTerms', None)

        self.number_of_properties = kwargs.get('numberOfProperties', None)

        self.number_of_individuals = kwargs.get('numberOfIndividuals', None)

        self.config = Config(**kwargs.get('config', {}))

        self.base_uris = kwargs.get('baseUris', None)

        self.links = kwargs.get('_links', None)

    @abstractmethod
    def print_content(self):
        pass


class Config:
    """
    Config class for additional ontology metadata.
    """
    def __init__(self, **kwargs):
        """
        :param kwargs: Keyword arguments for Config parameters of Ontology.
        """
        self.versionIri = kwargs.get('versionIri', None)

        self.namespace = kwargs.get('namespace', None)

        self.preferredPrefix = kwargs.get('preferredPrefix', None)

        self.title = kwargs.get('title', None)

        self.description = kwargs.get('description', None)

        self.homepage = kwargs.get('homepage', None)

        self.version = kwargs.get('version', None)

        self.mailingList = kwargs.get('mailingList', None)

        self.tracker = kwargs.get('tracker', None)

        self.logo = kwargs.get('logo', None)

        self.creators = kwargs.get('creators', None)

        self.annotations = kwargs.get('annotations', None)

        self.fileLocation = kwargs.get('fileLocation', None)

        self.oboSlims = kwargs.get('oboSlims', None)

        self.labelProperty = kwargs.get('labelProperty', None)

        self.definitionProperties = kwargs.get('definitionProperties', None)

        self.synonymProperties = kwargs.get('synonymProperties', None)

        self.hierarchicalProperties = kwargs.get('hierarchicalProperties', None)

        self.baseUris = kwargs.get('baseUris', None)

        self.hiddenProperties = kwargs.get('hiddenProperties', None)

        self.preferredRootTerms = kwargs.get('preferredRootTerms', None)

        self.isSkos = kwargs.get('isSkos', None)

        self.allowDownload = kwargs.get('allowDownload', None)

