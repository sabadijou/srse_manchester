from setuptools import setup, find_packages

setup(
    name='srse_manchester',
    version='1.0.1',
    packages=find_packages(),
    description='My Ontology Lookup Service',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sabadijou/srse_manchester/',
    author='Sadegh Abadijou',
    author_email='s.abadijou@gmail.com',
    license='MIT',
    include_package_data=True,
    install_requires=[
        'certifi==2023.11.17',
        'charset-normalizer==3.3.2',
        'colorama==0.4.6',
        'coverage==7.4.0',
        'exceptiongroup==1.2.0',
        'idna==3.6',
        'iniconfig==2.0.0',
        'packaging==23.2',
        'pluggy==1.3.0',
        'pytest==7.4.4',
        'pytest-cov==4.1.0',
        'requests==2.31.0',
        'tomli==2.0.1',
        'urllib3==2.1.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
