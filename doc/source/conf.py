################################################################################
#   Copyright (C) 2016 Neelesh Soni <neeleshsoni03@gmail.com>, 
#   <neelesh.soni@alumni.iiserpune.ac.in>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

# -- Project information -----------------------------------------------------

import os
import sys
import pathlib

confpath = pathlib.Path(__file__).parent.resolve()

dt_root = confpath.parent.parent.resolve()

dt_src_root = os.path.join(dt_root,'Disctransformation/')

sys.path.insert(0, os.path.abspath(os.path.join(dt_src_root,'core/')))
sys.path.insert(0, os.path.abspath(os.path.join(dt_src_root,'align_axis/')))
#sys.path.insert(0, os.path.abspath(os.path.join(dt_src_root,'DTransform/')))
sys.path.insert(0, os.path.abspath(os.path.join(dt_src_root,'transform/')))
sys.path.insert(0, os.path.abspath(os.path.join(dt_src_root,'example/')))
sys.path.insert(0, os.path.abspath(dt_src_root))
sys.path.insert(0, os.path.abspath(dt_root))


project = 'DiscTransformation'
copyright = '2016, Neelesh Soni'
author = 'Neelesh Soni'
release = '2.0.0'

# -- General configuration ---------------------------------------------------

extensions = []


#extensions = ['sphinx.ext.napoleon', 'sphinx.ext.napoleon',]
extensions = [
'sphinx.ext.autodoc', 
'sphinx.ext.napoleon',
'sphinx.ext.autosummary',
#'sphinx_copybutton',
'sphinx_toggleprompt',
'sphinx_pyreverse'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
