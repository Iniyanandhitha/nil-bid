# BidSecure - Private Auctions

BidSecure is a next-generation auction platform that combines privacy-preserving computation with a modern, ethereal "Pastel Sparkly" aesthetic. Built on the **Nillion Network**, it allows registered users to place blind bids on items, ensuring that bid amounts remain encrypted and confidential until the auction closes.

## ✨ New Features: Pastel Sparkly Theme
The application has been completely redesigned with a **Glassmorphism** and **Pastel Gradient** theme:
- **Glass Panels**: Modern frosted glass containers for all content.
- **Dynamic Backgrounds**: Floating blobs and subtle noise textures that bring the UI to life.
- **Micro-Interactions**: Smooth hover effects, animated gradients, and responsive layouts.
- **Unified Design**: Consistent styling across Home, Login, Signup, and Dashboards.

## Core Features
- **Secure Blind Bidding**: Leverages Nillion's multi-party computation (MPC) to keep bids private.
- **Role-Based Dashboards**: tailored experiences for both **Auctioneers** (listing items) and **Bidders** (placing bids).
- **Real-Time Updates**: Status indicators for live, upcoming, and closed auctions.
- **Search & Filter**: Easily find auctions by status (Ongoing, Completed) or keyword.

## 🛠 Installation & Setup

### Prerequisites
- Python 3.10+
- [nillion-sdk](https://docs.nillion.com/nillion-sdk-and-tools)
- Redis (for Celery background tasks)

### Step 1: Environment Setup
Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Nillion Network
Start the local Nillion devnet:
```bash
cd auction/nillion
./bootstrap-local-environment.sh
# Keep this terminal running!
```

### Step 3: Database & Redis
Apply migrations and ensure Redis is running:
```bash
python manage.py migrate
sudo systemctl start redis-server
```

### Step 4: Run the Application
You will need **4 separate terminals** to run the full stack:

**Terminal 1: Django Server**
```bash
source .venv/bin/activate
python manage.py runserver
```

**Terminal 2: Tailwind CSS Watcher** (Compiles the pastel theme)
```bash
source .venv/bin/activate
python manage.py tailwind start
```

**Terminal 3: Celery Worker** (Processes bids)
```bash
source .venv/bin/activate
celery -A bidding worker --loglevel=info
```

**Terminal 4: Celery Beat** (Scheduled tasks)
```bash
source .venv/bin/activate
celery -A bidding beat --loglevel=info
```

## 🚀 Usage

### For Bidders
1.  **Sign Up**: Create a "Bidder" account.
2.  **Browse**: Explore the "Live Now" auctions on your dashboard.
3.  **Bid**: Place a blind bid. Your amount is encrypted via Nillion.
4.  **Win**: Wait for the auction to close to see if you won!

### For Auctioneers
1.  **Sign Up**: Create an "Auctioneer" account.
2.  **Create**: List a new item with a base price and image.
3.  **Manage**: Track bids and close auctions from your dashboard.

## Security
BidSecure uses the **Nillion Network** to decentralize and encrypt sensitive auction data. Unlike traditional databases, bid values are split and distributed across nodes, making them mathematically impossible to expose without authorization.

## License
MIT License. See [LICENSE](LICENSE) for details.
