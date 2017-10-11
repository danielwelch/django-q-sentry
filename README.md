### Note

This is a proposed [Django Q](https://github.com/Koed00/django-q/) plugin intended to serve as an accompaniment to the changes in Django Q proposed in this fork. This package does nothing until those changes are incorporated.

# django-q-sentry

A [Django Q](https://github.com/Koed00/django-q/) Error Reporter plugin adding Sentry support.

### Installation

This plugin is intended to be included with Django Q as [setuptools extra](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies).

`$ pip install django-q[sentry]`

Or add `django-q[sentry]` to `requirements.txt`.

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
