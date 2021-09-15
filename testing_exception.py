import requests

url = "https://posduga.sysable.io/api/sendjsondata"
imei =  "088298203829"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
def kirim_data(data,img):
    
    data_fix = {"foto_cam":img,"ketinggian_air":data,"imei":imei}
    
    r = requests.post(url, data=json.dumps(data_fix), headers=headers)
    r.close()
    return r

data = 123
img = " "
kirim_data(data,img)