import os

__version__ = '0.3.3'
"""Library verison"""

STAC_VERSION = str(os.getenv('PYSTAC_VERSION', '0.8.1'))
"""STAC version"""
