class Parser:
    type = None
    xml = None

    def __init__(self, type, xml):
        self.type = type
        self.xml = xml

    def parse(self):
        if self.type == "/RIG/NStreinpositiesInterface5":
            self.ParseTrainLocations()


    def ParseTrainLocations(self):
        treinLocations = self.xml.findAll("TreinLocation")
        print("====================================")
        print(f"Total trains: {len(treinLocations)}")

        for tag in treinLocations:
            nummer = int(tag.TreinNummer.text)

            # if nummer != 2451:
            #     continue

            lat = tag.find("TreinMaterieelDelen").Latitude.text
            long = tag.find("TreinMaterieelDelen").Longitude.text

            print(nummer, lat, long)
