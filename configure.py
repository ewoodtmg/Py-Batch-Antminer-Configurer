# Copyright 2020 Navier, Inc
#Original Written by David Steinberg
#Modified by Erik Wood
import re, requests
from requests.auth import HTTPDigestAuth
import pprint

username = "root"
#Replace $PASS with your machine password
password = "$PASS"

pp = pprint.PrettyPrinter(indent=4)


def get_miner_config(ip):
    session = requests.session()

    response = session.get(
        "http://%s/cgi-bin/minerConfiguration.cgi" % ip,
        auth=HTTPDigestAuth(username, password),
        timeout=5,
    )

    # bitmain-nobeeper
    # bitmain-notempoverctrl

    payload = {
        "_ant_pool1url": re.findall('"url" : "(.*)"', response.text, re.MULTILINE)[0],
        "_ant_pool1user": re.findall('"user" : "(.*)"', response.text, re.MULTILINE)[0],
        "_ant_pool1pw": re.findall('"pass" : "(.*)"', response.text, re.MULTILINE)[0],
        "_ant_pool2url": re.findall('"url" : "(.*)"', response.text, re.MULTILINE)[1],
        "_ant_pool2user": re.findall('"user" : "(.*)"', response.text, re.MULTILINE)[1],
        "_ant_pool2pw": re.findall('"pass" : "(.*)"', response.text, re.MULTILINE)[1],
        "_ant_pool3url": re.findall('"url" : "(.*)"', response.text, re.MULTILINE)[2],
        "_ant_pool3user": re.findall('"user" : "(.*)"', response.text, re.MULTILINE)[2],
        "_ant_pool3pw": re.findall('"pass" : "(.*)"', response.text, re.MULTILINE)[1],
        "_ant_nobeeper": False,
        "_ant_notempoverctrl": False,
        "_ant_fan_customize_switch": False,
        "_ant_fan_customize_value": None,
        "_ant_freq": int(
            re.search('"bitmain-freq" : "(\d+)"', response.text, re.MULTILINE).groups()[
                0
            ]
        ),
        "_ant_voltage": int(
            re.search(
                '"bitmain-voltage" : "(\d+)"', response.text, re.MULTILINE
            ).groups()[0]
        ),
        "_ant_work_mode": int(
            re.search(
                '"bitmain-work-mode" : "(\d+)"', response.text, re.MULTILINE
            ).groups()[0]
        ),
    }
    pp.pprint(payload)

#Replace $IP with IP of the machine
get_miner_config("$IP")
