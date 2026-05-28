"""Student-owned dataset loading contract.

Students must implement ``load_dataset_split`` so that ``scripts/main.py`` can
evaluate every configured model on the same test split.
"""

from __future__ import annotations

from typing import Any
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATA_DIR  # Importation de la variable de dossier définie dans ton config.py


def load_dataset_split() -> tuple[Any, Any, Any, Any]:
    """Return the dataset split used for model evaluation.

    Expected return value:
        A tuple ``(X_train, X_test, y_train, y_test)``.
    """
    
    # 1. Chargement de ton fichier de ventes/stocks (ajuste le nom si nécessaire)
    # Le fichier doit se trouver dans ton dossier 'data/'
    df = pd.read_csv(DATA_DIR / "olist_ready_stocks.csv")
    
    # 2. Définition des colonnes de ton modèle Random Forest
    features = ['sales_lag_1', 'sales_lag_2', 'sales_moving_avg_4', 'month']
    target = 'weekly_sales_volume'
    
    X = df[features]
    y = df[target]
    
    # 3. Séparation Train / Test conforme (80% Train, 20% Test)
    # On fixe le random_state=42 pour que le découpage soit identique à ton notebook
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    return X_train, X_test, y_train, y_test