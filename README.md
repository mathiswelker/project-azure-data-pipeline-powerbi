# Data pipeline mit Spark, PostgreSQL und PowerBI

Dieses Projekt lädt Kundendaten per API, speichert sie in einer Postgres-Datenbank, verarbeitet sie mit Spark und bereitet sie für PowerBI-Analysen vor – alles in Docker-Containern organisiert.

Komponenten:
API: Stellt Endpunkte für Kunden, Produkte und Bestellungen bereit.
Postgres: Speichert die Rohdaten und die verarbeiteten Daten.
Spark: Liest Kundendaten aus Postgres, extrahiert Postleitzahlen, ergänzt Bundesland-Infos und schreibt die Ergebnisse zurück in die Datenbank.

Todo:
Streaming Daten mit kafka und spark implementieren,
CI mit pytest und GitHub Actions implementieren.
