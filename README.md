# Tablón de Anuncios — Kubernetes

Aplicación web de tablón de anuncios migrada de Docker a Kubernetes con escalado automático.

## Repositorios
- **Docker:** https://github.com/Daritxe2/practica-docker
- **Kubernetes:** https://github.com/Daritxe2/practica-k8s

## Requisitos
- GitHub Codespaces
- Docker
- kind
- kubectl

## Arranque con un solo comando
```bash
./start.sh
```

El script automáticamente:
1. Construye y publica las imágenes en el registry local
2. Crea el clúster Kubernetes con kind
3. Instala y configura el metrics-server para el escalado
4. Aplica todos los manifiestos de K8s
5. Espera a que los pods estén listos

## Tiempo de inicio aproximado
- Primera ejecución: ~3-5 minutos
- Ejecuciones posteriores: ~1-2 minutos

## Verificar escalado

En un terminal ejecuta:
```bash
watch -n 2 'kubectl get pods,hpa'
```

En otro terminal genera carga:
```bash
kubectl run stress --image=busybox --restart=Never -it --rm \
  -- sh -c "while true; do wget -q -O- http://web:5000/; done"
```

El HPA escalará automáticamente entre 1 y 8 réplicas según el uso de CPU (umbral: 20%).

## Estructura del proyecto
```
├── app/                  # Aplicación Flask
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
├── nginx/                # Proxy inverso
│   ├── Dockerfile
│   └── default.conf
├── k8s/                  # Manifiestos Kubernetes
│   ├── web-deployment.yaml
│   ├── redis-deployment.yaml
│   ├── nginx-deployment.yaml
│   └── web-hpa.yaml
├── docker-compose.yml
├── start.sh
├── imagesEnRegistry.sh
└── createCluster.sh
```

## Acceso a la aplicación

Una vez arrancado, la aplicación es accesible en el **puerto 8080**.

En GitHub Codespaces, ve a la pestaña **PUERTOS** y abre el puerto **8080** en el navegador.

Si quieres hacer el port-forward manualmente:
```bash
kubectl port-forward service/nginx 8080:80
```
