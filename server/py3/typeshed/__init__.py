import os

try:
    import pkg_resources
except ImportError:
    typeshed = os.path.dirname(__file__)
else:
    typeshed = pkg_resources.resource_filename('typeshed', '')
