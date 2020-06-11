# This file was automatically generated by Shore. Do not edit manually.
# For more information on Shore see https://pypi.org/project/nr.shore/

from __future__ import print_function
import io
import os
import re
import setuptools
import sys

with io.open('src/docspec_python/__init__.py', encoding='utf8') as fp:
  version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

readme_file = 'README.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = ['docspec >=0.1.0,<0.2.0', 'nr.sumtype >=0.0.3,<0.1.0']

setuptools.setup(
  name = 'docspec-python',
  version = version,
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'A parser based on LibCST producing docspec data from Python source code.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = None,
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = None, # TODO: '>=3.5,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'docspec-python = docspec_python.__main__:main',
    ]
  },
  cmdclass = {},
  keywords = [],
  classifiers = [],
)
