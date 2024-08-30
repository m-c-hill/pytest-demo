#!/bin/bash
export PYTHONPATH="${PYTHONPATH}:./src"
python -m pytest . --disable-warnings
