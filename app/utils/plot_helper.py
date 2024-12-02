import matplotlib.pyplot as plt

def plot_data(data, x_column, y_column, plot_type="line", title=None, xlabel=None, ylabel=None, figsize=(15, 4)):
    """
    Generates a plot of the data with customizable options.
    Args:
        data (pd.DataFrame): The data to plot.
        x_column (str): Column name for the x-axis.
        y_column (str): Column name for the y-axis.
        plot_type (str): Type of plot to generate ('line', 'scatter', 'bar').
        title (str, optional): Title of the plot. Defaults to None.
        xlabel (str, optional): Label for the x-axis. Defaults to None.
        ylabel (str, optional): Label for the y-axis. Defaults to None.
    Returns:
        matplotlib.figure.Figure: The generated plot figure.
    """
    try:
        # Validate input columns
        if x_column not in data.columns or y_column not in data.columns:
            raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the data.")
        
        # Create the plot
        fig, ax = plt.subplots(figsize=figsize)
        
        if plot_type == "line":
            ax.plot(data[x_column], data[y_column], marker='o', linestyle='-', markersize=4)
        elif plot_type == "scatter":
            ax.scatter(data[x_column], data[y_column])
        elif plot_type == "bar":
            ax.bar(data[x_column], data[y_column])
        else:
            raise ValueError(f"Unsupported plot type: '{plot_type}'. Use 'line', 'scatter', or 'bar'.")
        
        # Customize labels and title
        ax.set_xlabel(xlabel if xlabel else x_column)
        ax.set_ylabel(ylabel if ylabel else y_column)
        ax.set_title(title if title else f"{y_column} vs {x_column}")
        ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

        # Set transparent background
        fig.patch.set_alpha(0.0)  # Make the figure's background transparent
        ax.set_facecolor((0, 0, 0, 0))  # Make the axes' background transparent (RGBA)


        # Show the plot
        plt.show()
        
        return fig
    except Exception as e:
        print(f"Error plotting data: {e}")
        return None
