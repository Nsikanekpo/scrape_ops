# Scrape Ops — Scrapy Projects Collection

This repository contains all my Scrapy projects built while following the **Scrapy Beginners Series** from [ScrapeOps](https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide/).

Each project has its own **virtual environment** and **Scrapy setup** to keep dependencies isolated.

---

## 📂 Project Structure

scrape_ops/
│
├── chocolatescraper/ # Project 1: Chocolate Website Scraper
│ ├── venv/ # Virtual environment (not tracked by Git)
│ ├── chocolatescraper/ # Scrapy project files
│ ├── scrapy.cfg
│ └── requirements.txt
│
├── coffeescraper/ # Project 2: Coffee Product Scraper (future)
│ ├── venv/
│ ├── coffeescraper/
│ └── requirements.txt
│
└── README.md
---

## 🚀 Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/Nsikanekpo/scrape_ops.git

# Navigate to a project
  
  cd chocolatescraper

# Activate its virtual environment   
  
  source venv/bin/activate

# Run a spider 
  
  scrapy crawl chocolatescraper

   ## Project List 
  
Project Name	                 Description	                  Status

chocolatescraper	Scrapes chocolate data from target website  Pending
                  (Beginner Series Part 1)  
  
coffeescraper	    Scrapes coffee product data (Beginner       Pending
                  series Part 2)



# virtual Environment setup(per project)  
  
  ## Inside the project folder

python3 -m venv venv
source venv/bin/activate
pip install scrapy
pip freeze > requirements.txt

 ## 🔄 Git Workflow
All commits are done from the parent folder scrape_ops/ unless specified otherwise. 

# Check status

git status

# Add changes
git add .

# Commit changes
git commit -m "Meaningful commit message"

# Push to GitHub
git push origin main


# 📚 Resources

. Scrapy Documentation

. ScrapeOps Scrapy Beginners Guide




