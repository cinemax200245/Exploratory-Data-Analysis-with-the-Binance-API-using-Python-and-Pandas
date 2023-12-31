<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Cryptocurrency Price Analysis App</h1>

<p>This Streamlit app provides a straightforward interface to analyze the historical price data of cryptocurrencies, powered by the Binance API. Users can input the symbol of the cryptocurrency (e.g., BTCUSDT) and visualize key metrics, such as candlestick charts, monthly average closing prices, and monthly closing price distributions.</p>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<p>Before running the app, ensure that you have the necessary Python libraries installed. You can install them using the following:</p>

<pre>
<code>pip install streamlit pandas plotly cufflinks python-binance</code>
</pre>

<h3>Usage</h3>

<ol>
    <li>Clone the repository:</li>

    <pre>
    <code>git clone https://github.com/yourusername/cryptocurrency-analysis-app.git</code>
    <code>cd cryptocurrency-analysis-app</code>
    </pre>

    <li>Set up your Binance API keys:</li>

    <ul>
        <li>Open <code>crypto_analysis_app.py</code> in a text editor.</li>
        <li>Replace <code>'YOUR_API_KEY'</code> and <code>'YOUR_SECRET_KEY'</code> with your Binance API key and secret key.</li>
    </ul>

    <li>Run the Streamlit app:</li>

    <pre>
    <code>streamlit run crypto_analysis_app.py</code>
    </pre>

    <p>This command will launch a local server, and you can access the app in your web browser.</p>

    <li>Enter the symbol of the cryptocurrency (e.g., BTCUSDT) in the text input and explore the visualizations.</li>
</ol>

<h2>Features</h2>

<ul>
    <li>Candlestick Chart: Visualizes the open, high, low, and close prices over time.</li>
    <li>Monthly Average Closing Price: Displays a scatter plot of monthly average closing prices.</li>
    <li>Monthly Closing Price Distribution: Shows the distribution of closing prices on a monthly basis.</li>
</ul>

<h2>Troubleshooting</h2>

<p>If you encounter any issues, make sure to check the following:</p>

<ul>
    <li>Binance API keys are correctly set in the script.</li>
    <li>The specified cryptocurrency symbol is valid.</li>
</ul>

<p>If you still face problems, feel free to open an issue in this repository.</p>

<h2>Location Constraints</h2>

<p style="color: red;"><strong>Important:</strong> This app may not function properly if accessed from certain locations due to regulatory constraints. Binance, the underlying provider of cryptocurrency data, imposes restrictions on access from specific regions, including but not limited to the United States, Canada, Ontario, Malaysia, etc.</p>

<p>Additionally, please note that Streamlit servers are located and based in the United States. As a result, users from restricted regions may encounter issues running this app on Streamlit's servers.</p>

<p>To ensure proper functionality, it is recommended to run this app/code locally on your machine using a local Jupyter notebook. </p>

<p>Make sure to replace 'apiKey' and 'secretKey' with your actual Binance API key and secret key.</p>

</body>
</html>
