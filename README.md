### Resources

| Platform                                       | logo | type           | media           | status        | docs                                                       |
| ---------------------------------------------- | ---- | -------------- | --------------- | ------------- | ---------------------------------------------------------- |
| <a href="https://pollo.ai">Pollo</a>           |      | `ai_generator` | `video`         | `coming soon` | <a href="/app/crawlers/platforms/pollo/README.md">📄</a>   |
| <a href="https://www.promeai.pro/">Promeai</a> |      | `ai_generator` | `video`,`image` | `coming soon` | <a href="/app/crawlers/platforms/promeai/README.md">📄</a> |
|                                                |      |                |                 |               |                                                            |

### Structure

```shell
├── README.md
├── app
│   ├── api
│   │   ├── models
│   │   │   ├── APIBaseModel.py
│   │   │   ├── DataBaseModel.py
│   │   │   └── PolloRequest.py
│   │   ├── router.py
│   │   └── routers
│   │       ├── health_check.py
│   │       └── pollo_resource.py
│   ├── crawlers
│   │   ├── README.md
│   │   └── platforms
│   │       ├── pollo
│   │       │   ├── README.md
│   │       │   ├── crawler.py
│   │       │   ├── endpoints.py
│   │       │   ├── models.py
│   │       │   └── tags.py
│   │       └── promeai
│   │           └── README.md
│   ├── database
│   │   └── models
│   ├── http_client
│   │   └── HttpException.py
│   ├── main.py
│   ├── services
│   │   └── callback_service.py
│   └── utils
│       ├── logging_utils.py
│       └── serializers_utils.py
├── config
│   └── settings.py
├── github
├── pyproject.toml
├── scripts
├── start.py
├── tests
│   ├── integration
│   │   └── test_endpoints.py
│   ├── raw
│   │   └── index.html
│   └── unit
└── uv.lock

```
