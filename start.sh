#!/bin/bash
set -e

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║     Tablón de Anuncios — arranque K8s    ║"
echo "╚══════════════════════════════════════════╝"

echo ""
echo "▶ [1/4] Construyendo y pusheando imágenes..."
bash imagesEnRegistry.sh

echo ""
echo "▶ [2/4] Creando clúster kind..."
bash createCluster.sh

echo ""
echo "▶ [3/4] Aplicando manifiestos..."
kubectl apply -f k8s/

echo ""
echo "▶ [4/4] Esperando a que los pods estén listos..."
kubectl wait --for=condition=ready pod --all --timeout=120s

echo ""
kubectl get pods

echo ""
echo "✅ ¡Todo listo!"
echo ""
kubectl port-forward service/nginx 8080:80
