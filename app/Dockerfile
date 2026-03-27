# VULNERABILIDAD CORREGIDA: Se especifica tag exacto
FROM python:3.9-slim

# VULNERABILIDAD CORREGIDA (HIGH): Missing User Instruction
RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .

# VULNERABILIDAD CORREGIDA (LOW): pip install sin caché
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser /app

USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
