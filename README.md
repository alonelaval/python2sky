## python2sky 

python2sky 是一个python 语言的 skywalking 的客户端，遵循了  [Apache SkyWalking](https://github.com/apache/incubator-skywalking)  的tracing标准格式，现阶段支持的服务端版本为v2的协议。

### 安装：

```
  pip install python2sky
```

该项目花了大概3天的时间，后续会继续改进，在skywalking服务端 为6.6的时候测试通过，如下图：






##  快速入门：
在测试 agent 的时候，使用了 flask，手动埋点的方式，后续会改进成自动埋点，请查看[样例](https://github.com/alonelaval/python2sky/blob/master/tests/falsk_test/test_flask.py) 