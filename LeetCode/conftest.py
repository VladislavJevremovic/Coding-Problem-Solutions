import os
import sys

# Solution files import shared utilities as `from python.Helpers...`, which
# requires the LeetCode/ directory (this file's directory) to be importable.
# importlib mode does not add conftest directories to sys.path automatically,
# so do it explicitly here.
sys.path.insert(0, os.path.dirname(__file__))
