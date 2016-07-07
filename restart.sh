#!/bin/bash

pkill -f "run_will.py"
sleep 10
python ~/run_will.py &> /tmp/will.log 2> /tmp/will.err &

