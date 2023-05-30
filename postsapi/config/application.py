# -*- coding: utf-8 -*-
"""WSGI application initialization for postsapi."""
from postsapi.config.app_cfg import base_config

__all__ = ['make_app']


def make_app(global_conf, **app_conf):
    """
    Set postsapi up with the settings found in the PasteDeploy configuration
    file used.

    :param dict global_conf: The global settings for postsapi
                             (those defined under the ``[DEFAULT]`` section).

    :return: The postsapi application with all the relevant middleware
        loaded.

    This is the PasteDeploy factory for the postsapi application.

    ``app_conf`` contains all the application-specific settings (those defined
    under ``[app:main]``.
    """
    app = base_config.make_wsgi_app(global_conf, app_conf, wrap_app=None)

    # Wrap your final TurboGears 2 application with custom middleware here

    return app
