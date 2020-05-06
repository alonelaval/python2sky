## python2sky 

Python2sky is a Skywalking client written in Python, following the[Apache SkyWalking](https://github.com/apache/incubator-skywalking) tracing formats. Protocol v2 is currently supproted.[中文](README_CN.md)

### Installation

```
  pip install python2sky
```

This project is new and further improvements are on the way. All testing is performed and passed against Skywalking 6.6.

##  Quickstart

To test this agent, flask is used with manual event-tracking, which will eventually be iterated to automatic event-tracing in the near future. Please follow the [example](https://github.com/alonelaval/python2sky/blob/master/tests/falsk_test/test_flask.py).

### Configurations
#### Set Backend Address
```
from python2sky import config
config.BACKEND_SERVICE = "127.0.0.1:11800"

```
#### Set Service Name
```
from python2sky import config
config.SERVICE_NAME = "python-test"

```
#### Start Registration and Data Collecting
```
from python2sky.bootstrap import skywalking_boot
skywalking_boot()

```
#### Create Spans
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
#### Get Current Global TarceId
```
ContextManager.get_global_trace_id()
```
#### Stop Spans
Only after spans are stopped will they be sent to the backend.

```
ContextManager.stop_span(exit_span)
ContextManager.stop_span(local_span)
ContextManager.stop_span(entry_span)
```
#### Cross Process Propagation
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

#### Cross Thread Propagation
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

#### Testing on Java Project
[java](https://github.com/alonelaval/python2sky-agent-java-test) 

#### Add Python Components to Skywalking Backend
In **component-libraries.yml**:

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






