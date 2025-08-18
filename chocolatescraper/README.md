# Chocolatescraper

A Scrapy project that scrapes product information (name, price, and URL) from [The Chocolate Company UK](https://www.chocolate.co.uk/collections/all) product listings, following pagination until all products are retrieved. The spider stores data in a **PostgreSQL database** and can optionally export to **JSON** or **CSV** formats. It also supports proxy rotation and randomized user-agents via `.env` configuration.

## Project Structure

```text
chocolatescraper/
├── chocolatescraper/           # Project settings and modules
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py          # Includes proxy and user-agent rotation
│   ├── pipelines.py            # Includes price conversion, duplicates removal, and Postgres storage
│   ├── settings.py
│   └── spiders/
│       └── chocolatespider.py  # Main spider
├── scrapy.cfg                  # Scrapy configuration file
├── requirements.txt            # Dependencies
├── .env                        # Environment variables (not pushed to GitHub)
└── venv/                       # Python virtual environment

```

**Notes:**  
- `middlewares.py` includes proxy and user-agent rotation.  
- `pipelines.py` includes price conversion, duplicates removal, and PostgreSQL storage.  
- `.env` stores sensitive credentials like database info and ScrapeOps API key (not pushed to GitHub).  


## Environment Variables

Create a `.env` file in the project root with the following variables:

```dotenv
POSTGRES_HOST=172.17.144.1  
POSTGRES_DB=chocolate_scraping  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=your_postgres_password  
GBP_TO_USD_RATE=1.3  
SCRAPEOPS_API_KEY=your_scrapeops_api_key   # API key for proxy service
```

> **Important:** `.env` is included in `.gitignore` to keep sensitive credentials out of version control.

## Spider Details

**File:** `spiders/chocolatespider.py`  
**Spider Name:** `chocolatespider`  
**Start URL:** `https://www.chocolate.co.uk/collections/all`  

The spider:

1. Scrapes product name, price (converted from GBP to USD), and URL from each product listing.  
2. Handles pagination until all product pages are visited.  
3. Uses `SavingToPostgresPipeline` to store results in PostgreSQL.  
4. Uses the ScrapeOps proxy service via `.env` API key for request routing.  
5. Randomizes user-agents for each request.  
6. Optionally exports data to CSV or JSON if specified in the command.  

Example output item (before DB storage):

```json
{
    "name": "Milk Chocolate Bar",
    "price": 5.85,
    "url": "/products/milk-chocolate-bar"
}
```

## Installation & Setup

1. Clone this repository:  
```bash
git clone <repo-url>
cd chocolatescraper
```

2. Create & activate a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:  
```bash
pip install -r requirements.txt
```

4. Create the `.env` file (see above) and fill in your database and ScrapeOps API credentials.  

5. Ensure your PostgreSQL database is running and the `chocolate_products` table exists:  
```sql
CREATE TABLE IF NOT EXISTS chocolate_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price NUMERIC,
    url TEXT
);
```

## Running the Spider

Output to PostgreSQL (default):  
```bash
scrapy crawl chocolatespider
```

Optional: Output to JSON  
```bash
scrapy crawl chocolatespider -o myscrapeddata.json
```

Optional: Output to CSV  
```bash
scrapy crawl chocolatespider -o myscrapeddata.csv
```

> **Note:** Scrapy will append to JSON/CSV files if they already exist. The PostgreSQL table will append new items but duplicates are filtered automatically.

## Requirements

- Python 3.8+  
- Scrapy 2.x  
- psycopg2  
- environs (for `.env` variable management)

## Security & GitHub

- `.env` is never committed. Credentials are read at runtime via `environs`.  
- Pipelines handle sensitive operations like DB insertion securely without exposing passwords in code.  
- Proxy and user-agent rotation keep scraping behavior safe and reduce blocking risks.

## License

This project is for educational purposes only. Scraping should respect the target website’s `robots.txt` and terms of service.
