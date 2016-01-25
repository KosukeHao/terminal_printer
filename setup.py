# coding=utf8
__author__ = 'hellflame'

from setuptools import setup, find_packages

with open('README') as f:
    long_desc = f.read()

setup(
    name='TerminalPrinter',
    version='0.9.6',
    keywords=('text printer', 'picture printer', 'picture in terminal', 'print picture in terminal'),
    description="文字,字符,图片终端打印, print something in terminal",
    long_description=long_desc,
    license='MIT',
    author='hellflame',
    author_email='hellflamedly@gmail.com',
    url='https://github.com/hellflame/terminal_printer',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7'
    ],
    include_package_data=True,
    package_data={
        'fonts': [
            'fonts/DejaVuSansMono-Bold.ttf',
            'fonts/fengyun.ttf',
            'fonts/handstd_h.otf',
            'fonts/huakangbold.otf',
            'fonts/letter.ttf',
            'fonts/shuyan.ttf'
        ]
    },
    install_requires=[
        'Pillow'
    ],
    platforms="linux, Mac Os",
    entry_points={
        'console_scripts': [
            'terminalprint=terminal_printer.terminal_printer:main'
        ]
    }
)


