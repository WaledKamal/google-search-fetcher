# GoogleSearchResultsFetcher

## Overview
`GoogleSearchResultsFetcher` is a Python script to fetch website URLs from Google search results based on a given query. It uses the `googlesearch-python` library for simple integration with Google Search.

## Features
- Perform Google searches programmatically.
- Retrieve multiple results with URLs.
- Easy to use and customizable.

---

## Requirements
- Python 3.6 or above.
- Libraries:
  - `googlesearch-python`

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/waledkamal/google-search-fetcher.git
    cd google-search-fetcher
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Run the script:
    ```bash
    python google_search_fetcher.py
    ```

2. Enter the search description when prompted, e.g.:
    ```
    Enter a description for the search (e.g., boosting games website): boosting games website
    ```

3. Specify the number of results to retrieve:
    ```
    How many results do you want to retrieve? 10
    ```

4. View the output with URLs of websites:
    ```
    1. https://example1.com
    2. https://example2.com
    ```

---

## Notes
- Respect Google’s [Terms of Service](https://policies.google.com/terms) when using this tool.
- For large-scale or API-based queries, consider using the [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/introduction).

---

## License
This project is licensed under the MIT License.
