# Structure d’un projet pré-configuré pour tests API + UI + ETL

project_root/
├── etl/
│   ├── extract.py            # fonctions pour récupérer les données (fichier, API, etc.)
│   ├── transform.py          # nettoyage, validation, enrichissement
│   └── load.py               # insertion dans base ou export fichiers
│
├── api/
│   ├── app.py                # API Flask ou FastAPI exposant les fonctions ETL
│   ├── routes/
│   │   └── etl_routes.py     # endpoints REST
│   └── tests/
│       └── test_api.py       # tests des routes API avec httpx ou requests
│
├── ui/
│   ├── gui.py                # interface PySide6 avec affichage / bouton
│   └── tests/
│       └── test_gui.py       # tests avec pytest-qt
│
├── tests/
│   ├── test_etl.py           # tests unitaires sur ETL
│   ├── test_data_valid.py    # tests avec great_expectations ou pandera
│   └── test_all.sh           # script bash global
│
├── requirements.txt
├── conftest.py               # fixtures pytest
└── pytest.ini                # config globale pytest

# Exemple : test_api.py
import requests

def test_etl_trigger():
    response = requests.post("http://localhost:8000/etl/run")
    assert response.status_code == 200

# Exemple : test_gui.py avec pytest-qt
from ui.gui import MainWindow

def test_window_starts_up(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    assert window.isVisible()

# Exemple : test_data_valid.py avec great_expectations
import great_expectations as ge

def test_column_ranges():
    df = ge.from_pandas(load_some_data())
    df.expect_column_values_to_be_between("age", 0, 120)
