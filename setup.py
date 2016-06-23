from setuptools import setup, find_packages
setup(
    name = "jupyter_cjk_xelatex",
    version = "0.1",
    packages = find_packages(),
    scripts = ['jupyter_cjk_xelatex.py'],
    install_requires = ['jupyter'],

    # metadata for upload to PyPI
    author = "RainX",
    author_email = "i@rainx.cn",
    description = "jupyter-cjk-xelatex",
    license = "PSF",
    keywords = "jupyter pdf latex xelatex",
    url = "https://github.com/rainx/jupyter-cjk-xelatex",   # project home page, if any

    entry_points = {
        'console_scripts': [
            'cjk-xelatex=jupyter_cjk_xelatex.console:run',
            ],
        }
)
