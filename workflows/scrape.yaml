name: Price Scrape

on:
  schedule:
    # Runs at selected minutes of every hour.
    - cron: '2,7,12,17,22,27,32,37,42,47,52,57 * * * *'
  workflow_dispatch: # Allows you to run it manually from the Actions tab

jobs:
  update-prices:
    runs-on: ubuntu-latest
    permissions:
      # Give the action permission to write to the repo.
      contents: write
      
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install requests

      - name: Run Scraper
        run: python scraper.py

      - name: Commit and Push changes
        run: |
          git config --global user.name 'GitHub Action'
          git config --global user.email 'action@github.com'
          # Add all text files ending in .txt
          git add prices/*.txt
          git commit -m "Update prices" || exit 0
          git push
