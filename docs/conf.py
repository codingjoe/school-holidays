"""Sphinx configuration file."""

from pkg_resources import get_distribution

project = "school-holidays"
copyright = "2019, voiio GmbH"
release = get_distribution('school-holidays').version
version = '.'.join(release.split('.')[:2])

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
