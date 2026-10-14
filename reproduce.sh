#!/usr/bin/env bash
# Reproduction script for the G11 benchmark-audit paper.
#
# Re-verifies the paper's headline numbers from the shipped release file.
# Runs in seconds on any machine with Python 3 (no solver needed).
#
# Usage: bash reproduce.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py
