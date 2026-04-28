#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="ansingh-apps"

if kubectl get namespace "$NAMESPACE" &>/dev/null; then
  echo "Namespace '$NAMESPACE' already exists."
else
  kubectl create namespace "$NAMESPACE"
  echo "Namespace '$NAMESPACE' created."
fi
