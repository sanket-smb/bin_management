# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bin_management/__init__.py
from bin_management import __version__ as version

setup(
	name='bin_management',
	version=version,
	description='Bin Reports and Total Stock',
	author='SMB',
	author_email='smb@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
