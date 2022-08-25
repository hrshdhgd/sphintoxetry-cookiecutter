"""Code to run before generating the project."""

import re
import sys

MODULE_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

project_name = '{{ cookiecutter.project_name}}'

if not MODULE_REGEX.match(project_name):
    print(
        f'ERROR: {project_name} is not a valid Python module name. Please do not use a - and use _ instead'
    )

    # Exit to cancel project
    sys.exit(1)