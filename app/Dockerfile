# VULNERABILIDAD INTENCIONADA 1: Usar una imagen base sin especificar un tag exacto o sha256
FROM python:3.9

WORKDIR /app

# VULNERABILIDAD INTENCIONADA 2: Copiar todo de golpe (podría incluir archivos sensibles)
COPY . /app

RUN pip install -r requirements.txt

# VULNERABILIDAD INTENCIONADA 3: No crear un usuario sin privilegios (se ejecuta como root)
EXPOSE 5000

CMD ["python", "app.py"]