# ⚡ 猫站洛阳铲 ⚡

一个自动化在编程猫论坛挖坟的工具，当然也可以作为一个包导入到您的项目中

![GitHub last commit](https://img.shields.io/github/last-commit/Rov-Waff/codemao-diger-rebuild)

![PyPI - Version](https://img.shields.io/pypi/v/codemao-diger-rebuild)

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.codemao.cn%2Fweb%2Fforums%2Fposts%2F1630334%2Fdetails&query=n_views&label=%E7%8C%AB%E7%AB%99%E7%A4%BE%E5%8C%BA)

![GitHub Repo stars](https://img.shields.io/github/stars/Rov-Waff/codemao-diger-rebuild)

## 安装

### 通过pip安装

``````shell
pip install codemao-diger-rebuild
``````

### 通过源码安装

```shell
git clone git@github.com:Rov-Waff/codemao-diger-rebuild.git
cd codemao-diger-rebuild
python3 setup.py install
```

## 命令行使用

你可以运行这个包提供的一些Model以在猫站挖坟

### 生成帖子数据库

运行`codemao_diger.DBGenerator`这个Model可以生成存储帖子数据用的数据库，用法如下：

```shell
python3 -m codemao_diger.DBGenerator [数据库URL]
```

表结构请参考[文档](#)（没写好）

### 自动化挖坟

运行`codemao_diger.requester`这个Model可以自动化请求猫站API获取帖子数据，并将其存在指定数据库中，用法如下：

```shell
python3 -m codemao_diger.requester [起始ID] [结束ID] [间隔时间] [输出数据库]
```

### 数据分析（饼）

未完成，开发进度将会提交到`chart_dev`分支下，计划会有以下的功能

#### 生成热词词云图

计划Model路径`codemao_diger.chart.worldcloud`

#### 生成发帖量柱状图

计划Model路径`codemao_diger.chart.post_bar`

#### 生成板块帖子量柱状图

计划Model路径`codemao_diger.chart.board_bar`

## 在您的项目中引用

你也可以在你自己的项目中引用这个包，请遵循MIT License使用，文档暂时未完善

## 贡献

如果你要为项目贡献文档，请直接将写好的文档提交到`main`分支下的`/doc`文件夹

如果你要为数据分析贡献代码，请提交至`chart_dev`分支
