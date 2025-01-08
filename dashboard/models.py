from unicodedata import category
from django.db import models

# Create your models here.
CATEGORY = (
    ('Batteries', 'Batteries'),
    ('Battery Casing & Holder', 'Battery Casing & Holder'),
    ('Battery Charger/Modules', 'Battery Charger/Modules'),
    ('DC/DC Converter', 'DC/DC Converter'),
    ('Capacitors', 'Capacitors'),
    ('Development Boards', 'Development Boards'),
    ('Diodes', 'Diodes'),
    ('Displays', 'Displays'),
    ('Fan', 'Fan'),
    ('IC (Digital/Logic)', 'IC (Digital/Logic)'),
    ('IC (Other)', 'IC (Other)'),
    ('Inductors', 'Inductors'),
    ('LEDs', 'LEDs'),
    ('Machining Bolts / Screws / Kits', 'Machining Bolts / Screws / Kits'),
    ('Misc.', 'Misc.'),
    ('Motors', 'Motors'),
    ('Optocoupler', 'Optocoupler'),
    ('Potentiometers', 'Potentiometers'),
    ('Power Supply', 'Power Supply'),
    ('Pumps', 'Pumps'),
    ('Relays', 'Relays'),
    ('Remotes', 'Remotes'),
    ('Resistors', 'Resistors'),
    ('Sensors', 'Sensors'),
    ('Speaker / Buzzer', 'Speaker / Buzzer'),
    ('Switches', 'Switches'),
    ('Transistors', 'Transistors'),
    ('Wireless RF/BT', 'Wireless RF/BT'),
    
)

PACKAGE = (
    ('Through Hole', 'Through Hole'),
    ('Surface Mount', 'Surface Mount'),
    ('Other', 'Other'),
)

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    package = models.CharField(max_length=20, choices=PACKAGE, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.package} | {self.name} | #{ self.quantity} | {self.location}'