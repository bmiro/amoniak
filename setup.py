from setuptools import setup

INSTALL_REQUIRES = [
    'empowering',
    'erppeek',
    'pymongo',
    'rq<0.4',
    'modeldict',
    'times',
    'raven'
]

setup(
    name='amoniak',
    version='0.1.0',
    packages=['amoniak'],
    url='http://gisce.net',
    license='MIT',
    install_requires=['empowering', 'erppeek', 'pymongo', 'rq', 'modeldict'],
    author='GISCE-TI, S.L.',
    author_email='ti@gisce.net',
    description='AMON Tools for GISCE-ERP'
)