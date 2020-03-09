from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'




    #####################     triggering the signals      ######################

    def ready(self):
        import dashboard.signals