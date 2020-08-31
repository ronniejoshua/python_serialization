"""Load configuration with importlib"""
from importlib.machinery import SourceFileLoader


def load_config(path):
    """"
    Load configuration from path
    https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader
    """
    return SourceFileLoader('config', path).load_module()


if __name__ == "__main__":
    config = load_config("pssf_config.py")
    print(config)
    print(config.num_workers)
