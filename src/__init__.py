# src/__init__.py

"""
GameImageResizer Package Initialization

This package provides tools for resizing images to the nearest power of 2 dimensions.
"""

import os
import logging

# Setup basic logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function to read the configuration file
def read_config(file_path='config.txt'):
    """Reads the configuration file and returns the settings."""
    config = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                name, value = line.strip().split('=')
                config[name.strip().upper()] = value.strip()
        logger.info(f"Configuration loaded from {file_path}")
    except FileNotFoundError:
        logger.warning(f"{file_path} not found. Using default configuration.")
    return config

# Default configuration values
default_config = {
    'THRESHOLD': '0.25',
    'COMPRESSION': '0'
}

# Load configuration
config = read_config()
threshold = float(config.get('THRESHOLD', default_config['THRESHOLD']))
compression = int(config.get('COMPRESSION', default_config['COMPRESSION']))

__all__ = ['read_config', 'threshold', 'compression', 'logger']
