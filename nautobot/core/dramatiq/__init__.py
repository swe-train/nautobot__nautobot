#
# This file is derived in part from https://github.com/Bogdanp/django_dramatiq
#
# :copyright: Copyright 2017 Bogdan Paul Popa
# :license: Apache License 2.0, see NOTICE for more details.
#

import dramatiq
from django.conf import settings
from django.utils.module_loading import import_string


#
# The remainder of this file deals with initial setup and config of the worker.
# The final step deals with the autodiscovery of Jobs and other Actors.
#

RATE_LIMITER_BACKEND = None

def select_encoder():
    encoder = getattr(settings, "DRAMATIQ_ENCODER", "dramatiq.encoder.JSONEncoder")
    return import_string(encoder)()

def load_middleware(path_or_obj, **kwargs):
    if isinstance(path_or_obj, str):
        return import_string(path_or_obj)(**kwargs)
    return path_or_obj


def setup():

    result_backend_settings = getattr(settings, "DRAMATIQ_RESULT_BACKEND", {})
    if result_backend_settings:
        result_backend_path = result_backend_settings.get("BACKEND", "dramatiq.results.backends.StubBackend")
        result_backend_class = import_string(result_backend_path)
        result_backend_options = result_backend_settings.get("BACKEND_OPTIONS", {})
        result_backend = result_backend_class(**result_backend_options)

        results_middleware_options = result_backend_settings.get("MIDDLEWARE_OPTIONS", {})
        results_middleware = dramatiq.results.Results(backend=result_backend, **results_middleware_options)
    else:
        result_backend = None
        results_middleware = None

    rate_limiter_backend_settings = getattr(settings, "DRAMATIQ_RATE_LIMITER_BACKEND", {})
    if rate_limiter_backend_settings:
        rate_limiter_backend_path = rate_limiter_backend_settings.get(
            "BACKEND", "dramatiq.rate_limits.backends.stub.StubBackend"
        )
        rate_limiter_backend_class = import_string(rate_limiter_backend_path)
        rate_limiter_backend_options = rate_limiter_backend_settings.get("BACKEND_OPTIONS", {})
        RATE_LIMITER_BACKEND = rate_limiter_backend_class(**rate_limiter_backend_options)

    broker_settings = getattr(settings, "DRAMATIQ_BROKER", {})
    broker_path = broker_settings["BROKER"]
    broker_class = import_string(broker_path)
    broker_options = broker_settings.get("OPTIONS", {})
    middleware = [
        load_middleware(path)
        for path in broker_settings.get("MIDDLEWARE", [])
    ]

    if result_backend is not None:
        middleware.append(results_middleware)

    broker = broker_class(middleware=middleware, **broker_options)
    dramatiq.set_broker(broker)

    return broker
