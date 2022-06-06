from gzip import GzipFile
from io import BytesIO
from bs4 import BeautifulSoup
from parser import Parser

import zmq

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://pubsub.besteffort.ndovloket.nl:7664")

"""
/RIG/InfoPlusDVSInterface4              PutReisInformatieBoodschapIn
/RIG/InfoPlusPILInterface5              ??? takes too long
/RIG/InfoPlusPISInterface5              Contains old failures (hour old data)
/RIG/InfoPlusVTBLInterface5             Vrije TekstBericht Landeli
/RIG/InfoPlusVTBSInterface5             Vrije TekstBericht Station
/RIG/NStreinpositiesInterface5          Contains all active trains + locations, speed, etc
/RIG/InfoPlusRITInterface2              Contains old data from a hour ish ago
"""

"""
TODO: 
    

"""
# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusPITInterface5")

# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusDVSInterface4")
# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusPILInterface5")
# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusPISInterface5")
# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusVTBLInterface5")
# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusVTBSInterface5")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/NStreinpositiesInterface5")
# subscriber.setsockopt_string(zmq.SUBSCRIBE, "/RIG/InfoPlusRITInterface2")


def convertToSoup(response):
    with GzipFile(fileobj=BytesIO(response)) as f:
        xmlString = bytes.decode(f.read())

    return BeautifulSoup(xmlString, "xml")

print("Subcribed")
while True:
    # Setup variables we are going to need
    multipart = subscriber.recv_multipart()
    type = bytes.decode(multipart[0])
    response = multipart[1]

    xml = convertToSoup(response)

    # print(type, xml)
    parser = Parser(type, xml)
    parser.parse()