from unittest import TestCase
from .models import Entity


class NodeTestCase(TestCase):
    def test_create_root_node(self):
        node = Entity.objects.create(name='Movetech')
        self.assertEqual(node.name, 'Movetech')
        self.assertIsNone(node.parent)

    def test_create_hierarchy(self):
        parent = 'Deakin'
        children = ('Mathematics', 'Science', 'Accounting')
        root = Entity.objects.create(name=parent)
        for name in children:
            root = Entity.objects.create(name=name, parent=root)

        self.assertEqual(Entity.objects.count(), 4)
        self.assertEqual(root.ancestors.count(), 4)
