import sentry_sdk


class Sentry(object):

    def __init__(self, dsn, **kwargs):
        sentry_sdk.init(dsn, **kwargs)

    def report(self):
        sentry_sdk.capture_exception()

