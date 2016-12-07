# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', 'pacbum', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = 'Lucas S. Souza'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name='pacbum',
    version=version,
    author='Lucas S. Souza',
    author_email='lucas.soaresouza@gmail.com',
    url='https://github.com/fis-jogos/ep1-ls',
    description='The Lord of the Time! PacBUm!',
    long_description=codecs.open('README.rst', 'rb', 'utf8').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[ 
    'FGAme',
    'pygame',
    'pgzero'
    ],
    package_data={
        'pacbum': [
             'pacbum/images/*.*',
	     'pacbum/assets/*.*',
	     'pacbum/assets/sfx/*.*'
        ],
    },
    extras_require={
        'dev': [
            'python-boilerplate[dev]',
        ],
    },
    entry_points={
       'console_scripts': [
            'pacbum = pacbum.__main__:main'
        ],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)
