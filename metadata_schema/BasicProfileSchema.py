from ResourceSchema import Resources
from ReferenceSchema import References
from PersonSchema import Person
from IdentifierSchema import Identifier
from RelatedCatalogItemSchema import RelatedCatalogItem

from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class ModelTypeEnum(str, Enum):
    model = "model"
    framework = "framework"
    tool = "tool"
    testbed = "testbed"

"""Definitions
    model = a representation of a system via physics, mathematics, or empirical data, that can be used to approximate
        the system in question and used to conduct research or apply research to a management application
    framework = a modeling system composed of multiple component models or modules, which themselves could be described
        by a model catalog item. Sometimes known as a coupled model (Example: COAWST, HayWired, National Seismic Hazard Mapping Project)
    tool = a tool is not the model algorithm or code itself, but either 1) an interface built to facilitate
        interaction between a user and the model, or 2) a pre-processing or post-processing program used to prepare
        inputs or outputs for the model algorithm
    testbed = Infrastructure that allows you to understand model and data integration and performance (See, for
        example, https://www.ilamb.org/, or the USGS HyTest project)
"""


class TypeKeywordEnum(str, Enum):

    analytical = "Analytical"
    conceptual = "Conceptual"
    data_driven = "Data-Driven"
    deterministic = "Deterministic"
    empirical = "Empirical"
    geospatial = "Geospatial"
    mathematical = "Mathematical"
    numerical = "Numerical"
    mechanistic = "Mechanistic"
    physics_based = "Physics-based"
    process_based = "Process-based"
    statistical = "Statistical"
    stochastic = "Stochastic"
    
    

"""Definitions
    Analytical = Analytical models are mathematical models that have a closed form solution, i.e. the solution to the equations used to describe changes in a system can be expressed as a mathematical analytic function. (https://serc.carleton.edu/introgeo/mathstatmodels/Analytical.html)
    Conceptual = A conceptual model is a representation of a system, made of the composition of concepts
        which are used to help people know, understand, or simulate a subject the model represents. 
    Data-Driven = 
    Deterministic = the output of the model is fully determined by the parameter values and the initial conditions (set of inputs);
    Empirical = refers to any kind of computer modeling based on empirical/experimental observations rather than on mathematically describable relationships of the system modeled;
    Geospatial =
    Mathematical = a description of a system using mathematical concepts and language
    Mechanistic = assumes that a complex system can be understood by examining the workings of its individual parts and the manner in which they are coupled. Mechanistic models typically have a tangible, physical aspect, in that system components are real, solid and visible;
    Numerical = Numerical models are mathematical models that use some sort of numerical time-stepping procedure to obtain the models behavior over time. (SERC https://serc.carleton.edu/introgeo/mathstatmodels/Numerical.html)
    Physics-based = using equations based on laws of physics
    Process-based = based on a theoretical understanding of relevant physical processes
    Statistical = a mathematical model that embodies a set of statistical assumptions concerning the generation of sample data (and similar data from a larger population) (wikipedia)
    Stochastic = also called a probabilistic model, incorporates random variables and probability distributions into the model of an event or phenomenon. While a deterministic model gives a single possible outcome for an event, a probabilistic model gives a probability distribution as a solution;
"""


class BasicProfile(BaseModel):
    """Basic metadata profile

    Fields
    ------
    item_type : ModelTypeEnum
        model, tool, framework, testbed
    name : str
        title
    description : str
        abstract or general description
    organization: bool = 1
        1 = usgs ; 0 = external
    external_organization_name: Optional[str]
    release_date : str
        Date
    last_update : str
        Date
    author : Optional[List[Person]]
        The author(s) or developer(s) of this content.
    contact : Optional[List[Person]]
        Person(s) responsible for maintenance of the model or item.
    version : str
        Latest release version v1.0.0
    how_to_cite: Optional[str]
        Preferred citation format
    usgs_missionarea: Optional[str]
        USGS mission area
    identifier: Optional[List[Identifier]]
        Identifiers related to the model
    programming_language: Optional[str]
        Primary programming language used for the modeling
    license: Optional[str]
       CC0 see: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    resources: Optional[Resources]
        Custom object containing advanced resource section
    references: Optional[References]
        Custom object containing advanced reference section
    science_keywords: Optional[str]
        Topical science keywords that will help for discovering the item. Preferred to use terms from the USGS Thesaurus please see: https://apps.usgs.gov/thesaurus/
    type_keywords: Optional[TypeKeywordEnum]
    other_keywords: Optional[str]
        For example, platform and mode (Jupyter, Graphical User Interface, etc).
    image: Optional[HttpUrl]
        Header image for the model profile page
    related_catalog_items: Optional[List[str]]
        coawst - wrf item
    related_catalog_item_types: Optional[str]

    Example
    -------
    >>> BasicProfile(item_type="model",
    ...              name="COAWST",
    ...              description="sample description")
    BasicProfile(item_type=<ModelTypeEnum.model: 'model'>, name='COAWST', description='sample description', organization=1, external_organization_name=None, release_date=None, last_update=None, subtitle=None, author=None, contact=None, version=None, how_to_cite=None, usgs_missionarea=None, identifier=None, programming_language=None, license='CC0', resources=None, references=None, science_keywords=None, type_keywords=None, other_keywords=None, image=None, related_catalog_item=None)
    """

    _version: str = "v1.0.0"

    item_type: ModelTypeEnum = "model"
    name: str
    description: str
    organization: bool = 1
    external_organization_name: Optional[str]
    release_date: Optional[str]
    last_update: Optional[str]
    subtitle: Optional[str]
    author: Optional[List[Person]]
    contact: Optional[List[Person]]
    version: Optional[str]
    how_to_cite: Optional[str]
    usgs_missionarea: Optional[str]
    identifier: Optional[List[Identifier]]
    programming_language: Optional[str]
    license: Optional[str] = "CC0"
    resources: Optional[Resources]
    references: Optional[References]
    science_keywords: Optional[List[str]]
    type_keywords: Optional[TypeKeywordEnum]
    other_keywords: Optional[str]
    image: Optional[HttpUrl]
    related_catalog_item: Optional[RelatedCatalogItem]
