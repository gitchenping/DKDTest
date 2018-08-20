# coding=utf-8
import time
# from wap.config.Driver import driver
url="http://10.10.1.65:8083/project/list"
# driver.get(url)
time.sleep(20)


class Demo(object):

    def testfun(self):
        print "in test"
        pass

test=Demo()

class signle(object):
    driver=None

    def __new__(cls):
        if not hasattr(cls,'_instance'):
            cls._instance=object.__new__(cls)
            cls._instance.driver=Demo()
            return cls._instance
        else:
            return cls._instance


class Driver(signle):
    def getdriver(self):
        return self.driver

print dir(Driver())
Driver().getdriver()

print id(Driver())
print id(Driver())