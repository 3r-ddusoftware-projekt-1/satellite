import urequests

def send_datapoints(datapoints):
    base = "https://example.org/"
    url = base + "/api/upload_data"
    data = {"datapoints": datapoints}

    rsp = urequests.post(url, json=data)
    rsp_parsed = response.json()

    if not rsp_parsed.get("success", False):
        pass # TODO

    rsp.close()
