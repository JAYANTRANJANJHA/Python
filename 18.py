import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin

def setup_database():
    """Create and connect to SQLite database"""
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS scraped_data
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      url TEXT,
                      content TEXT,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn

def scrape_website(base_url, conn):
    """Scrape data from website and store in database"""
    try:
        # Fetch webpage
        response = requests.get(base_url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Scrape article titles and links (modify based on target site)
        articles = soup.find_all('article', limit=5)  # Adjust selector as needed
        
        cursor = conn.cursor()
        for article in articles:
            title = article.find('h2').get_text(strip=True) if article.find('h2') else 'No title'
            relative_url = article.find('a')['href'] if article.find('a') else ''
            url = urljoin(base_url, relative_url)
            
            # Get article content (example - visit each article page)
            content = scrape_article_content(url) if url else 'No content available'
            
            # Insert into database
            cursor.execute('''INSERT INTO scraped_data (title, url, content)
                             VALUES (?, ?, ?)''', (title, url, content))
        
        conn.commit()
        print(f"Successfully scraped and stored {len(articles)} items")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_article_content(article_url):
    """Scrape content from individual article page"""
    try:
        response = requests.get(article_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract article content - adjust selector based on target site
        content_paragraphs = soup.select('article p')  # Example selector
        return ' '.join(p.get_text(strip=True) for p in content_paragraphs)
    except:
        return "Could not retrieve content"

def main():
    # Example URL (replace with target website)
    target_url = "https://example-news-website.com/articles"
    
    # Setup database
    conn = setup_database()
    
    # Scrape website and store data
    scrape_website(target_url, conn)
    
    # Close database connection
    conn.close()
    print("Scraping complete. Data stored in scraped_data.db")

if __name__ == "__main__":
    main()
