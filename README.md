---
title: Meu Projeto IA
emoji: 🚀
colorFrom: blue
colorTo: gray
sdk: streamlit
python_version: 3.11
app_file: app.py
pinned: false
---

# 🎯 Marketing-Interessengruppen Vorhersage (K-Means)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://csv-extractor-ai-080526.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-orange.svg)
![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-8A2BE2.svg)

Interaktive **Streamlit**-Webanwendung, die **Machine Learning (K-Means Clustering)** nutzt, um Nutzer in Interessengruppen zu segmentieren. Ziel ist es, Marketingkampagnen durch eine präzise Zielgruppenansprache effektiver zu gestalten.

---

## 🌐 Live Demo

👉 **[https://csv-extractor-ai-080526.streamlit.app/](https://csv-extractor-ai-080526.streamlit.app/)**

Die App ist live auf **Streamlit Community Cloud** gehostet. Einfach im Browser öffnen, eine CSV-Datei hochladen und die vorhergesagten Interessengruppen visualisieren.

> 💡 **Dies war mein erstes Projekt, das mit [Claude Code](https://claude.com/claude-code) realisiert wurde.** Eine wirklich interessante und sehr praktische Erfahrung — von der Optimierung des Codes mit Schema-Validierung über die Generierung von Testdaten bis hin zum Deployment auf GitHub verlief alles flüssig und kollaborativ.

---

## 🚀 Funktionen

* **Interaktive Streamlit-Oberfläche**: CSV-Upload und Echtzeit-Visualisierung der Ergebnisse.
* **Automatische CSV-Validierung**: prüft Spalten, kategoriale Werte und numerische Typen vor der Verarbeitung.
* **Integrierte Vorverarbeitung**: `OneHotEncoder` für die Spalte `sexo` und `MinMaxScaler` für die numerischen Attribute.
* **Vorhersage in 3 Gruppen** mittels vortrainiertem K-Means-Modell (`kmeans.pkl`).
* **Automatische Spaltenumsortierung**, damit das Schema des Scalers eingehalten wird.
* **Vorlage zum Download** mit den 27 erwarteten Spalten.
* **Verteilungsdiagramm** der identifizierten Cluster.
* **CSV-Export** der Ergebnisse mit hinzugefügter Spalte `Gruppen`.
* **Vollständig auf Deutsch lokalisierte Oberfläche.**

---

## 🛠️ Technologie-Stack

| Komponente | Technologie | Funktion |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interaktive Web-Oberfläche |
| **Datenanalyse** | Pandas | Datenmanipulation und -bereinigung |
| **ML-Algorithmus** | Scikit-Learn (K-Means) | Clustering und Segmentierung |
| **Vorverarbeitung** | OneHotEncoder + MinMaxScaler | Kategoriale Kodierung und Skalierung |
| **Modellpersistenz** | Joblib | Laden der `.pkl`-Dateien |
| **KI-gestützte Entwicklung** | Claude Code | Code-Optimierung und -Generierung |

---

## 📋 Voraussetzungen

- Python 3.11+
- Pip

## ⚙️ Installation

```bash
git clone https://github.com/RuanaRamos/CSV-Extractor-AI.git
cd CSV-Extractor-AI
pip install -r requirements.txt
```

## ▶️ Ausführen

```bash
streamlit run app.py
```

Die Anwendung öffnet sich im Browser unter `http://localhost:8501`.

---

## 📂 Projektstruktur

```
.
├── app.py                    # Streamlit-Anwendung
├── requirements.txt          # Abhängigkeiten
├── encoder.pkl               # Trainierter OneHotEncoder
├── scaler.pkl                # Trainierter MinMaxScaler
├── kmeans.pkl                # Trainiertes K-Means-Modell (3 Cluster)
├── exemplo_interesses.csv    # Beispiel-CSV (200 Zeilen) zum Testen
├── generate_csv.py           # Skript zur Generierung neuer Beispiel-CSVs
└── README.md
```

---

## 📊 Schema der Eingabe-CSV

Die CSV muss **27 Spalten** enthalten: `sexo` (kategorial: `F`, `M`, `NE`) und 26 numerische Spalten:

`idade`, `numero_de_amigos`, `basquete`, `futebol_americano`, `futebol`, `softbol`, `voleibol`, `natacao`, `animacao`, `beisebol`, `tenis`, `esportes`, `fofo`, `danca`, `banda`, `marcha`, `musica`, `rock`, `cabelo`, `vestido`, `shopping`, `compras`, `roupas`, `nossa_marca`, `marca_concorrente`, `bebidas`

> Nutzen Sie den Button **„⬇️ Vorlage herunterladen"** in der Seitenleiste der App, um eine fertige Vorlage zu erhalten.

---

## 🎨 Beschreibung der Gruppen

| Gruppe | Beschreibung |
| :--- | :--- |
| **Gruppe 0** | Junges Publikum mit starkem Interesse an Mode, Musik und Aussehen. |
| **Gruppe 1** | Stark assoziiert mit Sport (American Football, Basketball) und kulturellen Aktivitäten wie Band und Rockmusik. |
| **Gruppe 2** | Ausgewogen, mit Interessen an Musik, Tanz und Mode. |

---

## 🤖 Über die Entwicklung mit Claude Code

Dieses Projekt wurde mit **Claude Code**, dem offiziellen CLI-Tool von Anthropic für KI-gestützte Entwicklung, optimiert und refaktoriert. In einer einzigen Sitzung war es möglich:

- 🔍 Die `.pkl`-Modelle zu inspizieren, um das erwartete Schema zu ermitteln
- ✨ Die `app.py` mit Validierung, Caching und Fehlerbehandlung zu refaktorieren
- 📝 Eine gültige Beispiel-CSV zu generieren, die mit der Pipeline kompatibel ist
- 🧪 Die Pipeline End-to-End zu testen
- 🚀 Das Git-Repository einzurichten und auf GitHub zu deployen

Die Erfahrung war **wirklich interessant und sehr praktisch** — eine flüssige und kollaborative Art, das Projekt zu entwickeln, zu debuggen und zu dokumentieren.

---

## 👤 Autorin

**Ruana Ramos** — [@RuanaRamos](https://github.com/RuanaRamos)
