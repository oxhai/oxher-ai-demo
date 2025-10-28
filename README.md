# 🚀 OXH AI - Trading Signals Demo

[![Try it on HuggingFace](https://img.shields.io/badge/🤗-Open%20in%20Spaces-blue.svg)](https://huggingface.co/spaces/oxhai/oxher-ai-playground)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Gradio 4.36.1](https://img.shields.io/badge/gradio-4.36.1-orange.svg)](https://gradio.app)

> Live demonstration of OXH AI's trading signal platform using real production data and AI-powered analysis.

---

## 🎮 Try It Now

### **[🚀 Launch Live Demo on HuggingFace Spaces](https://huggingface.co/spaces/oxhai/oxher-ai-playground)**

No installation required - just click and explore!

---

## 📸 Preview

![Demo Screenshot](https://via.placeholder.com/800x400/1e3a8a/ffffff?text=Add+Your+Screenshot+Here)

*Replace this with your actual demo screenshot*

---

## ✨ Features

### 1. **Signal Generator**
- Real-time AI-powered trading signals
- Entry/exit level recommendations
- Stop loss and take profit calculations
- Multi-timeframe analysis (1m to 1d)
- Confidence scoring
- Risk management integration

### 2. **Vision Analysis**
- Upload chart screenshots from any source
- Automatic pattern recognition
- Support/resistance detection
- Trend analysis
- Works with TradingView, Binance, Bybit, OKX charts

### 3. **Technical Indicators**
- RSI, MACD, Stochastic
- Bollinger Bands, ATR
- Moving averages (EMA, SMA)
- Volume indicators (OBV, MFI)
- ADX trend strength

### 4. **Bulk Scanner**
- Scan multiple trading pairs simultaneously
- Multi-timeframe analysis
- Ranked opportunities
- Risk-adjusted signals

### 5. **News Feed**
- Real-time crypto news updates
- Curated market news
- Source attribution

### 6. **Price Checker**
- Quick price lookups
- Real-time market data
- Support for 100+ trading pairs

---

## 🛠️ Tech Stack

- **Frontend:** Gradio 4.36.1
- **Backend API:** Node.js/Express (production)
- **AI Models:** GPT-5 Vision, Custom ML models
- **Data Sources:** Binance, Bybit, OKX
- **Language:** Python 3.10
- **Deployment:** HuggingFace Spaces

---

## 🏗️ Architecture

```
┌─────────────┐
│   Gradio    │ ← User Interface
│  Frontend   │
└──────┬──────┘
       │ HTTP Requests
       ▼
┌─────────────┐
│  REST API   │ ← Production Backend
│ (oxher.com) │
└──────┬──────┘
       │
       ├─► Binance API
       ├─► Bybit API
       ├─► OKX API
       └─► AI Models (GPT-5, Custom)
```

---

## 📦 Installation (Local Development)

### Prerequisites
- Python 3.10+
- pip

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/oxhai/oxher-ai-demo.git
cd oxher-ai-demo
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
python app.py
```

4. **Open in browser:**
```
http://localhost:7860
```

---

## 📋 Requirements

```txt
gradio==4.36.1
requests==2.31.0
pandas>=2.0.0
tabulate==0.9.0
pillow==10.2.0
huggingface-hub==0.19.4
pydantic==2.10.6
```

---

## 🔑 API Configuration

This demo uses OXH AI's public API with a demo key. For production use:

1. Visit [oxher.com](https://www.oxher.com)
2. Sign up for an account
3. Get your API key
4. Replace `API_KEY` in `app.py`

```python
API_BASE = "https://www.oxher.com/api"
API_KEY = "your_api_key_here"
```

---

## 🌐 Live Platforms

### Full Production Platform
Visit [oxher.com](https://www.oxher.com) for the complete platform with:
- Real-time signals updated every minute
- 100+ trading pairs
- Multi-exchange support
- Auto Signals Simulator (test without real money)
- Portfolio tracking
- Telegram alerts
- API access for developers
- Webhook integrations

### Demo (This Project)
Try the demo: [HuggingFace Spaces](https://huggingface.co/spaces/oxhai/oxher-ai-playground)

---

## 🎯 Use Cases

- **Traders:** Get AI-powered trading signals
- **Developers:** See how to integrate trading APIs
- **Data Scientists:** Explore technical indicator analysis
- **Educators:** Teaching AI in finance
- **Researchers:** Study trading algorithms

---

## 📊 Screenshots

### Signal Generator
![Signal Generator](https://via.placeholder.com/600x300/1e3a8a/ffffff?text=Signal+Generator+Screenshot)

### Vision Analysis
![Vision Analysis](https://via.placeholder.com/600x300/1e3a8a/ffffff?text=Vision+Analysis+Screenshot)

### Technical Indicators
![Technical Indicators](https://via.placeholder.com/600x300/1e3a8a/ffffff?text=Technical+Indicators+Screenshot)

*Add your actual screenshots here*

---

## 🔗 Links

- **Website:** [oxher.com](https://www.oxher.com)
- **Live Demo:** [HuggingFace Space](https://huggingface.co/spaces/oxhai/oxher-ai-playground)
- **GitHub:** [github.com/oxhai](https://github.com/oxhai)
- **LinkedIn:** [linkedin.com/company/oxhai](https://www.linkedin.com/company/oxhai/)
- **Telegram:** [t.me/aioxh](https://t.me/aioxh)
- **YouTube:** [youtube.com/@aioxh](https://www.youtube.com/@aioxh)

---

## ⚠️ Disclaimer

This is a demonstration platform for educational purposes. 

**Important:**
- This is NOT financial advice
- Cryptocurrency trading involves substantial risk
- Always do your own research (DYOR)
- Never invest more than you can afford to lose
- We are a signal platform, NOT an exchange
- We NEVER hold your funds or access your accounts

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

The demo code is open source. The underlying API and models are proprietary.

---

## 🤝 Contributing

This is a demo project showcasing our API. For feature requests or bug reports:

1. Open an issue on GitHub
2. Join our [Telegram Community](https://t.me/aioxh)
3. Contact us via [oxher.com](https://www.oxher.com/help)

---

## 🙏 Acknowledgments

- Built with [Gradio](https://gradio.app) by HuggingFace
- Powered by OXH AI's proprietary trading algorithms
- Market data from Binance, Bybit, and OKX
- AI models: GPT-5 Vision and custom ML models

---

## 📧 Contact & Support

- **Website:** [oxher.com](https://www.oxher.com)
- **Support:** [oxher.com/help](https://www.oxher.com/help)
- **Telegram:** [t.me/aioxh](https://t.me/aioxh)
- **Email:** Contact via website

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Built with ❤️ by the OXH AI Team

[Website](https://www.oxher.com) • [Demo](https://huggingface.co/spaces/oxhai/oxher-ai-playground) • [Community](https://t.me/aioxh)

</div>

