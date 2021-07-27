from setuptools import setup

setup(
    name = 'djangovehiclesapp',
    version = '0.0.1',
    author = 'Julian de Almeida Santos',
    author_email = 'julian.santos.info@gmail.com',
    packages=[
        'djangovehiclesapp',
        'djangovehiclesapp.management',
        'djangovehiclesapp.management.commands',
        'djangovehiclesapp.migrations',
    ],
    description = 'Django app to register vehicles.',
    long_description = 'Django app to register vehicles.',
    url = 'https://github.com/juliansantosinfo/djangovehiclesapp.git',
    project_urls = {
        'Código fonte': 'https://github.com/juliansantosinfo/djangovehiclesapp.git',
        'Download': 'https://github.com/juliansantosinfo/djangovehiclesapp/archive/0.0.1.zip'
    },
    install_requires=[
        'djangosimplemodels',
    ],
    license = 'MIT',
    keywords = 'vehicles app django',
)
