### Resources

| Platform                                      | logo | type                       | media                   | status        | docs                                                        |
| --------------------------------------------- | ---- | -------------------------- | ----------------------- | ------------- | ----------------------------------------------------------- |
| <a href="https://pollo.ai">Pollo</a>          |      | `ai_generator`             | `video`                 | `coming soon` | <a href="/app/crawlers/platforms/pollo/README.md">📄</a>    |
| <a href="https://promeai.pro/">Promeai</a>    |      | `ai_generator`             | `video`,`image`         | `coming soon` | <a href="/app/crawlers/platforms/promeai/README.md">📄</a>  |
| <a href="https://seaart.ai">Seaart</a>        |      | `ai_generator`,`ai_audio`  | `video`,`image`,`audio` | `coming soon` | <a href="/app/crawlers/platforms/seaart/README.md">📄</a>   |
| <a href="https://vidu.com">Vidu</a>           |      | `ai_generator`             | `video`,`image`         | `coming soon` | <a href="/app/crawlers/platforms/vidu/README.md">📄</a>     |
| <a href="https://artlist.io">Artlist</a>      |      | `ai_generator`,`ai_audio`  | `video`,`image`,`audio` | `coming soon` | <a href="/app/crawlers/platforms/artlist/README.md">📄</a>  |
| <a href="https://hailuoai.video">Hailuoai</a> |      | `ai_generator`,            | `video`,`image`,        | `coming soon` | <a href="/app/crawlers/platforms/hailuoai/README.md">📄</a> |
| <a href="https://app.klingai.com">Klingai</a> |      | `ai_generator`, `ai_audio` | `video`,`image`,        | `coming soon` | <a href="/app/crawlers/platforms/hailuoai/README.md">📄</a> |

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
