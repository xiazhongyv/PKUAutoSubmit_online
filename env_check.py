# -*- coding: utf-8
import sys
import os


def env_check():
    if sys.version_info < (3, 6):
        raise OSError('请至少使用 Python 3.6 及以上版本，建议使用 Python 3.7 及以上版本')

    try:
        import selenium
    except ImportError:
        raise ImportError(
            '没有找到selenium包，请用pip安装一下吧～ pip3 install --user selenium')

    if not os.path.exists('config.ini'):
        raise ValueError('请先在config.sample.ini文件中填入个人信息，并将它改名为config.ini')

    print('环境检查通过')

    return


env_check()
