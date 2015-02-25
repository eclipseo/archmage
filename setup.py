#!/usr/bin/env python

from setuptools import setup

setup(
    name = "archmage",
    fullname = "arCHMage",
    version = "0.2.4",
    description = "CHM(Compiled HTML) Decompressor",
    maintainer = "Basil Shubin",
    maintainer_email = "bashu@users.sourceforge.net",
    author = "Eugeny Korekin",
    author_email = "az@ftc.ru",
    url = "archmage.sf.net",
    license = "GPL",
    keywords = ["chm", "HTML Help", "Compiled HTML", "Compressed HTML"],
    long_description = "arCHMage is an extensible reader and decompiler for files in the CHM format. arCHMage is written in the Python programming language and uses PyCHM - python bindings for CHMLIB from GnoCHM project.",
    py_modules = ["archmod.CHM", "archmod.CHMParser", "archmod.CHMServer", "archmod.Cached", "archmod.mod_chm", "archmod.chmtotext", "archmod.htmldoc"],
    entry_points={
        'console_scripts': ['archmage = archmod.cli:main'],
    },
    data_files = [("/etc/archmage", ["arch.conf"]),
                  ("share/man/man1", ["archmage.1.gz"]),
                  ("share/archmage/templates",
                   ["templates/arch_contents.html",
                    "templates/arch_frameset.html",
                    "templates/arch_header.html",
                    "templates/index.html",
                    "templates/arch_css.css"]),
                  ("share/archmage/templates/icons",
                   ["templates/icons/next.gif",
                    "templates/icons/0.gif",
                    "templates/icons/1.gif",
                    "templates/icons/11.gif",
                    "templates/icons/12.gif",
                    "templates/icons/17.gif",
                    "templates/icons/2.gif",
                    "templates/icons/22.gif",
                    "templates/icons/90.gif",
                    "templates/icons/91.gif",
                    "templates/icons/92.gif",
                    "templates/icons/93.gif",
                    "templates/icons/94.gif",
                    "templates/icons/95.gif",
                    "templates/icons/96.gif",
                    "templates/icons/97.gif",
                    "templates/icons/98.gif",
                    "templates/icons/99.gif",
                    "templates/icons/10.gif",
                    "templates/icons/prev.gif",
                    "templates/icons/13.gif",
                    "templates/icons/14.gif",
                    "templates/icons/15.gif",
                    "templates/icons/16.gif",
                    "templates/icons/18.gif",
                    "templates/icons/19.gif",
                    "templates/icons/20.gif",
                    "templates/icons/21.gif",
                    "templates/icons/23.gif",
                    "templates/icons/24.gif",
                    "templates/icons/25.gif",
                    "templates/icons/26.gif",
                    "templates/icons/27.gif",
                    "templates/icons/35.gif",
                    "templates/icons/37.gif",
                    "templates/icons/39.gif",
                    "templates/icons/3.gif",
                    "templates/icons/4.gif",
                    "templates/icons/5.gif",
                    "templates/icons/6.gif",
                    "templates/icons/7.gif",
                    "templates/icons/8.gif",
                    "templates/icons/9.gif"])]
)
