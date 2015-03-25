# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Initialise 'blog' application"

    def handle(self, *args, **options):
        print("Initialised 'blog' app...")
