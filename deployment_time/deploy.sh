#!/bin/sh

echo "Deploying model..."
oasees-sdk mlops deploy-model --project-name=example1 --model=example1_2025-12-11_12-02-22.pkl && kubectl wait --for=condition=ready pod -l app=example1-2025-12-11-12-02-22pkl --timeout=300s
echo "\nModel Deployed!. Sending for inference...\n"
python3 send_for_inference.py
