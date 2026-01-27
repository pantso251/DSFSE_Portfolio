#!/usr/bin/env python3
"""
Script to remove hardcoded API keys from Jupyter notebooks and replace them
with secure config imports.
"""

import json
import re
from pathlib import Path


def update_google_maps_notebook():
    """Update google_maps_reviews_words.ipynb to use config module."""
    notebook_path = Path('learning-goals/goal-2-web-scraping/google_maps_reviews_words.ipynb')
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Update cells
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Replace hardcoded API key with config import
            if 'GOOGLE_API_KEY = "AIza' in source:
                # Replace the hardcoded key line
                new_source = re.sub(
                    r'GOOGLE_API_KEY = "AIza[^"]*".*',
                    '# Load API key securely from environment\nfrom config import get_api_key\nGOOGLE_API_KEY = get_api_key(\'GOOGLE_API_KEY\')',
                    source
                )
                cell['source'] = new_source.split('\n')
                # Ensure each line ends with \n except the last
                cell['source'] = [line + '\n' if i < len(cell['source'])-1 else line 
                                 for i, line in enumerate(cell['source'])]
    
    # Save the updated notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"✅ Updated {notebook_path}")


def update_trip_reviews_notebook():
    """Update trip_reviews.ipynb to use config module."""
    notebook_path = Path('learning-goals/goal-2-web-scraping/trip_reviews.ipynb')
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Update cells
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Replace hardcoded API key with config import
            if 'API_KEY = "132be' in source:
                # Replace the hardcoded key line
                new_source = re.sub(
                    r'API_KEY = "132be[^"]*".*',
                    '# Load API key securely from environment\nfrom config import get_api_key\nAPI_KEY = get_api_key(\'SERPAPI_KEY\')',
                    source
                )
                cell['source'] = new_source.split('\n')
                # Ensure each line ends with \n except the last
                cell['source'] = [line + '\n' if i < len(cell['source'])-1 else line 
                                 for i, line in enumerate(cell['source'])]
    
    # Save the updated notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"✅ Updated {notebook_path}")


if __name__ == '__main__':
    update_google_maps_notebook()
    update_trip_reviews_notebook()
    print("\n✅ All notebooks updated to use secure API key loading!")
    print("📝 Don't forget to create your secrets.env file from secrets.env.example")
