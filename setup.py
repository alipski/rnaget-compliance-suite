import setuptools

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

with open("README.md", "r") as fh:
    long_description = fh.read()
install_requires = ['requests', 'click', 'jsonschema', 'PyYAML', "Jinja2"]


setuptools.setup(
    name="rnaget-compliance",
    version="1.0.0",
    author="Sean Upchurch",
    author_email="sau@caltech.edu",
    description="A compliance utility reporting system for rnaget server implementations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ga4gh-rnaseq/rnaget-compliance-suite",
    package_data={'': ['web/*']},
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        rnaget-compliance=compliance_suite.cli:main
    ''',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
