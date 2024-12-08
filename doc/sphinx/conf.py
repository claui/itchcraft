# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pylint: skip-file
# type: ignore

project = 'Itchcraft'
copyright = '2024 Claudia Pellegrino'
executable = 'itchcraft'
author = 'Claudia Pellegrino <clau@tiqua.de>'
description = (
    'Tech demo for interfacing with heat-based USB insect bite healers'
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'autoapi.extension',
    'myst_parser',
    'sphinx.ext.autodoc',
]

autoapi_dirs = ['../../itchcraft']
autoapi_keep_files = True
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members',
]
autoapi_type = 'python'
autodoc_typehints = 'description'

html_theme = 'sphinx_rtd_theme'

python_display_short_literal_types = True
python_use_unqualified_type_names = True

myst_enable_extensions = [
    'deflist',
]


def skip_module(app, what, name, obj, skip, options):
    if what == 'data':
        return skip or name.endswith('.logger')
    if what == 'method':
        return skip or name.endswith('.__str__')
    if what == 'module':
        return skip or name in [
            'itchcraft.__main__',
            'itchcraft.cli',
            'itchcraft.fire_workarounds',
            'itchcraft.version',
            'itchcraft.settings',
        ]
    return skip


def setup(sphinx):
    sphinx.connect('autoapi-skip-member', skip_module)


templates_path = []
exclude_patterns = [
    '**/itchcraft/__main__/**',
    '**/itchcraft/cli/**',
    '**/itchcraft/fire_workarounds/**',
    '**/itchcraft/version/**',
    '**/itchcraft/settings/**',
]

# Man page output

man_pages = [
    (
        'usage',
        executable,
        description,
        [author],
        1,
    )
]

man_show_urls = True
