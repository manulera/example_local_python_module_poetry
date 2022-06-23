# Using a local module in a poetry project

This is a minimal example that shows how to install a local module in a poetry project.

Instructions:

* Start your poetry project:
  * Add `poetry.toml` so that environment installs locally (see content).
  * `poetry init` to initialize the project
  * `poetry install` to install the environment

* Create a folder with your module (here named `mymodule`). In there:
  * Add a `setup.py`. You can add more information, but this minimal version is sufficient.
  * Create a subdirectory with the same name (`mymodule`). In there:
    * Add an empty `__init__.py` file
    * Add the scripts with your code (here `functions.py`)

Then, `poetry install mymodule`.

Now you can use it from any folder, and whenever someone downloads the repo, it will be installed when they call `poetry install`.

External ref: https://python-packaging.readthedocs.io/en/latest/minimal.html