"""Student-owned metrics contract.

Students must implement ``compute_metrics`` to return the evaluation metrics
that matter for their project.
"""

from __future__ import annotations

from typing import Any
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def compute_metrics(y_true: Any, y_pred: Any) -> dict[str, float]:
    """Return the metrics used to compare model performance.

    Expected return value:
        A dictionary mapping metric names to numeric values.
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    return {
        "MAE_stocks": float(mae),
        "RMSE_stocks": float(rmse),
        "R2_stocks": float(r2)
    }
    