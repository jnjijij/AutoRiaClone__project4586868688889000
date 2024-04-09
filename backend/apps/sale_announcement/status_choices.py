from django.db import models


class StatusChoices(models.TextChoices):
    Active = "active",
    Blocked = "blocked",
    NotActive = "notActive",
    Pending = "pending"
