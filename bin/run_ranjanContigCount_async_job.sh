#!/bin/bash
script_dir=$(dirname "$(readlink -f "$0")")
export PYTHONPATH=$script_dir/../lib:$PATH:$PYTHONPATH
python $script_dir/../lib/ranjanContigCount/ranjanContigCountServer.py $1 $2 $3
