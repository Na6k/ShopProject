import os
from django.conf import settings
from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_root.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "shop_root.settings"
app = Celery("shop_root")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
