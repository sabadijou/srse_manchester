# Ontology Lookup Service API Interaction Tool

This repository contains a Python application designed to interact with the Ontology Lookup Service API. The tool allows users to input an ontology ID and retrieve detailed ontology information. This document provides guidelines for running the application using Docker and Python package manager.

### Run the application through Docker
Clone the repository

```bash
git clone https://github.com/sabadijou/srse_manchester.git
```

To build the Docker image and run the application using a docker container, run the following commands in your terminal:

```bash

docker build -t srse_manchester .

docker run -it --rm srse_manchester
```
### Use application as a Python package
Install the package via pip:
```bash
pip install srse-manchester
```

#### Usage

After installation, you can intract with OLS as follows:

```bash
from srse_manchester import explore_ontology

ontology_info = explore_ontology(ontology_id='hp')

ontology_info.print_content()
```
Also you can print all ontology parameters for example
```bash
print(ontology_info.lang, ontology_info.config.title, ontology_info.config.annotations)
```

### Run the application through command line
To run the application through command line, run the following commands:
```bash
git clone https://github.com/sabadijou/srse_manchester.git

cd srse_manchester

python explorer.py
```

### Run tests 
To run tests, follow these steps:
```bash
pytest tests/
```
