"""Module for generating plots specific to this poster."""

import matplotlib.pyplot as plt
import volcano_cooking.helper_scripts.view_generated_forcing as view

def get_plt() -> plt.Figure:
    """Return a figure object."""
    _PATH = "/home/een023/Documents/work/cesm/model-runs/e_BASELINE/synthetic/volcan-eesm_global_2015_so2-emissions-database_v1.0.nc"
    f = view.view_forcing(in_file=_PATH, width=1, style="bars", return_fig=True)
    if f is not None:
        return f
    else:
        raise ValueError("Could not generate figure.")
