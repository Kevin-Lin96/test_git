import requests

class TestSendRequest:
  def  test_post_andonInfo(self):
    # 发送post请求
    url = "http://www.67934.cn:30702/superlink/api/andonInfo/create/andonInfo"
    data = {
        "andonPc": {
          "areaName": "string",
          "areaToken": "string",
          "bindDevice": [
            {
              "bindDeviceName": "string",
              "bindDeviceToken": "string"
            }
          ],
          "bindProcessName": "string",
          "bindProcessNumber": "string",
          "createdBy": "string",
          "createdDate": "2022-11-05T04:45:13.949Z",
          "id": "string",
          "ip": "string",
          "metadata": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
          },
          "pcCode": "string",
          "pcName": "string",
          "token": "string",
          "updatedBy": "string",
          "updatedDate": "2022-11-05T04:45:13.949Z"
        },
        "andonPcName": "string",
        "andonProject": "string",
        "andonSet": {
          "createdBy": "string",
          "createdDate": "2022-11-05T04:45:13.949Z",
          "describe": "string",
          "iconUrl": "string",
          "id": "string",
          "metadata": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
          },
          "project": "string",
          "state": "string",
          "token": "string",
          "updatedBy": "string",
          "updatedDate": "2022-11-05T04:45:13.949Z"
        },
        "andonSetId": "string",
        "callPersonId": "string",
        "callPersonName": "string",
        "callTime": "2022-11-05T04:45:13.949Z",
        "comment": "string",
        "completeId": "string",
        "completeName": "string",
        "completeOpinion": "string",
        "completeTime": "2022-11-05T04:45:13.949Z",
        "icon": "string",
        "metadata": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "pcId": "string",
        "problemCode": "string",
        "problemOpinion": "string",
        "responseOpinion": "string",
        "responsePersonId": "string",
        "responsePersonName": "string",
        "responseTime": "2022-11-05T04:45:13.950Z",
        "status": "string",
        "token": "string"
      }
    rep = requests.post(url=url, json=data)
    print(rep.json())





