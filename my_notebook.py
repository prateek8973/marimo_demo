import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    # 22f3000812@ds.study.iitm.ac.in

    import marimo

    __generated_with = "0.1.82"
    app = marimo.App()

    return (app,)


@app.cell
def _():
    return

## dataframe
@app.cell
def _():
    import numpy as np
    import pandas as pd

    # Create a random dataset
    np.random.seed(42)
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 50),
        "y": np.linspace(0, 10, 50) * 2 + np.random.normal(0, 2, 50)
    })
    df
    return (df,)


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    slope_slider = mo.ui.slider(start=0.5, stop=3.0, step=0.1, value=2.0, label="Slope")
    slope_slider
    return (slope_slider,)


@app.cell
def _():
    return


@app.cell
def _(df, slope_slider):
    import matplotlib.pyplot as plt

    slope = slope_slider.value
    plt.figure(figsize=(6,4))
    plt.scatter(df["x"], df["y"], label="Data")
    plt.plot(df["x"], slope * df["x"], color="red", label=f"y = {slope}x")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()
    return


@app.cell
def _():
    return


@app.cell
def _():
    def _(slope):
        import marimo as mo
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
    if __name__ == "__main__":
        app.run()

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
