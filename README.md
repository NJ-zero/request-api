## request-api
主要基于requests+excel的接口测试

### 主要流程如下：
![image](https://github.com/NJ-zero/request-api/raw/master/flow.png)

### 代码整体结构如下：
- common文件夹,主要用来存放公共的文件及配置文件
  - getexceldata.py  setexceldata.py  用来读取和写入Excel数据
  - connect_DB check_db 主要是数据库相关，connect连接，check用来校验执行的sql和预期结果是否一致
  - readconfig.py 主要用来读取配置文件config.ini
  - check_all 主要用来校验结果，采用三重校验：1.status-code  2.sql执行的结果   3.content与预期结果正则匹配

- result文件，主要用来存放测试结果
- testcase文件夹，主要用来测试用例，目前采用的是一个模块一个用例
- testdata文件夹，主要用来存放测试数据，如：管理用例的Excel文件夹
- test_runner.py 用来执行所有的测试用例

### 个人认为的缺陷
由于只要依赖Excel，所以对用例设计要求较高  
当有较多业务上用例时，该模板就不在使用，直接在一个循环里轮询每一行数据  

### 20180511优化
- 支持简单串接口实现，即下一个接口的传参依赖上一个接口的返回
大致说明：
    - 被依赖接口，增加一行jsonpath解析接口返回的值，并加入一个列表jsondatas中
    - 依赖接口，在传参时，将依赖的参数value改为 'change{change}'
    - 读取Excel会用正则匹配，value值，将'change{change}'替换为jasondatas列表中的最后一个值

具体介绍可见 [个人主页](https://www.jianshu.com/p/dc1aafcf8c31)  
欢迎批评指正，交流学习。