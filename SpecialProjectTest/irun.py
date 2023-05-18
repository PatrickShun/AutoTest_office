"""
主程序
=== 参数预选 ===
config_language = 'CN'
config_language = 'CT'
config_language = 'EN'
config_environment = 'TUI'
config_environment = 'APPROVAL'
config_environment = 'LIVE'
config_appkey = "CE435BCB81636B363DBDCB2F41090605" # 保时捷普通话
config_appkey = "B70618D8E8132A32D4BCD6D68EFD08E2" # Audi SOP2 普通话
config_appkey = "5DDD2B9CCD6977BDFF3E109FBFBD0E15" # Audi SOP2 粤语
congfig_suite = 'CalendarList20230517_145837.xlsx'
congfig_sheet = '西方节日'
config_suite_col = 'B'          # 仅字母
config_result_col = '4'         # 仅数字
"""


from ARequests import A_requests
from ExcelEdit import A_excelEdit
from GetDatetimeName import GetName


def running():
    # 读取配置
    config_language = 'CN'
    config_environment = 'APPROVAL'
    config_appkey = 'B70618D8E8132A32D4BCD6D68EFD08E2'
    congfig_suite = 'CalendarList.xlsx'
    congfig_sheet = '西方节日'
    config_suite_col = 'B'
    config_result_col = '4'
    result_Display = []
    # 定义保存文件的名称,用于保存log和result文件;
    iGetName = GetName()
    iGetName.getDatetime()
    # 初始化Excel对象, 准备获取测试query;
    wb = A_excelEdit(congfig_suite)
    # 读取文件,获取某Sheet的某一列所有数据,也就是query列;
    queryList = wb.readExcel(congfig_sheet, config_suite_col)
    # 获取数据后,删除第一个元素, 即标题;
    del (queryList[0])
    # 初始化请求方式,传参appkey和环境,准备请求工作;
    req = A_requests(config_appkey, config_environment)
    # 保存执行Log;
    logName = '%s_Runninglog_%s.log' % (config_language, iGetName.dateName)
    with open(logName, 'w+') as f:
        # 遍历Excel中获取到的所有query;
        for q in queryList:
            if q:
                # 如果query非空, 则发出请求, 获取内容;
                fullLog = req.posturl(q)
                # 获取后, 挨个保存到Log中
                f.write("=" * 80 + '\n')
                f.write('Queyr:' + req.r_query)
                f.write('Domain:' + req.r_domain)
                f.write('Intent:' + req.r_intent)
                f.write('Slots:' + req.r_slot + '\n')
                f.write('DisplayText:' + req.r_displayText)
                f.write('MessageID:' + req.r_messgaeid)
                f.write(str(fullLog) + '\n')
                # 把当前测试接Display加入预写列表对象,如果为空则填入null占位:
                if req.r_displayText:
                    result_Display.append(req.r_displayText)
                else:
                    result_Display.append('null')

    # 保存结果.写入Excel
    wb.writeExcel(congfig_sheet, config_result_col, result_Display)
    # 输出报告
    print('Done')


if __name__ == '__main__':
    running()
