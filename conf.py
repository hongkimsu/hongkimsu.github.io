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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'demoblog'
copyright = '2023, demo'
author = 'demo'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_examples",
    "sphinxext.opengraph",
    # "sphinxext.rediraffe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_sidebars = {
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}


rediraffe_redirects = {
    "2023-01-01-markdown_blog_post.md": "blog/2023/2023-01-01-markdown_blog_post.md",
}
# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}
from pathlib import Path

for old, new in redirect_folders.items():
    for newpath in Path(new).rglob("**/*"):
        if newpath.suffix in [".ipynb", ".md"] and "ipynb_checkpoints" not in str(
            newpath
        ):
            oldpath = str(newpath).replace("blog/", "posts/", 1)
            # Skip pandoc because for some reason it's broken
            if "pandoc" not in str(newpath):
                rediraffe_redirects[oldpath] = str(newpath)

# -- ABlog ---------------------------------------------------

blog_baseurl = "https://hongkimsu.github.io"
blog_title = "demoblog"
blog_path = "blog"
blog_post_pattern = ["blog/*/*.ipynb", "blog/*/*.md"]
blog_feed_fulltext = True
blog_feed_subtitle = "Open communities, open science, communication, and data."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2


# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# MyST-NB
# Don't execute anything by default because many old posts don't execute anymore
# and this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "off"