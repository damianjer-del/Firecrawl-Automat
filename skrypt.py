import os
from firecrawl import FirecrawlApp

# Inicjalizacja Firecrawl
app = FirecrawlApp()

# Testowe pobranie zawartości przykładowej strony
response = app.scrape_url('https://example.com')
print(response)
