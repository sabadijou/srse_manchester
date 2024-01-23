from abc import abstractmethod, ABC


class Ontology(ABC):
    def __init__(self, **kwargs):
        self.languages = kwargs.get('languages')

        self.lang = kwargs.get('lang')

        self.ontology_id = kwargs.get('ontologyId')

        self.loaded = kwargs.get('loaded')

        self.updated = kwargs.get('updated')

        self.status = kwargs.get('status')

        self.message = kwargs.get('message')

        self.version = kwargs.get('version')

        self.fileHash = kwargs.get('fileHash')

        self.loadAttempts = kwargs.get('loadAttempts')

        self.number_of_terms = kwargs.get('numberOfTerms')

        self.number_of_properties = kwargs.get('numberOfProperties')

        self.number_of_individuals = kwargs.get('numberOfIndividuals')

        self.config = Config(**kwargs.get('config'))

        self.base_uris = kwargs.get('baseUris')

        self.links = kwargs.get('_links')

    @abstractmethod
    def print_content(self):
        pass


class Config:
    def __init__(self, **kwargs):

        self.versionIri = kwargs.get('versionIri')

        self.namespace = kwargs.get('namespace')

        self.preferredPrefix = kwargs.get('preferredPrefix')

        self.title = kwargs.get('title')

        self.description = kwargs.get('description')

        self.homepage = kwargs.get('homepage')

        self.version = kwargs.get('version')

        self.mailingList = kwargs.get('mailingList')

        self.tracker = kwargs.get('tracker')

        self.logo = kwargs.get('logo')

        self.creators = kwargs.get('creators')

        self.annotations = kwargs.get('annotations')

        self.fileLocation = kwargs.get('fileLocation')

        self.oboSlims = kwargs.get('oboSlims')

        self.labelProperty = kwargs.get('labelProperty')

        self.definitionProperties = kwargs.get('definitionProperties')

        self.synonymProperties = kwargs.get('synonymProperties')

        self.hierarchicalProperties = kwargs.get('hierarchicalProperties')

        self.baseUris = kwargs.get('baseUris')

        self.hiddenProperties = kwargs.get('hiddenProperties')

        self.preferredRootTerms = kwargs.get('preferredRootTerms')

        self.isSkos = kwargs.get('isSkos')

        self.allowDownload = kwargs.get('allowDownload')

