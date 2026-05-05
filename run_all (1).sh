#!/usr/bin/env bash

set -e

mkdir -p data/raw data/processed results/figures logs

if [ ! -f "data/raw/state_crime.csv" ]; then
    echo "Missing data/raw/state_crime.csv"
    exit 1
fi

if [ ! -f "data/raw/Unemployment2023.csv" ]; then
    echo "Missing data/raw/Unemployment2023.csv"
    exit 1
fi

python clean_and_merge.py
python analyze.py
