FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY ./src ./src

# Expose port
EXPOSE 8001

# Start app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
