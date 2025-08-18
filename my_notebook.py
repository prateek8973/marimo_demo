# ----------------
# install
# ----------------
import marimo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Initialize the Marimo app
# 22f3000812@ds.study.iitm.ac.in
# ---------------------------
# This is the main app object that will be passed to the last cell to run the app.
app = marimo.App(width="medium")

# ----------------------------------------
# Cell 1: Create synthetic dataset (df)
# ----------------------------------------
# This cell outputs `df`, which will be consumed by the plotting cell.
@app.cell
def dataset_cell():
    np.random.seed(42)
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 50),
        "y": np.linspace(0, 10, 50) * 2 + np.random.normal(0, 2, 50)
    })
    return df

# ----------------------------------------
# Cell 2: Create slope slider
# ----------------------------------------
# This cell outputs `slope_slider`, which will be consumed by the plotting cell.
@app.cell
def slope_slider_cell():
    import marimo as mo
    slope_slider = mo.ui.slider(
        start=0.5, stop=3.0, step=0.1, value=2.0, label="Slope"
    )
    return slope_slider

# ----------------------------------------
# Cell 3: Plot data and line
# ----------------------------------------
# This cell consumes `df` and `slope_slider`.
# It produces `slope` as output for the summary cell.
@app.cell
def plot_cell(df, slope_slider):
    slope = slope_slider.value
    plt.figure(figsize=(6,4))
    plt.scatter(df["x"], df["y"], label="Data")
    plt.plot(df["x"], slope * df["x"], color="red", label=f"y = {slope}x")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()
    return slope  # This value will be used by the summary cell

# ----------------------------------------
# Cell 4: Markdown summary
# ----------------------------------------
# This cell consumes `slope` from the plotting cell.
# It does not produce further output.
@app.cell
def summary_cell(plot_cell_output):
    import marimo as mo
    slope = plot_cell_output
    mo.md(f"""
    ### Analysis Summary  
    The current slope is **{slope:.2f}**.  
    Increasing the slope makes the red line steeper, while decreasing it flattens the line.  
    This demonstrates the effect of the slope parameter on a simple linear model.
    """)

# ----------------------------------------
# Cell 5: Run the app
# ----------------------------------------
# This cell consumes the `app` object initialized at the top.
# It is responsible for launching the Marimo interface.
if __name__ == "__main__":
    app.run()
