#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Katherine Dykes',
 'author_email': 'systems.engineering@nrel.gov',
 'description': 'NREL WISDEM turbine cost models',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license' : 'Apache License, Version 2.0',
 'name': 'Turbine_CostsSE',
 'package_data': {'Turbine_CostsSE': []},
 'package_dir': {'': 'src'},
 'packages': ['turbine_costsse', 'nrel_csm_tcc'],
 'zip_safe': False}


setup(**kwargs)

