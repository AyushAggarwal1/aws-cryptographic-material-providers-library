# __init__.py for a Smithy-Dafny generated Python project

# TODO-Python: Remove PYTHONPATH workaround, use fully-qualified module names via dfyproject.toml.
# Import project dependencies.
# TODO-Python-PYTHONPATH: Remove dependency imports to initialize PYTHONPATH with their modules

from . import internaldafny
import aws_cryptographic_materialproviders

# Add internaldafny code to PYTHONPATH (TODO-Python-PYTHONPATH: Remove)
import sys

module_root_dir = '/'.join(__file__.split("/")[:-1])

sys.path.append(module_root_dir + "/internaldafny/extern")
sys.path.append(module_root_dir + "/internaldafny/generated")