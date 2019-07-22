import requests;
import json;
import xml.etree.ElementTree as ET;

if __name__ == "__main__":
    session = requests.session();

    data = session.get("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionCountry");
    # jsons = json.loads(data.text);
    # body={"username":"niuhanyang","passwd":"aA123456"};
    # headers = "{'content-type': 'application/json'}";

    # respone = requests.post("http://api.nnzhp.cn/api/user/login",json.dumps(body),headers=headers);
    etree = ET.fromstring(data.text);
    print(etree.tag);

    print(etree.getchildren()[1].text);
    