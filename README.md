
# django-q-sentry

A [Django Q](https://github.com/Koed00/django-q/) Error Reporter plugin adding Sentry support.
# Before version 0.1.3 sentry raven was a dependency. After 0.1.3 sentry-sdk used as raven is being deprecated.

### Installation

This plugin is intended to be included with Django Q as [setuptools extra](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies).

`$ pip install django-q[sentry]`

Or add `django-q[sentry]` to `requirements.txt`.

> This plugin requires Django Q version 0.8.1 or greater.

### Usage

Configure Sentry via the Django Q `Q_CLUSTER` dictionary in your Django project's `settings.py`. It is important that the `sentry` key be set in the `error_reporter` dictionary, as this name aligns with the project's entry point for this plugin. The only required configuration entry is your Sentry DSN.
```python
Q_CLUSTER = {
    'error_reporter': {
        'sentry': {
            'dsn': 'https://******@sentry.io/<project>'
        }
    }
}
```
Please check the [python sentry client configuration docs](https://docs.sentry.io/clients/python/) for more options. Additional key-value pairs defined in `Q_CLUSTER['error_reporter']['sentry']` are passed directly as kwargs to instantiation of [`raven.Client`](https://docs.sentry.io/clients/python/#configuring-the-client).
