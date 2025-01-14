from unicodedata import category
from django.db import models

# Create your models here.
CATEGORY = (
    ('Batteries', 'Batteries'),
    ('Cables','Cables'),
    ('Capacitors', 'Capacitors'),
    ('Connectors','Connectors'),
    ('Consumables','Consumables'),
    ('DC/DC Converter', 'DC/DC Converter'),
    ('Development Boards', 'Development Boards'),
    ('Diodes', 'Diodes'),
    ('Displays', 'Displays'),
    ('Equipment', 'Equipment'),
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
    link = models.URLField(max_length=500, null=True, blank=True)  # New field for item links

    def __str__(self):
        return f'{self.package} | {self.name} | #{ self.quantity} | {self.location}'

class MarqueeText(models.Model):
    text = models.CharField(max_length=255, help_text="Text to display in the marquee")

    def __str__(self):
        return self.text

class CustomOrderItem(models.Model):
    package = models.CharField(max_length=20, choices=PACKAGE, null=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.quantity})'


class EquipmentCheckout(models.Model):
    equipment = models.ForeignKey(Product, on_delete=models.CASCADE, limit_choices_to={'category': 'Equipment'})
    user = models.CharField(max_length=100)  # Name of the person checking out
    checked_out_at = models.DateTimeField(auto_now_add=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100)  # Location of the equipment

    def __str__(self):
        status = "Checked In" if self.checked_in_at else "Checked Out"
        return f'{self.equipment.name} - {status}'
