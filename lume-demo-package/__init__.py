from lume-demo-package.files import VARIABLE_FILE
from lume_model.utils import variables_from_yaml

with open(VARIABLE_FILE, "r") as f:
    INPUT_VARIABLES, OUTPUT_VARIABLES = variables_from_yaml(f)

from . import _version
__version__ = _version.get_versions()['version']
