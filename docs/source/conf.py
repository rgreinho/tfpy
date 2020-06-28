# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath("../.."))

import aiohttp_theme


# -- Project information -----------------------------------------------------

project = "tfpy"
copyright = "2020, Rémy Greinhofer"
author = "Rémy Greinhofer"

# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "aiohttp_theme",
    "recommonmark",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}


# -- Options for HTML output -------------------------------------------------

html_static_path = ["_static"]
html_theme_path = [aiohttp_theme.get_path()]
html_theme = "aiohttp_theme"
html_theme_options = {
    "show_related": True,
    "page_width": "80%",
    "sidebar_width": "20%",
    "description": "Create Terraform resources using Python",
    "canonical_url": "https://github.com/rgreinho/tfpy",
    "github_user": "rgreinho",
    "github_repo": "tfpy",
    "github_button": True,
    "github_type": "star",
    "github_count": False,
    "github_banner": True,
}
html_sidebars = {"**": ["about.html", "navigation.html", "searchbox.html",]}

# Output file base name for HTML help builder.
htmlhelp_basename = "%sdoc" % project
