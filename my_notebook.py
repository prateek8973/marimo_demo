import marimo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Initialize the Marimo app
# ---------------------------
app = marimo.App(width="medium")  # The main app object

# ---------------------------
# 1. Create synthetic dataset
# ---------------------------
def create_dataset():
    """
    Create a simple synthetic dataset for linear regression demonstration.
    Returns:
        df (DataFrame): Contains columns 'x' and 'y'
    """
    np.random.seed(42)
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 50),
        "y": np.linspace(0, 10, 50) * 2 + np.random.normal(0, 2, 50)
    })
    return df

# Make it a Marimo cell
@app.cell
def dataset_cell():
    df = create_dataset()
    return df  # Will be used by plotting cell

# ---------------------------
# 2. Slope slider
# ---------------------------
def create_slope_slider():
    """
    Create a Marimo slider widget for adjusting the slope.
    Returns:
        slope_slider: Marimo slider object
    """
    import marimo as mo
    slope_slider = mo.ui.slider(
        start=0.5, stop=3.0, step=0.1, value=2.0, label="Slope"
    )
    return slope_slider

@app.cell
def slope_slider_cell():
    slider = create_slope_slider()
    return slider  # Will be used by plotting and summary cells

# ---------------------------
# 3. Plotting function
# ---------------------------
def plot_data_with_slope(df, slope):
    """
    Plot the data and overlay a line with the given slope.
    Args:
        df (DataFrame): Dataset with 'x' and 'y'
        slope (float): Slope of the red line
    """
    plt.figure(figsize=(6,4))
    plt.scatter(df["x"], df["y"], label="Data")
    plt.plot(df["x"], slope * df["x"], color="red", label=f"y = {slope}x")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

@app.cell
def plot_cell(df, slope_slider):
    slope = slope_slider.value
    plot_data_with_slope(df, slope)
    return slope  # Return slope for summary cell

# ---------------------------
# 4. Markdown summary
# ---------------------------
def show_analysis_summary(slope):
    """
    Display a markdown summary showing the effect of the slope.
    """
    import marimo as mo
    mo.md(f"""
    ### Analysis Summary  
    The current slope is **{slope:.2f}**.  
    Increasing the slope makes the red line steeper, while decreasing it flattens the line.  
    This demonstrates the effect of the slope parameter on a simple linear model.
    """)

@app.cell
def summary_cell(plot_cell_output):
    slope = plot_cell_output
    show_analysis_summary(slope)

# ---------------------------
# 5. Run the app
# ---------------------------
if __name__ == "__main__":
    app.run()
