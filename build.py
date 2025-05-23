#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "codemao-diger-rebuild"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
    project.name = "codemao-diger-rebuild"
    project.version = "2.0.0"
    project.url = "https://github.com/Rov-Waff/codemao-diger-rebuild"
    project.license = "MIT License"
    project.depends_on('requests>=2.32')
