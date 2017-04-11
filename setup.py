"""
CARTO tile data extraction from postgresql log
"""

from setuptools import setup, find_packages

setup(
    name="tiles_data_extractor",
    version='0.0.1',
    description='Log cruncher with the purpose of tile data extraction',
    url='https://github.com/cartodb/tile_data_extractor',
    author='CARTO Engine Team',
    author_email='engine@carto.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: ',
        'Topic :: ',
        'License :: OSI Approbed :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='postgresql log tile parser',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['postgresql_log_parser', 'psqlparse'],
    extras_require={
        'dev': ['ipdb', 'ipython'],
        'test': ['nose', 'nose-timer']
    }
)
