import sentry_sdk


class Sentry(object):

    def __init__(self, dsn, **kwargs):
        self.client = sentry_sdk.init(dsn=dsn, **kwargs)

    def report(self):
        sentry_sdk.capture_exception()
