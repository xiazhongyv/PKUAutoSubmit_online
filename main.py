# -*- coding: utf-8
from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options
from argparse import ArgumentParser
from func import *
import warnings
import sys
import os
import re
warnings.filterwarnings('ignore')


def go(config):
    conf = ConfigParser()
    conf.read(config, encoding='utf8')

    campus, reason, detail = dict(conf['common']).values()
    destination, track = dict(conf['out']).values()
    habitation, district, street = dict(conf['in']).values()
    capture = conf.getboolean('capture', '是否需要备案历史截图')
    path = conf['capture']['截图保存路径']
    wechat = conf.getboolean('wechat', '是否需要微信通知')

    run(driver_pjs, argconf.ID, argconf.PASSWORD, campus, argconf.MAIL_ADDRESS, argconf.PHONE_NUMBER, reason, detail, destination, track,
        habitation, district, street, capture, path, wechat, argconf.SENDKEY)


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

    go('config.ini')

    driver_pjs.quit()
