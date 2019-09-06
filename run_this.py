import os
import smtplib
import time
import itchat
import unittest
from BeautifulReport import BeautifulReport
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.logger import Log, report_path
# from common.HTMLTestRunnerCN import HTMLTestRunner
from common import read_config

now = time.strftime('%Y-%m-%d %H-%M-%S')


def add_case(case_path):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)  # 定义discover方法的参数
    Log().info('测试用例：%s' % discover)
    # HTMLTestRunner
    # testUnit = unittest.TestSuite()
    # discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         testUnit.addTests(test_case)
    # return testUnit

    # BeautifulReport
    return discover


def run_case(all_case, report_path):
    """执行所有测试用例，并把结果写入报告"""
    # HTMLTestRunner
    # report_abspath = os.path.join(report_path, now + 'report.html')
    # fp = open(report_abspath, 'wb')
    # runner = HTMLTestRunner(stream=fp, verbosity=2, title=read_config.title, description='用例执行情况：')
    # runner.run(all_case)  # 调用add_case函数返回值

    # BeautifulReport
    result = BeautifulReport(all_case)
    result.report(filename=now + 'report.html', description=read_config.title, log_path=report_path)
    Log().info('执行用例，生成HTML报告!')


def get_new_report_html(report_path_html):
    """获取最新的测试报告"""
    lists = os.listdir(report_path_html)
    for file_name in lists:
        if os.path.splitext(file_name)[1] == '.html':
            continue
        else:
            lists.remove(file_name)
    lists.sort(key=lambda a: os.path.getmtime(os.path.join(report_path_html, a)))
    Log().info('最新的测试报告是：%s' % lists[-1])
    report_file_html = os.path.join(report_path_html, lists[-1])  # 找到最新的测试报告文件
    return report_file_html


def get_new_report_excel(report_path_excel):
    """获取最新的测试报告"""
    lists = os.listdir(report_path_excel)
    for file_name in lists:
        if os.path.splitext(file_name)[1] == '.xlsx':
            continue
        else:
            lists.remove(file_name)
    lists.sort(key=lambda a: os.path.getmtime(os.path.join(report_path_excel, a)))
    Log().info('最新的测试报告是：%s' % lists[-1])
    report_file_excel = os.path.join(report_path_excel, lists[-1])  # 找到最新的测试报告文件
    return report_file_excel


def send_email(user, pwd, user_163, pwd_163, _to, smtp_service, smtp_service_163, report_file):
    """发送邮件"""
    msg = MIMEMultipart()
    msg['Subject'] = read_config.title
    msg['from'] = user
    msg['to'] = ';'.join(_to)  # 支持多个收件人
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"
    # 邮件正文
    part = MIMEText('{} UI自动化测试完成，测试报告见附件，请注意查看...'.format(read_config.title))
    if os.path.splitext(report_file)[1] == '.html':
        # with open(report_file, 'rb') as f:
        #     mail_body = f.read()
        # body = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(part)
        Log().info('写入邮件正文')
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 添加多个附件
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attach;filename=' + report_file[-11:]
    msg.attach(att)
    Log().info('添加邮件附件')
    try:
        try:
            s = smtplib.SMTP()
            s.connect(smtp_service_163)
            s.login(user_163, pwd_163)
            s.sendmail(user_163, _to, msg.as_string())
            s.quit()
            Log().info('%s账号邮件发送成功！请通知相关人员查收。\n' % user_163)
        except:
            s = smtplib.SMTP_SSL(smtp_service)
            s.login(user, pwd)
            s.sendmail(user, _to, msg.as_string())
            s.quit()
            Log().info('%s账号邮件发送成功！请通知相关人员查收。\n' % user)
    except smtplib.SMTPException as e:
        Log().info('邮件发送失败的原因是：%s \n' % e)


def send_wx():
    """发送微信消息提醒"""
    wx_name_list = read_config.wx_name.split(',')
    for wx_name in wx_name_list:
        name = itchat.search_friends(name=wx_name)
        if not name:
            name = itchat.search_chatrooms(name=wx_name)
            msg = '{} UI自动化测试完成，测试报告已发送到各位的邮箱，请下载后查看...'.format(read_config.title)
        else:
            msg = '{} UI自动化测试完成，测试报告已发送到您的邮箱，请下载后查看...'.format(read_config.title)
        if name:
            username = name[0]['UserName']
            itchat.send(msg, username)
            Log().info('微信：{}，提示信息发送成功.'.format(wx_name))


def run_email():
    # itchat.auto_login(hotReload=True)
    # 测试用例路径，匹配规则
    case_path = os.path.abspath(os.path.dirname(__file__)) + '\\case'
    all_case = add_case(case_path)
    # 生成报告测试路径
    run_case(all_case, report_path)
    # 获取最新的测试报告
    report_file_html = get_new_report_html(report_path)
    send_wx()  # 发送微信信息
    user = read_config.user
    # qq邮箱授权码
    pwd = read_config.pwd
    user_163 = read_config.user_163
    # 163邮箱授权码
    pwd_163 = read_config.pwd_163
    # _to = ['18701137212@163.com','liyongfeng@xxbmm.com','954274592@qq.com']
    _to = read_config.to.split(',')
    smtp_service = read_config.smtp_service
    smtp_service_163 = read_config.smtp_service_163
    send_email(user, pwd, user_163, pwd_163, _to, smtp_service, smtp_service_163, report_file_html)


if __name__ == '__main__':
    run_email()
