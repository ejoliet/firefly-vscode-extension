#!/bin/bash
source /Users/ejoliet/dev/firefly-vscode-extension/firefly_demo/.venv/bin/activate
python /Users/ejoliet/dev/firefly-vscode-extension/firefly_demo/dnd_firefly.py "$1"
deactivate
