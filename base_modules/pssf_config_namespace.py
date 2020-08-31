"""Load configuration with exec"""
from types import SimpleNamespace


def load_config(path):
    """"
    Load configuration from path

    https://docs.python.org/3/library/types.html#types.SimpleNamespace
    https://docs.python.org/3/library/functions.html#exec

    """
    with open(path) as fp:
        data = fp.read()
    ns = {}
    exec(data, {}, ns)
    return SimpleNamespace(**ns)


if __name__ == "__main__":
    config = load_config("pssf_config.py")
    print(config)
