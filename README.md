# Pipeline Project: API, PostgreSQL, Spark, Docker

## Overview
This project builds a pipeline with:
- A Flask API (Python)
- PostgreSQL database
- Spark transformation job
- All components are dockerized and orchestrated with Docker Compose

## Structure
- `api/` - Flask API service
- `postgres/` - Database init script
- `spark/` - Spark transformation job
- `docker/` - Docker Compose file

## Usage
1. Build and start all services:
   ```powershell
   cd docker
   docker-compose up --build
   ```
2. The API runs on port 5000, PostgreSQL on 5432.
3. Spark job connects to PostgreSQL and transforms data.

## Customization
- Replace example data and transformation logic as needed.
- Update Dockerfiles for additional dependencies.

## Notes
- Default credentials: user `postgres`, password `postgres`, db `postgres`.
- All code is for demonstration. Secure and optimize for production use.
