# Chocolatescraper

A Scrapy project that scrapes product information (name, price, and URL) from [The Chocolate Company UK](https://www.chocolate.co.uk/collections/all) product listings, following pagination until all products are retrieved. The spider outputs data in **JSON** or **CSV** formats.

---

## Project Structure

```
chocolatescraper/
├── chocolatescraper/           # Project settings and modules
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       └── chocolatespider.py  # Main spider
├── scrapy.cfg                   # Scrapy configuration file
├── requirements.txt             # Dependencies
└── venv/                        # Python virtual environment
```

---

## Spider Details

**File:** `spiders/chocolatespider.py`  
**Spider Name:** `chocolatespider`  
**Start URL:** `https://www.chocolate.co.uk/collections/all`

The spider:

1. Scrapes product name, price, and URL from each product listing.
2. Handles pagination until all product pages are visited.
3. Outputs results in the format you specify (CSV or JSON).

Example output item:
```json
{
    "name": "Milk Chocolate Bar",
    "price": "£4.50",
    "url": "/products/milk-chocolate-bar"
}
```

---

## Installation & Setup

1. **Clone this repository** (or copy the folder into your workspace):
   ```bash
   git clone <repo-url>
   cd chocolatescraper
   ```

2. **Create & activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Spider

### Output to JSON
```bash
scrapy crawl chocolatespider -o myscrapeddata.json
```

### Output to CSV
```bash
scrapy crawl chocolatespider -o myscrapeddata.csv
```

**Note:**  
If `myscrapeddata.json` or `myscrapeddata.csv` already exists, Scrapy will append data to it unless you delete or rename the file before running again.

---

## Example Commands

Run the spider with JSON output:
```bash
scrapy crawl chocolatespider -o myscrapeddata.json
```

Run the spider with CSV output:
```bash
scrapy crawl chocolatespider -o myscrapeddata.csv
```

---

## Requirements

- Python 3.8+
- Scrapy (see `requirements.txt`)

---

## License

This project is for educational purposes only. Scraping should always respect the target website’s `robots.txt` rules and terms of service.

