# Base stage for both dev and production
FROM python:3.10-alpine AS base

ENV PYTHONPATH="/app/"
ENV MONGO_ATLAS_URI="mongodb://localhost:27017"

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Install dependencies before copying code (caching optimization)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Development stage
FROM base AS development

# Set environment for development
ENV FLASK_ENV=development

# Copy source code for development
COPY . /app/

# Expose Flask port
EXPOSE 5000

# Run Flask in development mode (hot-reloading)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Production stage
FROM base AS production

# Set environment for production
ENV FLASK_ENV=production

# Copy source code for production (without .env, dev files, etc.)
COPY . /app/

# Expose Flask port
EXPOSE 5000

# Run the app in production mode
CMD ["python", "./app.py"]