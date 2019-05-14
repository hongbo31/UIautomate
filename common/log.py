import logging
import os
import time

get_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(get_path, 'log')
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log:
    def __init__(self):
        self.logname = os.path.join(log_path, time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())) + '.log')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个fileHandler，写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个streamHandler，输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warining':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    log = Log()
    log.info('--测试开始')
    log.info('操作步骤1，2，3')
    log.warning('测试结束')
    print(log.logname)