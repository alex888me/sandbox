import importlib.util

# absolute path to the module
module_path = "/absolute/path/to/your/module.py"

# create a module spec
spec = importlib.util.spec_from_file_location("module_name", module_path)

# create a module instance from the spec
module = importlib.util.module_from_spec(spec)

# execute the module
spec.loader.exec_module(module)

# now you can use the module
module.some_function()
