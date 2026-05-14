#!/usr/bin/env bash

set -euo pipefail

python3 scripts/build_site.py
python3 -m http.server 4173
