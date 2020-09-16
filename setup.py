from setuptools import setup, find_packages


__version__ = ''
exec(open('efb_caiyun_weather_slave/__version__.py').read())

with open('README.md') as f:
    long_description = f.read()

setup(
    name='efb-caiyun-weather-slave',
    version=__version__,
    author='Sun Ziping',
    author_email='sunziping2016@gmail.com',
    description='EFB CaiYun Weather Slave Channel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sunziping2016/efb-caiyun-weather-slave',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    license='GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities"
    ],
    keywords=['ehforwarderbot', 'EH Forwarder Bot', 'EH Forwarder Bot Slave Channel',
              'weather', 'CaiYun'],
    python_requires='>=3.6',
    install_requires=[
        "ehforwarderbot>=2.0.0",
    ],
    entry_points={
        'ehforwarderbot.slave': 'hawthorn.weather = efb_caiyun_weather_slave:CaiYunWeatherSlave',
    },
)
