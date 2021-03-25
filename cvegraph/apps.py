from django.apps import AppConfig


class CvegraphConfig(AppConfig):
    name = 'cvegraph'

    def ready(self):
        from cvegraph import updater
        updater.start()
