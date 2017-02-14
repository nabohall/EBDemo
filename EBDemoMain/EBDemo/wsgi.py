"""
WSGI config for EBDemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
raise RuntimeError("WSGI working directory: {}".format(os.getcwd()))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EBDemo.settings")

application = get_wsgi_application()
