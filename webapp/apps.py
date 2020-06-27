from django.apps import AppConfig


class WebappConfig(AppConfig):
    name = 'webapp'
    def ready(self):
        import webapp.signals
