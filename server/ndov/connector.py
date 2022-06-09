from ndov.analyzer import Analyzer

import zmq


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

HOST = "tcp://pubsub.besteffort.ndovloket.nl:7664"

# Threaded method, so we are passing the host as a parameter
def connect():
    print("[ZMQ] Starting connector\n")

    envelopes = [
        "/RIG/NStreinpositiesInterface5"
    ]

    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect(HOST)

    if len(envelopes) == 0:
        print("[ZMQ] No evenlope to subscribe on\n")
        return

    for envelope in envelopes:
        subscriber.setsockopt_string(zmq.SUBSCRIBE, envelope)
        print(f"[ZMQ] subscribed to {envelope}\n")

    while True:
        multipart = subscriber.recv_multipart()
        type = bytes.decode(multipart[0])
        response = multipart[1]

        analyzer = Analyzer(type, response)
        train, message = analyzer.analyze()

        print(train, message)