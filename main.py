# -*- coding: utf-8
from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from argparse import ArgumentParser
import re
from urllib.parse import quote
from urllib import request
import os
import sys
import time
import warnings
import json

warnings.filterwarnings('ignore')


def dropdown_handler(driver, xpath: str):
    """
    点击带有滚动条的菜单
    ref: https://stackoverflow.com/questions/57303355
    """
    wait = WebDriverWait(driver, 10)
    ele = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    ele.location_once_scrolled_into_view
    ele.click()
    time.sleep(0.1)


def login(driver, userName, password, retry=0):
    if retry == 3:
        raise Exception('门户登录失败')

    print('门户登陆中...')

    appID = 'portal2017'
    iaaaUrl = 'https://iaaa.pku.edu.cn/iaaa/oauth.jsp'
    appName = quote('北京大学校内信息门户新版')
    redirectUrl = 'https://portal.pku.edu.cn/portal2017/ssoLogin.do'

    driver.get('https://portal.pku.edu.cn/portal2017/')
    driver.get(
        f'{iaaaUrl}?appID={appID}&appName={appName}&redirectUrl={redirectUrl}')
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'logon_button')))
    driver.find_element_by_id('user_name').send_keys(userName)
    time.sleep(0.1)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(0.1)
    driver.find_element_by_id('logon_button').click()
    try:
        WebDriverWait(driver,
                      10).until(EC.visibility_of_element_located((By.ID, 'all')))
        print('门户登录成功！')
    except:
        print('Retrying...')
        login(driver, userName, password, retry + 1)


def go_to_simso(driver):
    button = driver.find_element_by_id('all')
    driver.execute_script("$(arguments[0]).click()", button)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'tag_s_stuCampusExEnReq')))
    driver.find_element_by_id('tag_s_stuCampusExEnReq').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'el-card__body')))


def go_to_application_out(driver):
    go_to_simso(driver)
    driver.find_element_by_class_name('el-card__body').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))


def go_to_application_in(driver, userName, password):
    driver.back()
    time.sleep(0.5)
    driver.back()
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-card__body')))
        time.sleep(0.5)
        driver.find_element_by_class_name('el-card__body').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))
    except:
        print('检测到会话失效，重新登陆中...')
        login(driver, userName, password)
        go_to_simso(driver)
        driver.find_element_by_class_name('el-card__body').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))


def select_in_out(driver, way):
    driver.find_element_by_class_name('el-select').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{way}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{way}"]').click()


def select_campus(driver, campus):
    driver.find_elements_by_class_name('el-select')[1].click()
    dropdown_handler(driver, f'//li/span[text()="{campus}"]')


def write_reason(driver, reason):
    driver.find_elements_by_class_name('el-select')[2].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{reason}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{reason}"]').click()


def select_destination(driver, destination):
    driver.find_elements_by_class_name('el-select')[3].click()
    dropdown_handler(driver, f'//li/span[text()="{destination}"]')


def select_district(driver, district):
    driver.find_elements_by_class_name('el-select')[4].click()
    dropdown_handler(driver, xpath=f'//li/span[text()="{district}"]')


def write_mail_address(driver, mail_address):
    driver.find_elements_by_class_name('el-input__inner')[2].clear()
    driver.find_elements_by_class_name('el-input__inner')[2].send_keys(
        f'{mail_address}')
    time.sleep(0.1)


def write_phone_number(driver, phone_number):
    driver.find_elements_by_class_name('el-input__inner')[3].clear()
    driver.find_elements_by_class_name('el-input__inner')[3].send_keys(
        f'{phone_number}')
    time.sleep(0.1)


def write_reason_detail(driver, detail):
    driver.find_element_by_class_name('el-textarea__inner').send_keys(
        f'{detail}')
    time.sleep(0.1)


def write_track(driver, track):
    driver.find_elements_by_class_name('el-textarea__inner')[1].send_keys(
        f'{track}')
    time.sleep(0.1)


def write_street(driver, street):
    driver.find_elements_by_class_name('el-textarea__inner')[1].send_keys(
        f'{street}')
    time.sleep(0.1)


def click_check(driver):
    driver.find_element_by_class_name('el-checkbox__label').click()
    time.sleep(0.1)


def click_inPeking(driver):
    driver.find_element_by_class_name('el-radio__inner').click()
    time.sleep(0.1)


def submit(driver):
    driver.find_element_by_xpath(
        '//button/span[contains(text(),"保存")]').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '(//button/span[contains(text(),"提交")])[3]')))
    driver.find_element_by_xpath(
        '(//button/span[contains(text(),"提交")])[3]').click()
    time.sleep(0.1)


