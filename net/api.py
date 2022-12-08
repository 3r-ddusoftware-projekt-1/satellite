import urequests

def send_datapoints(datapoint, url_base):
    url = url_base + "/api/upload_data"
    data = datapoint

    rsp = urequests.post(url, json=data)
    rsp_parsed = response.json()

    if not rsp_parsed.get("success", False):
        pass # TODO

    rsp.close()
