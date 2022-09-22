import requests


class IcasKPM():

    def __init__(self):
        self.vwmJiraID = []


    def postGetURL(self):

        data = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "seraph.rememberme.cookie=27938%3A96f69fba12150a7e66d11b12f8c091cb872fceff; JSESSIONID=314A0785906F04585FFBAE20545DEF70; atlassian.xsrf.token=B6VW-6ZIG-SH3J-D7SH_fd1a6b91817cc08ea21e0c0985ebc6ec2b463cd2_lin",
                "Host": "10.2.0.248:8080",
                "Upgrade-Insecure-Requests": "1"
                }
                
        baseURL = 'http://10.2.0.248:8080/issues/?jql=project = IDS3 AND text ~ '+ '"9048547"' + 'order by created DESC'
        headers = {"User-Agent":"Mozilla/5.0"}
        res = requests.get(baseURL,params=data,headers=headers)
        res.encoding = "utf-8"
        html = res.text

        print(html)



    def runTest(self):
        self.postGetURL()



if __name__ == "__main__":
    myRun = IcasKPM()
    # myRun.runTest()

# http://10.2.0.248:8080/issues/?jql=project = IDS3 AND text ~ "9048547" order by created DESC