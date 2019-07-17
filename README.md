### 介绍
后台系统WEB UI自动化测试

### 环境
* Python3
* Selenium2(2.48.0)
* Firefox 36
* unittest
* HTMLTestRunner.py

### 主要内容
* PO模式
* 每条用例运行完成自动截图
* 每个case.py运行中只打开一次浏览器，该case.py运行完成之后关闭浏览器
* 生成html测试报告
* 发送测试报告到邮箱

### 运行
* 单个测试文件运行
~~~
python3 *_case.py //case目录下
~~~

* 批量运行
~~~
python3 run_test.py //case目录下
~~~
