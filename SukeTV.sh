#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 SukeTV.py > ../SukeTV.ts

echo m3u grabbed
