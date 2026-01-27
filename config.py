"""
Configuration module for loading API keys securely.

This module loads API keys from environment variables or a secrets.env file.
Never hardcode API keys directly in notebooks or Python files.

Usage in notebooks:
    from config import get_api_key
    
    GOOGLE_API_KEY = get_api_key('GOOGLE_API_KEY')
    SERPAPI_KEY = get_api_key('SERPAPI_KEY')
"""

import os
from pathlib import Path


def load_env_file(env_file='secrets.env'):
    """
    Load environment variables from a .env file.
    
    Args:
        env_file (str): Path to the environment file
    
    Returns:
        dict: Dictionary of environment variables
    """
    env_path = Path(__file__).parent / env_file
    env_vars = {}
    
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        env_vars[key.strip()] = value.strip()
    
    return env_vars


def get_api_key(key_name, default=None):
    """
    Get an API key from environment variables or secrets.env file.
    
    Priority:
    1. System environment variables
    2. secrets.env file
    3. Default value (if provided)
    
    Args:
        key_name (str): Name of the API key (e.g., 'GOOGLE_API_KEY')
        default (str): Default value if key is not found
    
    Returns:
        str: The API key value
    
    Raises:
        ValueError: If the API key is not found and no default is provided
    """
    # Check system environment first
    value = os.environ.get(key_name)
    
    # If not in system env, try loading from secrets.env
    if value is None:
        env_vars = load_env_file()
        value = env_vars.get(key_name)
    
    # Use default if still not found
    if value is None:
        if default is not None:
            return default
        else:
            raise ValueError(
                f"API key '{key_name}' not found. "
                f"Please set it in your environment or create a 'secrets.env' file. "
                f"See 'secrets.env.example' for the template."
            )
    
    return value


# Convenience functions for specific API keys
def get_google_api_key():
    """Get Google Places API key."""
    return get_api_key('GOOGLE_API_KEY')


def get_serpapi_key():
    """Get SerpApi key (for TripAdvisor scraping)."""
    return get_api_key('SERPAPI_KEY')
