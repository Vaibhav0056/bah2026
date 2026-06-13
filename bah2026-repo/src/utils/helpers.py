"""
helpers.py — Common utility functions for the project.
Add reusable functions here so teammates don't rewrite the same code.
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def get_project_root() -> str:
    """Returns the absolute path to the project root directory."""
    # Go up from src/utils/ → src/ → project root
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


def data_path(filename: str, split: str = "raw") -> str:
    """
    Returns the full path to a file in the data directory.

    Args:
        filename: Name of the file (e.g., 'dataset.csv')
        split: Subfolder — 'raw', 'processed', or 'sample'

    Example:
        path = data_path('my_data.csv', split='raw')
    """
    return os.path.join(get_project_root(), "data", split, filename)


def save_figure(fig, filename: str, dpi: int = 150):
    """
    Saves a matplotlib figure to the outputs/visualizations/ folder.

    Args:
        fig: matplotlib Figure object
        filename: e.g., 'loss_curve.png'
        dpi: Resolution (default 150)
    """
    out_dir = os.path.join(get_project_root(), "outputs", "visualizations")
    os.makedirs(out_dir, exist_ok=True)
    fig.savefig(os.path.join(out_dir, filename), dpi=dpi, bbox_inches="tight")
    print(f"Figure saved → outputs/visualizations/{filename}")


def set_seed(seed: int = 42):
    """Set random seed for reproducibility."""
    import random
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
    except ImportError:
        pass
    print(f"Random seed set to {seed}")
