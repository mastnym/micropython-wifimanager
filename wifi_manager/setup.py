import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

from distutils.core import setup
setup(
  name = 'micropython-wifimanager',
  cmdclass={'sdist': sdist_upip.sdist},
  py_modules = ['wifi_manager'],
  version = '0.3.4',
  description = 'A simple network configuration utility for MicroPython on the ESP-8266 and ESP-32 boards',
  author = 'Mitchell Currie',
  author_email = 'mitch@mitchellcurrie.com',
  url = 'https://github.com/mitchins/micropython-wifimanager',
  download_url = 'https://github.com/mitchins/micropython-wifimanager/archive/0.3.4.tar.gz',
  keywords = ['micropython', 'esp8266', 'esp32', 'wifi', 'manager'],
  classifiers = [],
)
