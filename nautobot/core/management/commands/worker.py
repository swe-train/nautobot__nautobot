import sys

from dramatiq.cli import CPUS, folder_path, main as dramatiq_main
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Thin wrapper to the `dramatiq` command that includes the Nautobot dramatiq
    app context. This allows us to execute dramatiq commands without having to
    worry about the chicken-and-egg problem with bootstrapping the Django
    settings.
    """

    def run_from_argv(self, argv):
        sys.argv.remove("worker")

        # Enforce that the core worker entrypoint is used as the broker arg
        sys.argv.insert(1, "nautobot.core.dramatiq.worker")

        sys.exit(dramatiq_main())
