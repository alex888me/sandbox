import importlib.util
import sys

def load_config(path):
    spec = importlib.util.spec_from_file_location("config", path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_config>")
        sys.exit(1)

    config_path = sys.argv[1]
    config = load_config(config_path)

    if config.DEBUG_MODE:
        print("Debug mode is on.")

    # More code using your config data...
    # ...

if __name__ == "__main__":
    main()
