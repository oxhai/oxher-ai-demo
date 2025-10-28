"""
OXH AI Demo - HuggingFace Space
Real-time AI-powered crypto trading signals platform

Full platform: https://www.oxher.com
API Key: sk_55d8d615c4bb42c8576ca1fbcdf53f34a7697bd74f1ad213c28750ca2294f93f
"""

import gradio as gr
import requests
import json
from typing import Optional, Dict, Any
import pandas as pd

# API Configuration
API_BASE = "https://www.oxher.com/api"
API_KEY = "sk_55d8d615c4bb42c8576ca1fbcdf53f34a7697bd74f1ad213c28750ca2294f93f"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

# ============================================================================
# SIGNAL GENERATOR
# ============================================================================

def generate_signal(symbol: str, interval: str, balance: float, leverage: int, risk_tolerance: str):
    """Generate AI trading signal with real API"""
    try:
        # Use GET endpoint (no auth required, works with API key)
        response = requests.get(
            f"{API_BASE}/futures-signal",
            headers=headers,
            params={
                "symbol": symbol.upper(),
                "interval": interval,
                "limit": 500
            },
            timeout=30
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
        
        data = response.json()
        
        # Format output
        output = f"""## Trading Signal Generated

**Symbol:** {data.get('symbol', 'N/A')}
**Timeframe:** {data.get('interval', 'N/A')}
**Direction:** {data.get('direction', 'N/A')}
**Confidence:** {data.get('confidence', 0) * 100:.1f}%

### Entry & Exit Levels
- **Entry Price:** ${data.get('price', 0):.4f}
- **Stop Loss:** ${data.get('stopLoss', 0):.4f}
- **Take Profit:** ${data.get('takeProfit', 0):.4f}

### Technical Analysis
- **Trend:** {data.get('trend', 'N/A')}
- **Signal Strength:** {data.get('signalStrength', 'N/A')}

### Rationale
{data.get('rationale', 'Signal generated based on multi-indicator analysis including RSI, MACD, ADX, Supertrend, and advanced momentum indicators.')}

### Risk Warning
This is a demo signal. Always do your own research and never invest more than you can afford to lose.

---
**Want real-time signals with personalized tuning?** Visit [oxher.com](https://www.oxher.com) for full features!
"""
        return output
        
    except Exception as e:
        return f"Error generating signal: {str(e)}"


# ============================================================================
# VISION ANALYSIS
# ============================================================================

def analyze_chart(image):
    """Analyze chart screenshot with AI vision"""
    try:
        if image is None:
            return "Please upload a chart image"
        
        # Prepare multipart form data
        files = {
            'image': ('chart.png', open(image, 'rb'), 'image/png')
        }
        
        response = requests.post(
            f"{API_BASE}/vision/analyze",
            headers={"x-api-key": API_KEY},
            files=files,
            timeout=30
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
        
        data = response.json()
        
        output = f"""## Vision Analysis Results

**Direction:** {data.get('direction', 'N/A')}
**Confidence:** {data.get('confidence', 0):.1f}%
**Timeframe:** {data.get('timeframe', 'N/A')}
**Symbol:** {data.get('symbol', 'N/A')}

### Detected Patterns
{', '.join(data.get('patterns', [])) if data.get('patterns') else 'No patterns detected'}

### Price Levels
- **Entry:** ${data.get('levels', {}).get('entry', 0):.2f}
- **Stop Loss:** ${data.get('levels', {}).get('sl', 0):.2f}
- **Take Profit 1:** ${data.get('levels', {}).get('tp1', 0):.2f}
- **Take Profit 2:** ${data.get('levels', {}).get('tp2', 0):.2f}

### Analysis
{data.get('rationale', 'No analysis provided')}

---
**Need advanced pattern recognition?** Try [oxher.com](https://www.oxher.com) for real-time vision analysis!
"""
        return output
        
    except Exception as e:
        return f"Error analyzing chart: {str(e)}"


# ============================================================================
# TECHNICAL INDICATORS
# ============================================================================

def get_indicators(symbol: str, interval: str):
    """Fetch technical indicators"""
    try:
        # Get current price
        price_response = requests.get(
            f"{API_BASE}/price?symbol={symbol.upper()}",
            headers=headers,
            timeout=10
        )
        price = 0
        if price_response.status_code == 200:
            price = price_response.json().get('price', 0)
        
        # Get indicators
        payload = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": 500
        }
        
        response = requests.post(
            f"{API_BASE}/technical-indicators",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
        
        data = response.json()
        indicators = data.get('indicators', {})
        
        # Extract last values from arrays
        rsi_array = indicators.get('rsi14', [])
        rsi = rsi_array[-1] if rsi_array and len(rsi_array) > 0 else 0
        
        atr_array = indicators.get('atr14', [])
        atr = atr_array[-1] if atr_array and len(atr_array) > 0 else 0
        
        ema50_array = indicators.get('ema50', [])
        ema50 = ema50_array[-1] if ema50_array and len(ema50_array) > 0 else 0
        
        sma20_array = indicators.get('sma20', [])
        sma20 = sma20_array[-1] if sma20_array and len(sma20_array) > 0 else 0
        
        # MACD
        macd_data = indicators.get('macd', {})
        macd_array = macd_data.get('macd', [])
        macd_signal_array = macd_data.get('signal', [])
        macd = macd_array[-1] if macd_array and len(macd_array) > 0 else 0
        macd_signal = macd_signal_array[-1] if macd_signal_array and len(macd_signal_array) > 0 else 0
        
        # Bollinger Bands
        boll = indicators.get('bollinger', {})
        boll_upper_array = boll.get('upper', [])
        boll_middle_array = boll.get('middle', [])
        boll_lower_array = boll.get('lower', [])
        boll_upper = boll_upper_array[-1] if boll_upper_array and len(boll_upper_array) > 0 else 0
        boll_middle = boll_middle_array[-1] if boll_middle_array and len(boll_middle_array) > 0 else 0
        boll_lower = boll_lower_array[-1] if boll_lower_array and len(boll_lower_array) > 0 else 0
        
        output = f"""## Technical Indicators - {symbol.upper()}

**Timeframe:** {interval}
**Price:** ${price:.2f}

### Momentum Indicators
- **RSI (14):** {rsi:.2f} - {'Oversold' if rsi < 30 else 'Overbought' if rsi > 70 else 'Neutral'}
- **MACD:** {macd:.4f}
- **MACD Signal:** {macd_signal:.4f}
- **MACD Histogram:** {macd - macd_signal:.4f}

### Trend Indicators
- **EMA 50:** ${ema50:.2f}
- **SMA 20:** ${sma20:.2f}
- **Trend:** {'Bullish' if ema50 > sma20 else 'Bearish' if ema50 < sma20 else 'Neutral'}

### Volatility Indicators
- **ATR (14):** {atr:.4f}
- **Bollinger Upper:** ${boll_upper:.2f}
- **Bollinger Middle:** ${boll_middle:.2f}
- **Bollinger Lower:** ${boll_lower:.2f}
- **Bollinger Width:** {boll_upper - boll_lower:.2f}

### Analysis
- **Total Indicators:** {data.get('meta', {}).get('count', 0)} candles analyzed

---
**Want live indicator updates?** Check out [oxher.com](https://www.oxher.com) for real-time data with 50+ indicators!
"""
        return output
        
    except Exception as e:
        return f"Error fetching indicators: {str(e)}"


# ============================================================================
# MULTI-SYMBOL SCANNER
# ============================================================================

def scan_symbols(symbols_text: str, intervals_text: str, risk: str):
    """Scan multiple symbols for signals"""
    try:
        symbols = [s.strip().upper() for s in symbols_text.split(',') if s.strip()]
        intervals = [i.strip() for i in intervals_text.split(',') if i.strip()]
        
        if not symbols or not intervals:
            return "Please provide symbols and intervals"
        
        payload = {
            "symbols": symbols,
            "intervals": intervals,
            "riskTolerance": risk.lower(),
            "balance": 1000,
            "leverage": 10
        }
        
        response = requests.post(
            f"{API_BASE}/scan-bulk",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
        
        # Response is array of bundles: [{symbol, all, best, exchanges}]
        bundles = response.json()
        
        if not bundles or len(bundles) == 0:
            return "No signals found"
        
        # Create table from best signals
        df_data = []
        for bundle in bundles[:10]:  # Limit to 10 results
            best = bundle.get('best', {})
            df_data.append({
                'Symbol': bundle.get('symbol', 'N/A'),
                'Interval': best.get('interval', 'N/A'),
                'Direction': best.get('direction', 'N/A'),
                'Confidence': f"{best.get('confidence', 0) * 100:.1f}%",
                'Entry': f"${best.get('price', 0):.4f}",
                'Stop Loss': f"${best.get('stopLoss', 0):.4f}",
                'Take Profit': f"${best.get('takeProfit', 0):.4f}"
            })
        
        df = pd.DataFrame(df_data)
        
        output = f"""## Bulk Scan Results

**Symbols Scanned:** {len(symbols)}
**Timeframes:** {', '.join(intervals)}
**Signals Found:** {len(bundles)}

### Top Opportunities

{df.to_markdown(index=False)}

---
**Want to scan 100+ pairs?** Visit [oxher.com](https://www.oxher.com) for unlimited scanning!
"""
        return output
        
    except Exception as e:
        return f"Error scanning symbols: {str(e)}"


# ============================================================================
# NEWS FEED
# ============================================================================

def get_news():
    """Fetch latest crypto news"""
    try:
        response = requests.get(
            f"{API_BASE}/news-feed",
            headers=headers,
            timeout=30
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
        
        # Response is direct array from backend
        articles = response.json()
        
        if not articles or len(articles) == 0:
            return "No news available"
        
        # Limit to 10 articles
        articles = articles[:10]
        
        output = "## Latest Crypto News\n\n"
        
        for idx, article in enumerate(articles, 1):
            title = article.get('title', 'No title')
            source = article.get('source', 'Unknown')
            pub_date = article.get('pub_date') or article.get('created_at', 'N/A')
            description = article.get('description') or article.get('content', 'No description available')
            
            # Truncate description
            if len(description) > 200:
                description = description[:200] + "..."
            
            output += f"""### {idx}. {title}

**Source:** {source}
**Published:** {pub_date}

{description}

---

"""
        
        output += "\n**Want real-time news alerts?** Visit [oxher.com](https://www.oxher.com) for instant notifications!"
        
        return output
        
    except Exception as e:
        return f"Error fetching news: {str(e)}"


# ============================================================================
# PRICE CHECKER
# ============================================================================

def check_price(symbol: str):
    """Check current price"""
    try:
        response = requests.get(
            f"{API_BASE}/price?symbol={symbol.upper()}",
            headers=headers,
            timeout=10
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code}"
        
        data = response.json()
        
        return f"""## Current Price

**Symbol:** {data.get('symbol', 'N/A')}
**Price:** ${data.get('price', 0):.4f}

---
**Want live price streaming?** Check [oxher.com](https://www.oxher.com) for real-time updates!
"""
        
    except Exception as e:
        return f"Error: {str(e)}"


# ============================================================================
# GRADIO UI
# ============================================================================

# Custom CSS - Oxher Style (white, minimal, clean)
custom_css = """
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #ffffff;
    color: #111111;
}

.gradio-container {
    max-width: 1400px !important;
    margin: 0 auto;
}

h1, h2, h3 {
    color: #111111 !important;
    font-weight: 700 !important;
}

.gr-button-primary {
    background: #3b82f6 !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}

.gr-button-primary:hover {
    background: #2563eb !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
}

.gr-input, .gr-textarea, .gr-dropdown {
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    background: #ffffff !important;
}

.gr-box {
    border: 1px solid #e5e7eb !important;
    border-radius: 12px !important;
    background: #ffffff !important;
}

.gr-panel {
    background: #f8fafc !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
}

/* Tab styling */
.gr-tab {
    border: 1px solid #e5e7eb !important;
    border-radius: 8px 8px 0 0 !important;
    background: #ffffff !important;
}

.gr-tab-selected {
    background: #3b82f6 !important;
    color: white !important;
}
"""

# Create Gradio Interface
with gr.Blocks(css=custom_css, title="OXH AI - Demo") as demo:
    
    gr.Markdown("""
    # OXH AI - AI-Powered Crypto Trading Signals
    
    **Live Demo** | Full platform with real-time updates: [oxher.com](https://www.oxher.com)
    
    This demo uses **real data** from our production API. All signals and analysis are live!
    """)
    
    with gr.Tabs():
        
        # TAB 1: Signal Generator
        with gr.Tab("Signal Generator"):
            gr.Markdown("### Generate AI Trading Signals")
            gr.Markdown("Get real-time AI-powered trading signals with entry/exit levels and risk management")
            
            with gr.Row():
                with gr.Column():
                    sig_symbol = gr.Textbox(label="Symbol", value="BTCUSDT", placeholder="BTCUSDT")
                    sig_interval = gr.Dropdown(
                        label="Timeframe",
                        choices=["1m", "5m", "15m", "30m", "1h", "4h", "1d"],
                        value="1h"
                    )
                    sig_balance = gr.Number(label="Balance (USD)", value=1000)
                    sig_leverage = gr.Slider(label="Leverage", minimum=1, maximum=125, value=10, step=1)
                    sig_risk = gr.Dropdown(
                        label="Risk Tolerance",
                        choices=["Low", "Medium", "High"],
                        value="Medium"
                    )
                    sig_btn = gr.Button("Generate Signal", variant="primary")
                
                with gr.Column():
                    sig_output = gr.Markdown(label="Signal Results")
            
            sig_btn.click(
                fn=generate_signal,
                inputs=[sig_symbol, sig_interval, sig_balance, sig_leverage, sig_risk],
                outputs=sig_output
            )
        
        # TAB 2: Vision Analysis
        with gr.Tab("Vision Analysis"):
            gr.Markdown("### AI Chart Analysis")
            gr.Markdown("""Upload chart screenshots from **any source for instant AI analysis:
            
**Supported Sources:**
- TradingView charts
- Binance exchange screenshots
- Bybit trading interface  
- OKX platform charts
- Any other exchange or charting tool

**Simply upload and our AI automatically:**
- Detects patterns (head & shoulders, triangles, channels, wedges)
- Identifies support/resistance levels
- Provides entry/exit recommendations
- No manual input needed!

**Want to test signals risk-free?** Visit [oxher.com](https://www.oxher.com) for **Auto Signals Simulator**:
- Test without real money
- No exchange account needed
- No API key required
- Just OXH credits
- 100% independent system""")
            
            with gr.Row():
                with gr.Column():
                    vision_image = gr.Image(label="Upload Chart Image", type="filepath")
                    vision_btn = gr.Button("Analyze Chart", variant="primary")
                
                with gr.Column():
                    vision_output = gr.Markdown(label="Analysis Results")
            
            vision_btn.click(
                fn=analyze_chart,
                inputs=vision_image,
                outputs=vision_output
            )
        
        # TAB 3: Technical Indicators
        with gr.Tab("Technical Indicators"):
            gr.Markdown("### Real-Time Technical Indicators")
            gr.Markdown("Get comprehensive technical analysis with RSI, MACD, Bollinger Bands, and more")
            
            with gr.Row():
                with gr.Column():
                    ind_symbol = gr.Textbox(label="Symbol", value="BTCUSDT", placeholder="BTCUSDT")
                    ind_interval = gr.Dropdown(
                        label="Timeframe",
                        choices=["1m", "5m", "15m", "30m", "1h", "4h", "1d"],
                        value="1h"
                    )
                    ind_btn = gr.Button("Get Indicators", variant="primary")
                
                with gr.Column():
                    ind_output = gr.Markdown(label="Indicators")
            
            ind_btn.click(
                fn=get_indicators,
                inputs=[ind_symbol, ind_interval],
                outputs=ind_output
            )
        
        # TAB 4: Multi-Symbol Scanner
        with gr.Tab("Bulk Scanner"):
            gr.Markdown("### Scan Multiple Symbols")
            gr.Markdown("Scan multiple trading pairs simultaneously to find the best opportunities")
            
            with gr.Row():
                with gr.Column():
                    scan_symbols_input = gr.Textbox(
                        label="Symbols (comma-separated)",
                        value="BTCUSDT,ETHUSDT,BNBUSDT",
                        placeholder="BTCUSDT,ETHUSDT,SOLUSDT"
                    )
                    scan_intervals_input = gr.Textbox(
                        label="Timeframes (comma-separated)",
                        value="1h,4h",
                        placeholder="1h,4h,1d"
                    )
                    scan_risk = gr.Dropdown(
                        label="Risk Tolerance",
                        choices=["Low", "Medium", "High"],
                        value="Medium"
                    )
                    scan_btn = gr.Button("Scan Symbols", variant="primary")
                
                with gr.Column():
                    scan_output = gr.Markdown(label="Scan Results")
            
            scan_btn.click(
                fn=scan_symbols,
                inputs=[scan_symbols_input, scan_intervals_input, scan_risk],
                outputs=scan_output
            )
        
        # TAB 5: News Feed
        with gr.Tab("News Feed"):
            gr.Markdown("### Latest Crypto News")
            gr.Markdown("Stay updated with the latest cryptocurrency news and market updates")
            
            news_btn = gr.Button("Load Latest News", variant="primary")
            news_output = gr.Markdown(label="News")
            
            news_btn.click(
                fn=get_news,
                inputs=None,
                outputs=news_output
            )
        
        # TAB 6: Price Checker
        with gr.Tab("Price Checker"):
            gr.Markdown("### Quick Price Check")
            gr.Markdown("Get current market prices for any trading pair")
            
            with gr.Row():
                with gr.Column():
                    price_symbol = gr.Textbox(label="Symbol", value="BTCUSDT", placeholder="BTCUSDT")
                    price_btn = gr.Button("Check Price", variant="primary")
                
                with gr.Column():
                    price_output = gr.Markdown(label="Price")
            
            price_btn.click(
                fn=check_price,
                inputs=price_symbol,
                outputs=price_output
            )
    
    gr.Markdown("""
    ---
    ## About OXH AI
    
    This is a **live demo** showcasing our production API capabilities with real market data.
    
    ### Full Platform Features at [oxher.com](https://www.oxher.com)
    
    **Signal Generation:**
    - Real-time signals updated every minute
    - 100+ trading pairs across Binance, Bybit, OKX
    - Advanced AI pattern recognition
    - Personalized signal tuning
    
    **Auto Signals Simulator:**
    - Test signals without risking real money
    - See actual performance in simulated environment
    - No exchange account connection needed
    - No API keys required from you
    - Just OXH credits and you're ready to go
    
    **Additional Features:**
    - Portfolio performance tracking
    - Telegram instant alerts
    - Risk management tools
    - Webhook integrations
    - API access for developers
    - Historical signal analysis
    
    ### Important: How We Work
    
    **We are a SIGNAL PLATFORM, not an exchange:**
    - You trade on YOUR OWN exchange account
    - We NEVER ask for your exchange API keys
    - We NEVER access your trading accounts
    - We NEVER hold your funds
    - We provide intelligence, YOU execute trades
    - You maintain 100% control of your assets
    
    **Safe & Secure:**
    - Zero custody model
    - Complete independence
    - Your security is our priority
    
    ---
    
    **Links:**
    - **Website:** [oxher.com](https://www.oxher.com)
    - **GitHub:** [github.com/oxhai](https://github.com/oxhai)
    - **LinkedIn:** [linkedin.com/company/oxhai](https://www.linkedin.com/company/oxhai/)
    - **Telegram:** [t.me/aioxh](https://t.me/aioxh)
    - **YouTube:** [youtube.com/@aioxh](https://www.youtube.com/@aioxh)
    """)

if __name__ == "__main__":
    demo.queue()
    demo.launch()

