#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from decouple import config


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "em_system.settings")

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        os.environ.setdefault("DJANGO_CONFIGURATION", "Test")
    else:
        os.environ.setdefault(
            "DJANGO_CONFIGURATION",
            config("DJANGO_CONFIGURATION", default="Production"),
        )

    try:
        from configurations.management import (
            execute_from_command_line,
        )
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
