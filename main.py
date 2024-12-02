import streamlit.web.cli as stcli
import sys
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

def main():
    """
    Entry point for running the Streamlit application.
    """

    app_path = './app/streamlit_app.py'

    # Adjust sys.argv to mimic the command-line input for Streamlit
    sys.argv = ["streamlit", "run", app_path]

    # Start Streamlit server
    stcli.main()


if __name__ == "__main__":
    main()


    "test"