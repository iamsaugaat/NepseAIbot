# NEPSE AI Trading Signal Bot

This project implements a simple AI trading signal bot for the NEPSE index using a Flask web application. The bot fetches stock data from Alpha Vantage, generates buy/sell signals based on moving average crossovers, and displays the signals on a web page.

## Setup and Deployment

### Prerequisites

- Python 3.x
- Alpha Vantage API key

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/iamsaugaat/NepseAIbot.git
   cd NepseAIbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install flask requests pandas ta
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to see the app running locally.

### Deploy to GitHub Pages with GitHub Actions

1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. Configure GitHub Pages in your repository settings:
   - Go to the repository on GitHub.
   - Navigate to `Settings` > `Pages`.
   - Set the source to the `main` branch and save.

3. GitHub Actions will automatically run the bot based on the schedule defined in the workflow file.

## Customization

- Modify the `generate_signals` function in `app.py` to implement different trading strategies.
- Update the HTML template (`index.html`) to change the appearance of the web page.

## License

This project is licensed under the MIT License.
