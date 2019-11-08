Getting Started
===============

This page details how to get started with molecool.

molecool is currently under development, and can not yet be installed from PyPi or conda.

Installation
------------

**These instructions assume you have the python package manager conda installed.**

To install molecool, navigate to the GitHub repository and clone it.

To do a developmental install, type,

"pip install -e ."

Dependencies
^^^^^^^^^^^^
You need to install numpy and matplotlib.

Usage
-----

Once installed, you can use the package. This example draws a benzene molecule from an xyz file.::

  import molecool

  benzene_symbols, benzene_coords = molecool.open_xyz('benzene.xyz')
