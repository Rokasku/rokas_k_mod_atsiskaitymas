import requests
from bs4 import BeautifulSoup
import os
import csv
from typing import Union, List, Dict

def crawl_website(
    url: str, output_format: str = "dict"
) -> Union[Dict, List, str]:

    data = {"titles": [], "links": []}

    try:
        # Tikriname, ar formatas yra teisingas
        if output_format not in ["dict", "list", "csv"]:
            raise ValueError("Invalid output format. Use 'dict', 'list', or 'csv'.")

        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        titles = [tag.text.strip() for tag in soup.find_all("h1")[:5]]
        links = [tag.get("href") for tag in soup.find_all("a", href=True)[:5]]
        data["titles"] = titles
        data["links"] = links

        if output_format == "dict":
            return data
        elif output_format == "list":
            return [{"title": t, "link": l} for t, l in zip(data["titles"], data["links"])]
        elif output_format == "csv":
            os.makedirs("output", exist_ok=True)
            file_path = "output/results.csv"
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Link"])
                writer.writerows(zip(data["titles"], data["links"]))
            return f"Data saved to {file_path}"
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    website = input("Enter website URL (e.g., https://example.com): ")
    format_choice = input("Choose output format (dict, list, csv): ")
    print(crawl_website(website, output_format=format_choice))
