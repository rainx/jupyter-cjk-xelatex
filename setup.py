from setuptools import setup, find_packages
setup(
    name = "jupyter-cjk-xelatex",
    version = "0.2",
    packages = find_packages(),
    # scripts = ['jupyter_cjk_xelatex.py', "./console/__init__.py"],
    install_requires = ['jupyter'],

    # metadata for upload to PyPI
    author = "rainx",
    author_email = "i@rainx.cn",
    description = "Handle the encoding error for jupyter nbconvert to convert notebook to pdf document",
    license = "MIT",
    keywords = "jupyter pdf latex xelatex",
    url = "https://github.com/rainx/jupyter-cjk-xelatex",   # project home page, if any

    entry_points = {
        'console_scripts': [
            'cjk-xelatex=console:run',
            ],
        }
)
