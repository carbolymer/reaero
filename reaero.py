#!/usr/bin/python
import pycurl as pc
from io import BytesIO


class ReAero(object):
    # XHTMLRequest Headers
    headers = ['X-Requested-With: XMLHttpRequest']

    # user agent
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'

    def set_manual_connection(self):
        form_data = '<?xml version="1.0" encoding="UTF-8"?><request>' \
                    '<RoamAutoConnectEnable>1</RoamAutoConnectEnable>' \
                    '<AutoReconnect>0</AutoReconnect>' \
                    '<ReconnectInterval>0</ReconnectInterval>' \
                    '<MaxIdelTime>600</MaxIdelTime>' \
                    '<ConnectMode>1</ConnectMode></request>'
        self.submit_connection_settings(form_data)

    def set_auto_connection(self):
        form_data = '<?xml version="1.0" encoding="UTF-8"?><request>' \
                    '<RoamAutoConnectEnable>1</RoamAutoConnectEnable>' \
                    '<AutoReconnect>0</AutoReconnect>' \
                    '<ReconnectInterval>0</ReconnectInterval>' \
                    '<MaxIdelTime>600</MaxIdelTime>' \
                    '<ConnectMode>2</ConnectMode></request>'
        self.submit_connection_settings(form_data)

    def submit_connection_settings(self, form_data):
        buffer = BytesIO()

        # curl init
        c = pc.Curl()

        c.setopt(pc.URL, 'http://192.168.1.1/api/dialup/connection')
        c.setopt(pc.WRITEDATA, buffer)
        c.setopt(pc.REFERER, 'http://192.168.1.1/html/mobileconnection.html')
        c.setopt(pc.HEADER, True)
        c.setopt(pc.HTTPHEADER, self.headers)
        c.setopt(pc.USERAGENT, self.user_agent)
        c.setopt(pc.POSTFIELDS, form_data)
        c.perform()
        c.close()

        # body = buffer.getvalue()
        # print(body)

if __name__ == "__main__":
    reaero = ReAero()
    # setting manual connection disconnects device from the network
    reaero.set_manual_connection()
    # setting auto connection connects it again
    reaero.set_auto_connection()
    # IT DOES NOT REQUIRE ADMIN PASSWORD TO CHANGE SETTINGS, LMAO! @_@
    # https://www.kb.cert.org/vuls/id/871148
