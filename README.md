# Data pipeline mit Kafka, PostgreSQL und PowerBI

Das Projekt simuliert eine Datenpipeline eines einfachen Onlineshops. 
Es werden Batch-Beispieldaten von einer API per python-Skript und Streaming-Beispieldaten über Kafka in eine PostgreSQL Datenbank transportiert und dann in PowerBI visualisiert.

Für Kafka- und PostgreSQL-Instanzen wurden Docker-Container verwendet. Ein Airflow DAG orchestriert die Dateningestion.

Unit-Tests und Linting wurden mithilfe von pytest in GitHub Actions umgesetzt um Continuous Integration sicherzustellen.