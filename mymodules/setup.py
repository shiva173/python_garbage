from setuptools import setup

setup(
    name='vsearch',
    version='1.0',
    description='The Head First python search tools',
    author='HF Python 2e',
    py_modules=['vsearch'],
)

# для создания своего модуля создаем в папке mymodules stup.py после чего выполняем
# python setup.py sdist, cd sdist pip install module.tar