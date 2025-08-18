import marimo

# Store the Marimo version used for generating this notebook
__generated_with = "0.14.17"

# Initialize a Marimo app with medium width layout
app = marimo.App(width="medium")


@app.cell
def _():
    # This cell seems redundant as it initializes another app
    # Possibly leftover from previous version
    import marimo

    __generated_with = "0.1.82"
    app = marimo.App()

    # Return the app object (though it is not used here)
    return (app,)


@app.cell
def _():
    # Empty cell placeholder
    return


## DataFrame creation
@app.cell
def _():
    import numpy as np
    import pandas as pd

    # Create a random dataset for linear regression demonstration
    np.random.seed(42)  # For reproducibility
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 50),  # X values from 0 to 10
        "y": np.linspace(0, 10, 50) * 2 + np.random.normal(0, 2, 50)  # Y = 2x + noise
    })

    # Display the dataframe
    df
    return (df,)


@app.cell
def _():
    # Empty cell placeholder
    return


@app.cell
def _():
    import marimo as mo

    # Create a slider for adjusting the slope in the plot
    slope_slider = mo.ui.slider(
        start=0.5, stop=3.0, step=0.1, value=2.0, label="Slope"
    )
    # Display the slider
    slope_slider
    return (slope_slider,)


@app.cell
def _():
    # Empty cell placeholder
    return


# Plotting cell
@app.cell
def _(df, slope_slider):
    import matplotlib.pyplot as plt

    # Get the current slope value from the slider
    slope = slope_slider.value

    # Create a scatter plot of the data
    plt.figure(figsize=(6,4))
    plt.scatter(df["x"], df["y"], label="Data")

    # Plot a line with the current slope
    plt.plot(df["x"], slope * df["x"], color="red", label=f"y = {slope}x")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

    return


@app.cell
def _():
    # Empty cell placeholder
    return


# Markdown summary cell
@app.cell
def _():
    def _(slope):
        import marimo as mo

        # Display analysis summary in markdown format
        mo.md(f"""
        ### Analysis Summary  
        The current slope is **{slope:.2f}**.  
        Increasing the slope makes the red line steeper, while decreasing it flattens the line.  
        This demonstrates the effect of the slope parameter on a simple linear model.
        """)
        return 
    return


@app.cell
def _(app):
    # Run the app when executed as the main script
    if __name__ == "__main__":
        app.run()

    return


@app.cell
def _():
    # Empty cell placeholder
    return


# Final run command if script is executed directly
if __name__ == "__main__":
    app.run()
