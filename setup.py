import setuptools



required = [
    "pandas",
    "requests"
    ]

setuptools.setup(name = 'pyinvestor',
                 version = "0.0.2",
                 description = "python wrapper for the IEX API",
                 long_description = open('README.md').read().strip(),
                 author = 'SamurAI Sarl (Fabio Capela)',
                 author_email = 'fabio.capela@samurai.team',
                 url = 'https://github.com/SamurAi-sarl/PyInvestor',
                 packages = ['PyInvestor'],
                 install_requires = required,
                 keywords = ['finance', 'trading', 'stock', 'IEX', 'API', 'market'],
                 license = 'Apache-2.0',
                 zip_safe = False)

                 
