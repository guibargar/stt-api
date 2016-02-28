#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swedish_train_traffic_api.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
