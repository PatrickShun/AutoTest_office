from datetime import datetime

class GetName():

    def __init__(self):
        self.dateName = ''
        self.dateNameExcel = ''
        
    def getDatetime(self,basicFileName='none'):
        splitName = basicFileName.split('.')[0]
        nowtime = datetime.now()
        dataTimeName = nowtime.strftime('%Y%m%d_%H%M%S')
        self.dateName = dataTimeName
        self.dateNameExcel = 'Result_%s_%s.xlsx' % (splitName, dataTimeName)


if __name__ == '__main__':
    pass