#!/bin/bash
printenv
pkill -f "run_will.py"
sleep 1
printenv
export TEMPLATE_DIRS=[]
./run_will.py 

