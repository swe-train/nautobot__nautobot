#
# This file is the entrypoint module for Nautobot dramatiq workers
# As such, it is not intended to be imported directly by any other components
#

import django
import nautobot
from nautobot.core.dramatiq import setup as dramatiq_setup

#
# Run setup of Nautobot because this is the entrypoint for worker processes
#
nautobot.setup()
django.setup()
#dramatiq_setup()


# Only after setup has occured, we can discover and import all actors (jobs)
from nautobot.core.dramatiq.discovery import import_jobs_from_apps
import_jobs_from_apps()
