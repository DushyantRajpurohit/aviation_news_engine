# Aviation News Engine

A Python-based news aggregator designed to scrape, store, and serve aviation-related news from various sources.

## Features

- **News Scraper**: Automatically fetches latest articles from aviation websites defined in `sites.json`.
- **Data Persistence**: Stores scraped articles in a local SQLite database (`demo_data.db`).
- **Web Interface**: Includes a lightweight web server to browse and read the collected news in a user-friendly format.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DushyantRajpurohit/aviation_news_engine.git](https://github.com/DushyantRajpurohit/aviation_news_engine.git)
   cd aviation_news_engine
   ```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Scraper**
Fetch the latest news and update the database:
```bash
python demo_engine.py
```

2. **Start the Web Server**
Launch the application to view the news:
```bash
python server.py
```
Access the interface in your browser (typically at http://127.0.0.1:5000).

3. **Utilities & Configuration**
Add/Remove Sites: Edit `sites.json` to configure the target websites and scraping rules.

Inspect Data: Use the utility script to check database contents:

```bash
python view_data.py
```
