## python2sky 

python2sky 是一个python 语言的 skywalking 的客户端，遵循了  [Apache SkyWalking](https://github.com/apache/incubator-skywalking)  的tracing标准格式，现阶段支持的服务端版本为v2的协议。

### 安装：

```
  pip install python2sky
```

该项目时间很短，后续会继续改进，在skywalking服务端版本为6.6的时候测试通过。

##  快速入门：
在测试 agent 的时候，使用了 flask，手动埋点的方式，后续会改进成自动埋点，请查看[样例](https://github.com/alonelaval/python2sky/blob/master/tests/falsk_test/test_flask.py) 

### 配置 
#### 服务端地址
```
from python2sky import config
config.BACKEND_SERVICE = "127.0.0.1:11800"

```
#### 服务名称
```
from python2sky import config
config.SERVICE_NAME = "python-test"

```
#### 启动注册和收集数据
```
from python2sky.bootstrap import skywalking_boot
skywalking_boot()

```
#### 创建 span
```
from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager
from python2sky.context.common import set_tag_url, set_tag_method, set_tag_status_code, set_layer_http, FLASK, \
    set_component, REQUESTS

entry_span = ContextManager.create_entry_span(request.path, None)
set_tag_url(entry_span, request.url)
set_tag_method(entry_span, req.method)
set_tag_status_code(entry_span, 200)
set_layer_http(entry_span)
set_component(entry_span, FLASK)
exit_url = "www.google.com"
local_span = ContextManager.create_local_span("/locahost_span")
exit_span = ContextManager.create_exit_span("/exit_span", exit_url)
```
#### 获取当前 tarceId
```
ContextManager.get_global_trace_id()
```
#### 结束 span
只有 span被 结束，才会被发送到后端服务器。

```
ContextManager.stop_span(exit_span)
ContextManager.stop_span(local_span)
ContextManager.stop_span(entry_span)
```
#### 多进程传播
```
@app.route('/flask/cross_process')
def cross_process():
    sw6 = request.headers.get(SKYWALKING_HERADER_V2)
    req = request
    context_carrier = None
    if sw6 and sw6 != "":
        context_carrier = ContextCarrier()
        context_carrier.deserialize(sw6)

    entry_span = ContextManager.create_entry_span(req.path, context_carrier)
    set_tag_url(entry_span, request.url)
    set_tag_method(entry_span, req.method)
    set_tag_status_code(entry_span, 200)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)

    exit_url = "http://localhost:8088/project/b"
    exit_carrier = ContextCarrier()
    exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)
    set_layer_http(exit_span)
    set_component(exit_span, REQUESTS)
    data = requests.get("http://localhost:8088/project/b", headers={SKYWALKING_HERADER_V2: exit_carrier.serialize()})
    set_tag_status_code(exit_span, data.status_code)

    ContextManager.stop_span(exit_span)
    ContextManager.stop_span(entry_span)

```

#### 多线程传播
```
@app.route('/flask/cross_thread')
def cross_thread():
    req = request
    entry_span = ContextManager.create_entry_span(req.path, None)
    set_tag_url(entry_span, request.url)
    set_tag_method(entry_span, req.method)
    set_tag_status_code(entry_span, 200)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)

    exit_url = "http://localhost:8088/project/b"
    snapshot = ContextManager.capture()

    def local_thread():
        local_span = ContextManager.create_local_span("/flask/cross_thread/local")
        ContextManager.continued(snapshot)
        ContextManager.stop_span(local_span)

    def exit_thread():
        exit_carrier = ContextCarrier()
        exit_span = ContextManager.create_exit_span("/flask/cross_thread/exit", exit_url)
        ContextManager.continued(snapshot)
        set_layer_http(exit_span)
        set_component(exit_span, REQUESTS)
        ContextManager.inject(exit_carrier)
        data = requests.get("http://localhost:8088/project/b", headers={SKYWALKING_HERADER_V2: exit_carrier.serialize()})
        set_tag_status_code(exit_span, data.status_code)
        ContextManager.stop_span(exit_span)

    t1 = Thread(target=local_thread, args=())
    t2 = Thread(target=exit_thread, args=())
    t1.start()
    t2.start()

    ContextManager.stop_span(entry_span)
```

#### 测试java项目
[java](https://github.com/alonelaval/python2sky-agent-java-test) 

#### skywalking 服务端添加 python 组件
在 **component-libraries.yml** 添加：

```
# python components
# [6000, 7000) for python agent
Flask:
  id: 6001
  languages: python
Requests:
  id: 6002
  languages: python
```


## License
Apache License 2.0. See [LICENSE](LICENSE) file for details.






