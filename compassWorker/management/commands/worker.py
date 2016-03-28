from channels import Group
from django.core.management import BaseCommand
import time

#The class must be named Command, and subclass BaseCommand

class Command(BaseCommand):
    # Show this when the user types help
    help = "Compass Worker"
    
    # A command must define handle()
    def handle(self, *args, **options):
        x = 0
        while True:
            Group("compass").send({'text': "Yeah working..." + str(x)})
            time.sleep(2)
            x = x + 1
            self.stdout.write("Yeah working..." + str(x))
