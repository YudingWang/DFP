const axios = require('axios');

async function fetchStockData(symbol) {
    const url = `http://finance.yahoo.com/quote/${symbol}`;
    try {
        const response = await axios.get(url);
        // Process response.data
    } catch (error) {
        console.error('Error fetching stock data:', error);
    }
}
