#!/usr/bin/env python3
import pytest
import sys

if __name__ == '__main__':
    pytest_args = sys.argv[1:]
    run_tests = True
    pytest.main(['tests'])
