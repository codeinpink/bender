#!/bin/bash

pkill -f "run_will.py"
sleep 1
unset WILL_TEMPLATE_DIRS_PICKLED
./run_will.py
