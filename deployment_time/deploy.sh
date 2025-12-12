#!/bin/sh

echo "Deploying model..."
oasees-sdk mlops deploy-model --project-name=example1 --model=example1_2025-12-12_15-37-45.pkl && kubectl wait --for=condition=ready pod -l app=example1-2025-12-12-15-37-45pkl --timeout=300s
echo "\nModel Deployed!. Sending for inference...\n"
python3 send_for_inference.py
