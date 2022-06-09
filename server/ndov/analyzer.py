from gzip import GzipFile
from io import BytesIO
from bs4 import BeautifulSoup


class Analyzer:
    type = None
    xml = None

    def __init__(self, type, response):
        self.type = type
        self.xml = self.convert_to_soup(response)

    def convert_to_soup(self, response):
        with GzipFile(fileobj=BytesIO(response)) as f:
            xml_string = bytes.decode(f.read())

        return BeautifulSoup(xml_string, "xml")

    def analyze(self):
        print(self.type, self.xml)

        if self.type == "/RIG/NStreinpositiesInterface5":
            self.train_locations()

        return 1, "im an important message"

    def train_locations(self):
        locations = self.xml.findAll("TreinLocation")
        print("====================================")
        print(f"Total trains: {len(locations)}")

        for tag in locations:
            nummer = int(tag.TreinNummer.text)

            lat = tag.find("TreinMaterieelDelen").Latitude.text
            long = tag.find("TreinMaterieelDelen").Longitude.text

            print(nummer, lat, long)
