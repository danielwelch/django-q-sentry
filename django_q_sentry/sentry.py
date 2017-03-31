import raven


class Sentry(object):

    def __init__(self, dsn, **kwargs):
        self.client = raven.Client(dsn, **kwargs)

    def report(self):
        self.client.captureException()
