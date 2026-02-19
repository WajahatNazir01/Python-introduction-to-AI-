import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ----------------- SETTINGS -----------------
BASE_URL = "https://www.olx.com.pk/items/q-iphone-15-pro-max"
HEADERS = {"User-Agent": "Mozilla/5.0"}
OUTPUT_FILE = "lahore_filtered_iphone15.xlsx"

# ----------------- FUNCTIONS -----------------
def get_listing_links():
    """
    Fetch all listing links from the main search page
    and convert relative URLs to absolute URLs.
    """
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to fetch search page:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/item/" in href:
            # Convert relative URL to absolute
            if href.startswith("/"):
                href = "https://www.olx.com.pk" + href
            links.append(href)

    # Remove duplicates
    return list(set(links))


def scrape_ad(url):
    """
    Scrape individual ad page and filter by:
    - Location: Lahore
    - Color: Natural Titanium
    - Storage: 256GB or above
    - PTA approved
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return None
    except Exception as e:
        print("Error fetching:", url, e)
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ", strip=True).lower()

    # ----------------- FILTER CONDITIONS -----------------
    if "lahore" not in text:
        return None
    if "natural titanium" not in text:
        return None
    if "pta" not in text:
        return None
    if not any(x in text for x in ["256", "512", "1tb"]):
        return None

    # ----------------- EXTRACT INFO -----------------
    title_tag = soup.find("h1")
    price_tag = soup.find("span")

    # Seller and posted time
    seller = ""
    posted_time = ""

    for span in soup.find_all("span"):
        t = span.get_text(strip=True)
        t_lower = t.lower()
        if "member since" in t_lower:
            seller = t
        if "ago" in t_lower or "today" in t_lower:
            posted_time = t

    return {
        "Title": title_tag.get_text(strip=True) if title_tag else "",
        "Price": price_tag.get_text(strip=True) if price_tag else "",
        "URL": url,
        "Seller Info": seller,
        "Posted": posted_time
    }


# ----------------- MAIN SCRIPT -----------------
def main():
    print("Collecting listing links...")
    links = get_listing_links()
    print(f"Found {len(links)} listings on the search page.")

    results = []

    for link in links:
        data = scrape_ad(link)
        if data:
            results.append(data)
            print("Matched:", data["Title"])

        time.sleep(3)  # polite delay to avoid blocking

    if results:
        df = pd.DataFrame(results)
        df.to_excel(OUTPUT_FILE, index=False)
        print(f"Saved {len(results)} filtered listings to {OUTPUT_FILE}")
    else:
        print("No matching ads found. Try adjusting filters or check the page layout.")


if __name__ == "__main__":
    main()
