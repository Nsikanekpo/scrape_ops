from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

import psycopg2
from environs import Env



# Load environment variables
env = Env()
env.read_env()

class PriceToUSDPipeline:
    gbpToUsdRate = env.float("GBP_TO_USD_RATE", 1.3)  # fallback to 1.3

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('price'):
            adapter['price'] = float(adapter['price']) * self.gbpToUsdRate
            return item
        else:
            raise DropItem(f"Missing price in {item}")

class DuplicatesPipeline:
    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.names_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        self.names_seen.add(adapter['name'])
        return item

class SavingToPostgresPipeline:

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = psycopg2.connect(
            host=env("POSTGRES_HOST"),
            database=env("POSTGRES_DB"),
            user=env("POSTGRES_USER"),
            password=env("POSTGRES_PASSWORD")
        )
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        try:
            self.curr.execute("""
                INSERT INTO chocolate_products (name, price, url)
                VALUES (%s, %s, %s)
            """, (
                item["name"],
                item["price"],
                item["url"]
            ))
            self.connection.commit()
        except Exception as e:
            print(e)