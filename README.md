# **API-Based Currency Converter**  

## 🌍 About the Project  
This is a **CLI-based currency converter** that fetches real-time exchange rates using the **ExchangeRate-API**. Users can input an amount, select a source currency, and convert it into a target currency.  

## 🚀 Features  
- ✅ Real-time exchange rates fetched via API  
- ✅ Supports multiple currencies (USD, EUR, GBP, etc.)  
- ✅ Simple and user-friendly command-line interface  
- ✅ Error handling for invalid inputs and API failures  

## 🛠️ Installation & Setup  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```

### **2. Install Dependencies**  
Ensure you have **Python** installed. You also need the `requests` library:  
```bash
pip install requests
```

### **3. Get Your API Key**  
1. Sign up at [ExchangeRate-API](https://www.exchangerate-api.com/)  
2. Get your **free API key**  
3. Replace `"your_api_key_here"` in `main.py` with your actual API key  

## 🎯 Usage  
Run the script using:  
```bash
python main.py
```
Follow the on-screen instructions to enter an amount and choose currencies for conversion.

## 📸 Example Output  
```bash
Enter amount: 50
Enter source currency (e.g., USD, EUR, GBP): USD
Enter target currency (e.g., EUR, GBP, JPY): EUR
50 USD = 46.25 EUR
```

## ⚡ Future Improvements  
- 🔹 Add a **GUI version** using Tkinter or PyQt  
- 🔹 Support for **historical exchange rates**  
- 🔹 Implement a **web-based version**  

