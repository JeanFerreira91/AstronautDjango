"""
ASGI config for AstronautProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Ensure DJANGO_SETTINGS_MODULE is set properly based on your project name!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AstronautProject.settings')
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from django_idom import IDOM_WEBSOCKET_PATH

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": SessionMiddlewareStack(
            AuthMiddlewareStack(URLRouter([IDOM_WEBSOCKET_PATH]))
        ),
    }
)