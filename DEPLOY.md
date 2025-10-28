# Deployment Guide - HuggingFace Spaces

## Prerequisites

- HuggingFace account (free to create at [huggingface.co](https://huggingface.co))
- Basic understanding of Git (optional, for advanced deploy method)
- No technical setup required on your machine

## Quick Deploy (5 Minutes)

### Step 1: Create HuggingFace Account
1. Go to [huggingface.co/join](https://huggingface.co/join)
2. Sign up with email, Google, or GitHub
3. Verify your email address
4. You're ready to deploy!

### Step 2: Create New Space
1. Click **"New Space" button in top navigation
2. Fill in Space details:
   - **Owner:** Your username
   - **Space name:** `oxher-demo` or `oxh-ai-demo` (must be lowercase, no spaces)
   - **License:** MIT
   - **SDK:** Select **Gradio**
   - **Hardware:** CPU (Free tier - sufficient for this demo)
   - **Visibility:** Public (recommended for maximum reach)
3. Click **"Create Space"**

### Step 3: Upload Essential Files
Upload these 3 files in order (drag & drop or use upload button):

1. **README.md** - Contains Space metadata and description
2. **requirements.txt** - Python dependencies (auto-installed by HuggingFace)
3. **app.py** - Main application code

**Important:** Upload README.md first as it contains Space configuration!

### Step 4: Automatic Build
- HuggingFace automatically detects Gradio SDK
- Installs dependencies from requirements.txt
- Builds and deploys your Space
- **Wait 2-3 minutes** for build completion
- Check build logs in Space settings if needed

### Step 5: Test Your Demo
Once build completes, your Space is live!

Test all 6 tabs:
1. **Signal Generator** - Generate signal for BTCUSDT
2. **Vision Analysis** - Upload a chart screenshot
3. **Technical Indicators** - Check ETHUSDT indicators
4. **Bulk Scanner** - Scan multiple symbols
5. **News Feed** - Load latest crypto news
6. **Price Checker** - Check current prices

All features use **real production API** with live market data!

## Alternative: Git Deploy (Advanced)

For developers who prefer Git workflow:

```bash
# Install git-lfs (required for HuggingFace)
git lfs install

# Clone your new Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/oxher-demo
cd oxher-demo

# Copy all demo files
cp -r ../oxher-demo/* .

# Add all files to git
git add .

# Commit with descriptive message
git commit -m "Deploy: OXH AI Trading Signals Demo

Features:
- Real-time signal generation
- AI vision analysis
- Technical indicators
- Multi-symbol scanner
- Crypto news feed
- Price checker

API: https://www.oxher.com/api"

# Push to HuggingFace
git push
```

HuggingFace will automatically detect changes and rebuild your Space.

## Configuration

**No configuration needed!**

- API key is embedded in code (public demo key)
- Valid for 1 month
- Rate limits handled by backend
- No secrets or environment variables required
- Works out of the box

### Optional: Extend API Key

If the demo API key expires, contact OXH AI team:
- Email: support@oxher.com
- Telegram: [@aioxh](https://t.me/aioxh)
- Create ticket at: [oxher.com/help](https://www.oxher.com/help)

## Features Enabled

### 1. Signal Generator
- Real-time AI signal generation
- Multi-timeframe analysis (1m to 1d)
- Confidence scoring
- Entry/exit levels with stop loss/take profit
- Uses GET `/futures-signal` endpoint

### 2. Vision Analysis  
**Upload chart screenshots from anywhere:**
- TradingView charts
- Binance exchange screenshots
- Bybit trading interface
- OKX platform charts
- Any other exchange or charting tool

**Simply upload a screenshot and our AI will:**
- Automatically detect the chart
- Identify patterns (head & shoulders, triangles, channels, etc.)
- Find support/resistance levels
- Provide trading recommendations
- No manual input needed!

Uses POST `/vision/analyze` endpoint with multipart file upload

### 3. Technical Indicators
- 10+ indicators (RSI, MACD, Bollinger Bands, ATR, etc.)
- Real-time calculation from live market data
- Uses POST `/technical-indicators` endpoint

### 4. Bulk Scanner
- Scan multiple trading pairs simultaneously
- Multiple timeframe analysis
- Ranked by best opportunities
- Uses POST `/scan-bulk` endpoint

### 5. News Feed
- Latest crypto market news
- Multiple sources aggregated
- Uses GET `/news-feed` endpoint

### 6. Price Checker
- Quick price lookups for any pair
- Real-time exchange prices
- Uses GET `/price` endpoint

## Important: Auto Signals Simulator

**This demo shows our API capabilities, but for the BEST experience:**

Visit [oxher.com](https://www.oxher.com) to access **Auto Signals Simulator**:

- **Test signals without real money** - See how signals perform in simulated environment
- **No exchange account needed** - Completely standalone system
- **No API key required** - We never ask for your exchange credentials
- **Just OXH credits** - Purchase credits and start testing immediately
- **Safe testing environment** - Learn signal quality before trading real money
- **Full platform features** - Portfolio tracking, Telegram alerts, custom tuning, and more

**We are a signal platform, NOT an exchange:**
- You maintain full control of your funds
- Trade on YOUR OWN exchange account
- We provide intelligence, you execute trades
- Zero custody - maximum security

## Monitoring & Analytics

### View Space Logs
1. Go to your Space page
2. Click "Settings" tab
3. Select "Logs" section
4. Monitor real-time activity:
   - API response times
   - Error rates
   - User interactions
   - Request patterns

### Analytics to Track
- Daily active users
- Most popular tabs
- Average session duration
- API endpoint usage
- Conversion to oxher.com

## Updating Your Demo

### Method 1: Web UI
1. Go to your Space page
2. Click "Files" tab
3. Select file to edit (e.g., `app.py`)
4. Click "Edit" button
5. Make changes
6. Click "Commit changes"
7. Space automatically rebuilds

### Method 2: Git
```bash
cd oxher-demo
# Make changes to files
git add .
git commit -m "Update: description of changes"
git push
```

Space will auto-rebuild on push (takes 2-3 minutes).

## Troubleshooting

### Build Fails
- Check build logs in Space settings
- Verify requirements.txt has correct package versions
- Ensure app.py has no syntax errors
- Check Python version compatibility (3.9+)

### API Errors
- Verify API key is correct
- Check oxher.com API status
- Test endpoints with curl:
```bash
curl -H "x-api-key: sk_55d8d615c4bb42c8576ca1fbcdf53f34a7697bd74f1ad213c28750ca2294f93f" \
     https://www.oxher.com/api/price?symbol=BTCUSDT
```

### Slow Performance
- Normal for CPU tier (free)
- Upgrade to GPU if needed (paid)
- Optimize timeout values in app.py

## Support

Need help with deployment?

- GitHub Issues: [github.com/oxhai/issues](https://github.com/oxhai)
- Email: support@oxher.com
- Telegram Community: [@aioxh](https://t.me/aioxh)
- Help Center: [oxher.com/help](https://www.oxher.com/help)

## Post-Deployment Checklist

After successful deployment:

- [ ] Test all 6 tabs thoroughly
- [ ] Verify real data is loading
- [ ] Upload a test chart for Vision Analysis
- [ ] Check Space logs for errors
- [ ] Add Space URL to oxher.com website
- [ ] Share on social media (Twitter, LinkedIn, Telegram)
- [ ] Add link to GitHub README
- [ ] Monitor usage metrics
- [ ] Collect user feedback

## Next Steps

1. Promote Your Demo
   - Add prominent link on oxher.com homepage
   - Create social media posts
   - Share in crypto trading communities
   - Add to GitHub repository README

2. Monitor Performance
   - Track daily users
   - Measure conversion rates
   - Analyze popular features
   - Collect user feedback

3. Optimize Based on Data
   - Add more popular features
   - Improve slow endpoints
   - Update documentation
   - Enhance UX based on usage patterns

---

Deployment completed! Your OXH AI demo is now live on HuggingFace.

