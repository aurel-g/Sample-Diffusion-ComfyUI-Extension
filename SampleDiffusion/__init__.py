import os
import importlib

NODE_CLASS_MAPPINGS = {}

current_package = __name__

for node in os.listdir(os.path.dirname(__file__)):
    if node.startswith('EXT_'):
        node = node.split('.')[0]
        node_import = importlib.import_module(f"{current_package}.{node}")
        # get class node mappings from py file
        NODE_CLASS_MAPPINGS.update(node_import.NODE_CLASS_MAPPINGS)
