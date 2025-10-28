# Quick Start Guide

Welcome! This guide will help you deploy the OXH AI demo to HuggingFace Spaces in just 5 minutes.

## Prerequisites

- HuggingFace account (create free at [huggingface.co/join](https://huggingface.co/join))
- 3 files ready: `app.py`, `requirements.txt`, `README.md`

## Local Testing (Optional)

If you want to test locally before deploying:

```bash
cd huggingface-demos/oxher-demo

# Install dependencies
pip install -r requirements.txt

# Run the app locally
python app.py
```

The app will be available at `http://localhost:7860`

**Note:** Local testing is optional. You can deploy directly to HuggingFace without testing locally.

## Deploy to HuggingFace (Recommended Method)

### Web UI Deploy - Step by Step

#### Step 1: Create Space (1 minute)
1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Log in if needed
3. Fill in the form:
   - **Space name:** `oxher-demo` or `oxh-ai-demo` (lowercase, no spaces)
   - **License:** MIT
   - **SDK:** Gradio (select from dropdown)
   - **Hardware:** CPU - Free (sufficient for this demo)
   - **Visibility:** Public (recommended for maximum reach)
4. Click **"Create Space"**

#### Step 2: Upload Files (1 minute)

Upload these 3 files **in this order**:

1. **First:** `README.md`
   - Contains Space metadata (title, SDK version, etc.)
   - HuggingFace reads this for configuration
   - Drag & drop or click "Add file"

2. **Second:** `requirements.txt`
   - Python dependencies list
   - HuggingFace auto-installs these packages

3. **Third:** `app.py`
   - Main application code
   - 641 lines, 6 functional tabs

**Important:** Upload README.md first! It contains Space configuration metadata.

#### Step 3: Wait for Build (2-3 minutes)

HuggingFace automatically:
- Detects Gradio SDK
- Creates Python environment
- Installs requirements.txt packages
- Launches app.py
- Exposes public URL

**Watch build progress:**
- Green checkmark = Success
- Red X = Build failed (check logs)
- Orange spinner = Building...

#### Step 4: Test Your Demo (2 minutes)

Once deployed, test all features:

1. **Signal Generator**
   - Symbol: BTCUSDT
   - Timeframe: 1h
   - Click "Generate Signal"
   - Should see: Direction, Confidence, Entry/Exit levels

2. **Vision Analysis**
   - Upload any chart screenshot (TradingView, Binance, etc.)
   - Click "Analyze Chart"
   - Should see: Patterns, Support/Resistance, Recommendations

3. **Technical Indicators**
   - Symbol: ETHUSDT
   - Timeframe: 4h
   - Click "Get Indicators"
   - Should see: RSI, MACD, Bollinger Bands, etc.

4. **Bulk Scanner**
   - Symbols: BTCUSDT,ETHUSDT,BNBUSDT
   - Timeframes: 1h,4h
   - Click "Scan Symbols"
   - Should see: Table with ranked opportunities

5. **News Feed**
   - Click "Load Latest News"
   - Should see: Recent crypto news articles

6. **Price Checker**
   - Symbol: BTCUSDT
   - Click "Check Price"
   - Should see: Current price

**All tabs should show real, live data!**

#### Step 5: Share Your Demo

Your Space is now live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/oxher-demo
```

Share this URL everywhere!

### Method 2: Git (Advanced)

```bash
# Install git-lfs
git lfs install

# Clone your new Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/oxher-demo
cd oxher-demo

# Copy demo files
cp -r ../oxher-demo/* .

# Commit and push
git add .
git commit -m "Deploy OXH AI Demo"
git push
```

## After Deployment

### 1. Test Your Space

Visit your Space URL and test all tabs:
- Signal Generator
- Vision Analysis (upload a chart image)
- Technical Indicators
- Bulk Scanner
- News Feed
- Price Checker

### 2. Share Your Demo

Add to oxher.com:
```html
<a href="https://huggingface.co/spaces/YOUR_USERNAME/oxher-demo" target="_blank">
  Try Live Demo on HuggingFace
</a>
```

### 3. Promote on Social Media

Copy and customize these templates:

**Twitter/X Post:**
```
Try our AI Trading Signals Demo on HuggingFace!

Real-time signals | AI chart analysis | Technical indicators | Multi-symbol scanner

All with REAL market data from our production API

Demo: https://huggingface.co/spaces/YOUR_USERNAME/oxher-demo
Platform: https://oxher.com

#AI #Crypto #Trading #MachineLearning #TradingSignals
```

**LinkedIn Post:**
```
We've just launched our AI-powered crypto trading signals demo on HuggingFace!

Experience the power of our production API:
- Real-time signal generation
- AI vision chart analysis
- 50+ technical indicators
- Multi-symbol bulk scanning
- Live crypto news feed

This demo uses our actual production infrastructure - not mock data.

Try it free: [Your Space URL]
Full platform: https://oxher.com

#AI #CryptoTrading #FinTech #MachineLearning
```

**Telegram Announcement:**
```
LIVE NOW: OXH AI Demo on HuggingFace

Experience our platform capabilities:
- AI Trading Signals (real-time)
- Vision Chart Analysis (screenshot upload)
- Technical Indicators (50+ indicators)
- Multi-Symbol Scanner
- Crypto News Feed

Demo: [Your Space URL]

Full features at oxher.com including:
- Auto Signals Simulator (test without real money!)
- No exchange account connection required
- Just OXH credits needed

Join us: t.me/aioxh
```

**Reddit Post (r/algotrading, r/CryptoCurrency):**
```
Title: Built an AI Trading Signals Platform - Live Demo on HuggingFace

We've been building OXH AI, an AI-powered crypto trading signals platform, and just launched a live demo on HuggingFace.

Features:
- Real-time signal generation
- AI vision analysis for chart screenshots
- 50+ technical indicators
- Multi-symbol bulk scanner
- Live news feed

This uses our production API with real market data - not simulated.

Demo: [Your Space URL]
Platform: oxher.com

Key differentiator: We're a signal platform, not an exchange. You trade on your own accounts. We never hold funds or require API key access.

Would love feedback from the community!
```

## Monitoring

Check your Space logs for:
- API response times
- User interactions
- Error rates

Go to: Space Settings → Logs

## Updates

To update your demo:
1. Edit `app.py` locally
2. Test changes
3. Push to HuggingFace
4. Space auto-rebuilds

## Support

Need help?
- GitHub Issues: [github.com/oxhai](https://github.com/oxhai)
- Email: support@oxher.com
- Telegram: [@aioxh](https://t.me/aioxh)

---

**Deployment completed!** Your OXH AI demo is ready to share with the world.

