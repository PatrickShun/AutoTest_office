"""
用于Asterix项目的Requests请求服务
"""
import requests
import json


class A_requests(object):

    def __init__(self, ExAppkey, ExEnvironment):
        self.in_appkey = ExAppkey
        if ExEnvironment == 'TUI':
            self.baseURL = "http://audi-pre.mobvoi.com/search/qa/?"
        elif ExEnvironment == 'APPROVAL':
            self.baseURL = "http://audi-pre.mobvoi.com/search/qa/?"
        elif ExEnvironment == 'LIVE':
            self.baseURL = "http://audi-pre.mobvoi.com/search/qa/?"
        else:
            raise KeyError('Environment环境参数错误,请正确选择TUI/APPROVAL/LIVE')

    def geturl(self, iquery):
        # ---GET 方式---
        data = {
            "query": iquery,
            "appkey": self.in_appkey,
            "version": "40000",
            "address": "中国,北京市,北京市,朝阳区,北京市朝阳区惠新东街,14号,39.979515,116.424273",
            "output": "lite"
        }
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(self.baseURL, params=data, headers=headers)
        res.encoding = "utf-8"
        html = res.text
        rDict = json.loads(html)
        print("=" * 50)
        print("Query:", rDict["query"])
        print("Domain:", rDict["domain"])
        print("Display:", rDict["languageOutput"]["displayText"])
        print("MessageId", rDict["messageId"])
        print("=" * 50, "\n")
        return rDict

    def posturl(self, iquery):
        # ---POST 方式---
        params = {
            'address': "中国,北京市,北京市,朝阳区,北京市朝阳区惠新东街,14号,39.979515,116.424273",
            'search_type': 'global',
            'output': 'lite',
            "appkey": self.in_appkey,
            'query': iquery,
            'qa_control_param': {
                'data': {
                    'persist': {
                        'isSupportMediaSessionControl': 'true',
                        'build_up_type': 'FAWVW_FBU',
                        'clu_version': '3B',
                        'has_mib3_map': 'true',
                        'enable_indomain': 'true',
                        'is_gas_car': 'true',
                        'cancel_indomain': 'true',
                        'asterix_map': 'mib3'}}}}
        payload = str(params).encode('utf-8')
        headers = {'content-type': "application/json",
                   'cache-control': "no-cache"}
        res = requests.request("POST", self.baseURL,
                               data=payload, headers=headers)
        # print(res.headers)
        # print(res.status_code)
        rDict = json.loads(res.text)
        # print(rDict)
        self.r_query = rDict['hypotheses'][0]['query'] + '\n'
        self.r_domain = rDict['hypotheses'][0]['states']['semantic']['domain'] + '\n'
        self.r_intent = rDict['hypotheses'][0]['states']['semantic']['intent'] + '\n'
        self.r_slot = json.dumps(rDict['hypotheses'][0]['states']['semantic']['slots'],
                                 sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
        self.r_displayText = rDict['hypotheses'][0]["languageOutput"]["displayText"] + '\n'
        self.r_messgaeid = rDict['hypotheses'][0]["messageId"] + '\n'
        print("=" * 80)
        print("Query:", self.r_query)
        print("Domain:", self.r_domain)
        print("Intent:", self.r_intent)
        print("Slots:", self.r_slot)
        print("Display:", self.r_displayText)
        print("MessageId:", self.r_messgaeid)
        print("=" * 80, "\n")
        return rDict


if __name__ == '__main__':
    irun = A_requests('B70618D8E8132A32D4BCD6D68EFD08E2', 'TUI')
    irun.posturl('最近的双色球中奖结果')
