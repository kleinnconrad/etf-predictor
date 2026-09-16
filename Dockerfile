# Offizielles, schlankes Python-Image
FROM python:3.12-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# System-Abhängigkeiten installieren (für Machine Learning Bibliotheken oft nötig)
RUN apt-get update && apt-get install -y build-essential curl && rm -rf /var/lib/apt/lists/*

# Abhängigkeiten kopieren und installieren
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-install-project

# Deinen kompletten Code in den Container kopieren
COPY . .
RUN uv sync --frozen

# Port für Streamlit freigeben
EXPOSE 8501

# Startbefehl für die Streamlit App
CMD ["uv", "run", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]