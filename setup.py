#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'codemao-diger-rebuild',
        version = '2.0.1',
        description = '',
        long_description = '# ⚡ 猫站洛阳铲 ⚡\n\n一个自动化在编程猫论坛挖坟的工具，当然也可以作为一个包导入到您的项目中\n\n![GitHub last commit](https://img.shields.io/github/last-commit/Rov-Waff/codemao-diger-rebuild)\n\n![PyPI - Version](https://img.shields.io/pypi/v/codemao-diger-rebuild)\n\n![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.codemao.cn%2Fweb%2Fforums%2Fposts%2F1630334%2Fdetails&query=n_views&label=%E7%8C%AB%E7%AB%99%E7%A4%BE%E5%8C%BA)\n\n![GitHub Repo stars](https://img.shields.io/github/stars/Rov-Waff/codemao-diger-rebuild)\n\n## 安装\n\n### 通过pip安装\n\n``````shell\npip install codemao-diger-rebuild\n``````\n\n### 通过源码安装\n\n```shell\ngit clone git@github.com:Rov-Waff/codemao-diger-rebuild.git\ncd codemao-diger-rebuild\npython3 setup.py install\n```\n\n## 命令行使用\n\n你可以运行这个包提供的一些Model以在猫站挖坟\n\n### 生成帖子数据库\n\n运行`codemao_diger.DBGenerator`这个Model可以生成存储帖子数据用的数据库，用法如下：\n\n```shell\npython3 -m codemao_diger.DBGenerator [数据库URL]\n```\n\n表结构请参考[文档](#)（没写好）\n\n### 自动化挖坟\n\n运行`codemao_diger.requester`这个Model可以自动化请求猫站API获取帖子数据，并将其存在指定数据库中，用法如下：\n\n```shell\npython3 -m codemao_diger.requester [起始ID] [结束ID] [间隔时间] [输出数据库]\n```\n\n### 数据分析（饼）\n\n未完成，开发进度将会提交到`chart_dev`分支下，计划会有以下的功能\n\n#### 生成热词词云图\n\n计划Model路径`codemao_diger.chart.worldcloud`\n\n#### 生成发帖量柱状图\n\n计划Model路径`codemao_diger.chart.post_bar`\n\n#### 生成板块帖子量柱状图\n\n计划Model路径`codemao_diger.chart.board_bar`\n\n## 在您的项目中引用\n\n你也可以在你自己的项目中引用这个包，请遵循MIT License使用，文档暂时未完善\n\n## 贡献\n\n如果你要为项目贡献文档，请直接将写好的文档提交到`main`分支下的`/doc`文件夹\n\n如果你要为数据分析贡献代码，请提交至`chart_dev`分支\n',
        long_description_content_type = None,
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        keywords = '',

        author = '',
        author_email = '',
        maintainer = '',
        maintainer_email = '',

        license = 'MIT License',

        url = 'https://github.com/Rov-Waff/codemao-diger-rebuild',
        project_urls = {},

        scripts = [],
        packages = [
            'codemao_diger.DBMapper',
            'codemao_diger.charts.post_bar',
            'codemao_diger.requester',
            'codemao_diger.requester.entity'
        ],
        namespace_packages = [],
        py_modules = ['codemao_diger.DBGenerator'],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'pyecharts>=2.0.0',
            'requests>=2.32'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
