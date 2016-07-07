#!/bin/bash

pkill -f "run_will.py"
sleep 1
export TEMPLATE_DIRS = []
./run_will.py 

