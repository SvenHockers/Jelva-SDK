import pluggy
import importlib.util
import pathlib
import sys

hookspec = pluggy.HookspecMarker("jelva")
hookimpl = pluggy.HookimplMarker("jelva")

class PluginSpec:
    """Plugin specification for strategies and connectors."""
    @hookspec
    def register_strategy(self, strategy: object) -> None:
        """Register a trading strategy."""
        pass

    @hookspec
    def register_connector(self, connector: object) -> None:
        """Register a data or broker connector."""
        pass

def load_from_directory(path: str) -> pluggy.PluginManager:
    """Dynamically load all .py files in a directory as pluggy plugins."""
    pm = pluggy.PluginManager("jelva")
    pm.add_hookspecs(PluginSpec)
    path_obj = pathlib.Path(path)
    for py_file in path_obj.glob("*.py"):
        spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[py_file.stem] = mod
        spec.loader.exec_module(mod)
        pm.register(mod)
    return pm

# Backend runner stub
# TODO: On backend, fetch ZIP, unzip to /tmp/strategy, call load_from_directory('/tmp/strategy'), then pm.hook.run_strategy(input_data=...)
