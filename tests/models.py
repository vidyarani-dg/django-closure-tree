from closure_tree.models import Node
from django.db import models


class Entity(Node):
    name = models.CharField(max_length=64)
