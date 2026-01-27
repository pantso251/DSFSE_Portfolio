# API Keys Security Guide

## ⚠️ Important Security Notice

**NEVER commit API keys to version control!** This repository uses environment variables to keep API keys secure.

## 🔑 Setting Up Your API Keys

### Step 1: Create your secrets file

Copy the example template:
```bash
cp secrets.env.example secrets.env
```

### Step 2: Add your API keys

Edit `secrets.env` and replace the placeholder values with your actual API keys:

```bash
# secrets.env
GOOGLE_API_KEY=AIzaSyD4zNLt3VtqjGW7ZYDRbGG8lQSvsdY4htA
SERPAPI_KEY=132be331306d1619add51865f414944dec9bddda3e4abeedf375265e566f00b4
```

### Step 3: Verify the file is ignored by git

The `secrets.env` file is already listed in `.gitignore`, so it won't be committed. You can verify this by running:

```bash
git status
```

Your `secrets.env` should NOT appear in the list of untracked files.

## 📓 Using API Keys in Notebooks

In your Jupyter notebooks, import the API keys using the `config` module:

```python
# At the top of your notebook
from config import get_api_key

# Load your API keys
GOOGLE_API_KEY = get_api_key('GOOGLE_API_KEY')
SERPAPI_KEY = get_api_key('SERPAPI_KEY')

# Now use them in your code
# ...
```

## 🔒 Security Best Practices

1. **Never hardcode API keys** directly in notebooks or Python files
2. **Always use environment variables** or a secrets file
3. **Add secrets files to `.gitignore`** to prevent accidental commits
4. **Use different API keys** for development and production
5. **Rotate your API keys** if they are accidentally exposed
6. **Limit API key permissions** to only what's needed

## 🚨 What to Do If You Accidentally Commit an API Key

If you accidentally commit an API key to the repository:

1. **Immediately revoke/regenerate** the API key in the service's console
2. **Remove the key from git history** using tools like `git-filter-branch` or `BFG Repo-Cleaner`
3. **Update your local `secrets.env`** with the new key
4. **Never just delete the file** - the key remains in git history!

## 📚 Where to Get API Keys

### Google Places API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the "Places API"
4. Go to Credentials and create an API key
5. Restrict the API key to only the APIs you need

### SerpApi (for TripAdvisor)
1. Sign up at [SerpApi](https://serpapi.com/)
2. Go to your dashboard
3. Copy your API key
4. Note: Free tier has limited requests per month

## ✅ Verification

To test if your API keys are loaded correctly, run this in a Python console:

```python
from config import get_api_key

try:
    google_key = get_api_key('GOOGLE_API_KEY')
    print("✅ Google API key loaded successfully")
except ValueError as e:
    print(f"❌ Error: {e}")

try:
    serpapi_key = get_api_key('SERPAPI_KEY')
    print("✅ SerpApi key loaded successfully")
except ValueError as e:
    print(f"❌ Error: {e}")
```

## 📖 Additional Resources

- [Google Cloud API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
