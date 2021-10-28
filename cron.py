import env_check
from crontab import CronTab
import os
import sys
import getopt


def set_crontab():
    user_cron = CronTab(user=True)
    script_path = os.path.join(os.getcwd(), 'main.py')
    job = user_cron.new(command=f'python3 {script_path}')
    try:
        exec_h = int(input('脚本需要每几小时执行一次？'))
        # TODO: 或许可以加上个检查，如果当天报过了就不再报？
    except ValueError:
        raise ValueError('emmm，输入数字就行哈')
    if not 0 < exec_h <= 24:
        raise ValueError('emmm，输得不对？ 输入范围应该是(0, 24]中的整数哦')
    job.hour.every(exec_h)
    job.enable()
    user_cron.write()


def reset_crontab():
    user_cron = CronTab(user=True)
    script_path = os.path.join(os.getcwd(), 'main.py')
    count = 0
    for job in user_cron:
        if job.command == f'python3 {script_path}':
            user_cron.remove(job)
            user_cron.write()
            count += 1

    print(f'成功清除{count}项定时任务~')


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'c')
    is_reset = False
    for cmd, arg in opts:
        if cmd == '-c':
            is_reset = True

    if is_reset:
        reset_crontab()
    else:
        set_crontab()
