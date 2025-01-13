from unicodedata import category
from django.db import models

# Create your models here.
CATEGORY = (
    ('Batteries', 'Batteries'),
    ('Battery Casing & Holder', 'Battery Casing & Holder'),
    ('Battery Charger/Modules', 'Battery Charger/Modules'),
    ('Cables','Cables'),
    ('Capacitors', 'Capacitors'),
    ('Connectors','Connectors'),
    ('Consumables','Consumables'),
    ('DC/DC Converter', 'DC/DC Converter'),
    ('Development Boards', 'Development Boards'),
    ('Diodes', 'Diodes'),
    ('Displays', 'Displays'),
    ('Fan', 'Fan'),
    ('Fuse','Fuse'),
    ('Hardware, Fasteners, Accessories','Hardware, Fasteners, Accessories'),
    ('IC (Digital/Logic)', 'IC (Digital/Logic)'),
    ('IC (Other)', 'IC (Other)'),
    ('Inductors', 'Inductors'),
    ('LEDs', 'LEDs'),
    ('Magnetics','Magnetics'),
    ('Misc.', 'Misc.'),
    ('Motors', 'Motors'),
    ('Optoelectronics','Optoelectronics'),
    ('Optocoupler/Optoisolator', 'Optocoupler/Optoisolator'),
    ('Potentiometers', 'Potentiometers'),
    ('Power Supply', 'Power Supply'),
    ('Pumps', 'Pumps'),
    ('Relays', 'Relays'),
    ('Remotes', 'Remotes'),
    ('Resistors', 'Resistors'),
    ('Sensors', 'Sensors'),
    ('Speaker / Buzzer', 'Speaker / Buzzer'),
    ('Switches', 'Switches'),
    ('Transformers','Transformers'),
    ('Transistors', 'Transistors'),
    ('Wire','Wire'),
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

class MarqueeText(models.Model):
    text = models.CharField(max_length=255, help_text="Text to display in the marquee")

    def __str__(self):
        return self.text

class CustomOrderItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.quantity})'
