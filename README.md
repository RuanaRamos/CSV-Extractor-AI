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

# Cluster-Prediction-App

# 🎯 Marketing-Interessengruppen Vorhersage (K-Means)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-orange.svg)

Diese interaktive Web-Anwendung nutzt **Machine Learning (K-Means Clustering)**, um Nutzer in spezifische Interessengruppen zu segmentieren. Ziel ist es, Marketingkampagnen durch präzise Zielgruppenansprache effektiver zu gestalten.

---

## 🚀 Funktionen

* **CSV-Daten-Upload**: Laden Sie Ihre Kundendaten direkt im CSV-Format hoch.
* **Automatisierte Vorhersage**: Das Modell klassifiziert jeden Nutzer automatisch in vordefinierte Cluster.
* **Daten-Vorverarbeitung**: Integrierte Skalierung (**StandardScaler**) und Kategorien-Kodierung (**OneHotEncoder**).
* **Ergebnis-Export**: Laden Sie die segmentierte Liste als neue CSV-Datei für Ihr Marketing-Tool herunter.
* **Mehrsprachige Oberfläche**: Komplett auf Deutsch optimiert.

---

## 🛠️ Technologie-Stack

| Komponente | Technologie | Funktion |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interaktive Web-Oberfläche |
| **Datenanalyse** | Pandas | Datenmanipulation und -reinigung |
| **ML-Algorithmus** | Scikit-Learn (K-Means) | Clustering und Segmentierung |
| **Modellspeicherung** | Joblib | Laden der trainierten `.pkl` Dateien |

---

## 📋 Voraussetzungen & Installation

Stellen Sie sicher, dass Sie Python installiert haben.

1. **Repository klonen**:
   ```bash
   git clone [https://github.com/SEU-USUARIO/cluster-prediction-app.git](https://github.com/SEU-USUARIO/cluster-prediction-app.git)
   cd cluster-prediction-app
