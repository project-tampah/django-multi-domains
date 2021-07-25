# django-multi-domains

This Django App sets specific [URL Confs](https://docs.djangoproject.com/en/dev/topics/http/urls/) for configured domains.

After all, the app has only a small middleware.

## Installation

```bash
pip install django-multi-domains
```

## Setup

The following configurations should be added in the [Django Settings](https://docs.djangoproject.com/en/dev/ref/settings/) Module.

1. Add `"multi_domains"` to `INSTALLED_APPS`

   ```python
   INSTALLED_APPS = [
       "...",
       "multi_domains",
   ]
   ```

2. Add middleware `"multi_domains.middleware.MultiDomainsMiddleware"` to the beginning of the `MIDDLEWARE`

   ```python
   MIDDLEWARE = [
       "multi_domains.middleware.MultiDomainsMiddleware",
       "...",
   ]
   ```

3. Define the mapping of domain and urlconf `MULTI_DOMAINS`

   ```python
   MULTI_DOMAINS = {
       "api.example.com": "api.urls",
       "shop.example.com": "shop.urls",
   }
   ```

If no mapping is set for a domain, `ROOT_URLCONF` is used as a fallback.
