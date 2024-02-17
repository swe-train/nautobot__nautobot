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

        # Enforce that the core broker loader is already sent as the first argument
        sys.argv.insert(1, "nautobot.core.dramatiq")

        sys.exit(dramatiq_main())
