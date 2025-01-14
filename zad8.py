import requests
import argparse
from typing import Optional


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: Optional[str],
        city: str,
        state: Optional[str],
        postal_code: str,
        country: str,
        longitude: Optional[float],
        latitude: Optional[float],
        phone: Optional[str],
        website_url: Optional[str],
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"Brewery: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Location: {self.street}, {self.city}, {self.state}, "
            f"{self.postal_code}, {self.country}\n"
            f"Coordinates: ({self.latitude}, {self.longitude})\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
        )


def fetch_breweries(city: Optional[str] = None):
    url = "https://api.openbrewerydb.org/breweries"
    params = {"per_page": 20}
    if city:
        params["by_city"] = city

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch breweries.")
        return []


def main():
    parser = argparse.ArgumentParser(description="Fetch breweries information")
    parser.add_argument("--city", type=str, help="Filter breweries by city")
    args = parser.parse_args()

    breweries_data = fetch_breweries(city=args.city)
    breweries = [
        Brewery(
            id=data.get("id"),
            name=data.get("name"),
            brewery_type=data.get("brewery_type"),
            street=data.get("street"),
            city=data.get("city"),
            state=data.get("state"),
            postal_code=data.get("postal_code"),
            country=data.get("country"),
            longitude=data.get("longitude", None),
            latitude=data.get("latitude", None),
            phone=data.get("phone", None),
            website_url=data.get("website_url", None),
        )
        for data in breweries_data
    ]

    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