def fill_out(driver, campus, mail_address, phone_number, reason, detail, destination, track):
    print('开始填报出校备案')
    print('选择出校/入校    ', end='')
    select_in_out(driver, '出校')
    print('选择校区    ', end='')
    select_campus(driver, campus)
    print('填写邮箱    ', end='')
    write_mail_address(driver, mail_address)
    print('填写手机号    ', end='')
    write_phone_number(driver, phone_number)
    print('填写出入校事由    ', end='')
    write_reason(driver, reason)
    print('填写出入校事由详细描述    ', end='')
    write_reason_detail(driver, detail)
    print('选择出校目的地    ', end='')
    select_destination(driver, destination)
    print('填写出校行动轨迹    ', end='')
    write_track(driver, track)
    click_check(driver)
    submit(driver)
    print('出校备案填报完毕！')


def fill_in(driver, campus, mail_address, phone_number, reason, detail, habitation, district, street):
    print('开始填报入校备案')
    print('选择出校/入校    ', end='')
    select_in_out(driver, '入校')
    print('选择校区    ', end='')
    select_campus(driver, campus)
    print('填写邮箱    ', end='')
    write_mail_address(driver, mail_address)
    print('填写手机号    ', end='')
    write_phone_number(driver, phone_number)
    print('填写出入校事由    ', end='')
    write_reason(driver, reason)
    print('填写出入校事由详细描述    ', end='')
    write_reason_detail(driver, detail)
    if habitation != '北京':
        raise Exception('暂不支持京外入校备案，请手动填写')
    print('选择居住地所在区    ', end='')
    select_district(driver, district)
    print('填写居住地所在街道    ', end='')
    write_street(driver, street)
    click_inPeking(driver)
    click_check(driver)
    submit(driver)
    print('入校备案填报完毕！')


def wechat_notification_success(userName, sckey):
    with request.urlopen(
            quote('https://sctapi.ftqq.com/' + sckey + '.send?title=成功报备&desp=学号' +
                  str(userName) + '成功报备',
                  safe='/:?=&')) as response:
        response = json.loads(response.read().decode('utf-8'))


def wechat_notification_failed(userName, sckey):
    with request.urlopen(
            quote('https://sctapi.ftqq.com/' + sckey + '.send?title=[请注意]报备失败&desp=学号' +
                  str(userName) + '报备失败，需要您手动报备或在github页面手动重新运行，您可以在主仓库issue下报告错误日志。',
                  safe='/:?=&')) as response:
        response = json.loads(response.read().decode('utf-8'))


def exception_printer(e: Exception or None):
    print_bold = lambda x: print('\033[1;31m' + x + '\033[0m', file=sys.stderr)
    print_bold("多次重试失败，报备失败")
    print_bold('请检查您的配置是否正确，或者稍后重试')
    print_bold('如果错误依然存在，请在这里汇报Bug：https://github.com/xiazhongyv/PKUAutoSubmit_online/issues')
    print_bold('错误详细信息：')
    raise e


def run(driver, userName, password, campus, mail_address, phone_number, reason, detail, destination, track,
        habitation, district, street, wechat, sckey):

    for try_times in range(5):
        try:
            print("======= 第", try_times + 1, "次报备尝试 =======")
            login(driver, userName, password)
            go_to_application_out(driver)
            fill_out(driver, campus, mail_address, phone_number, reason, detail, destination, track)
            go_to_application_in(driver, userName, password)
            fill_in(driver, campus, mail_address, phone_number, reason, detail, habitation, district, street)
            print('\n报备成功')
            break

        except Exception as e:
            print("\n报备失败")
            if try_times == 4:
                if wechat:
                    wechat_notification_failed(userName, sckey)
                exception_printer(e)

    if wechat:
        wechat_notification_success(userName, sckey)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--ID', type=str)
    parser.add_argument('--PASSWORD', type=str)
    parser.add_argument('--MAIL_ADDRESS', type=str)
    parser.add_argument('--PHONE_NUMBER', type=str)
    parser.add_argument('--SENDKEY', type=str)
    argconf = parser.parse_args()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_pjs = webdriver.Edge(
        options=chrome_options,
        executable_path='/usr/bin/chromedriver',
        service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    print('Driver Launched\n')

    conf = ConfigParser()
    conf.read("config.ini", encoding='utf8')

    campus, reason, detail = dict(conf['common']).values()
    destination, track = dict(conf['out']).values()
    habitation, district, street = dict(conf['in']).values()
    wechat = conf.getboolean('wechat', '是否需要微信通知')

    run(driver_pjs, argconf.ID, argconf.PASSWORD, campus, argconf.MAIL_ADDRESS, argconf.PHONE_NUMBER, reason, detail,
        destination, track, habitation, district, street, wechat, argconf.SENDKEY)

    driver_pjs.quit()
