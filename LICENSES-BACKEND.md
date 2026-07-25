## データセットおよび疑似データについて (Dataset & Synthetic Data)

本プロジェクトで使用している機械学習モデルの学習データおよびWEB用DBデータは、すべて独自に生成した疑似データ（Synthetic Data）です。


* **背景・経緯:**  
  モデル構築にあたり Kaggle のコンペティションデータのデータ構造・仕様を参考にしていますが、該当データの利用規約（「No private sharing outside teams」等）を遵守するため、元のデータセットは使用・同梱しておりません。

* **データの性質:**   
  本リポジトリに含まれるデータは、SDV や Faker 等のライブラリを用いて作成した疑似データであり、規約上の制約を受けることなく安全に公開・利用できるものです。

* **参考コンペティション:**  
  [Customer Churn Prediction 2020](https://www.kaggle.com/competitions/customer-churn-prediction-2020)

### 主要ライブラリおよびライセンス (Third-Party Licenses)

本プロジェクト（データの生成およびWebアプリケーション構築等）で使用している主要なライブラリおよびそのライセンス一覧です。

| Name                               | Version     | License                                            |
|------------------------------------|-------------|----------------------------------------------------|
| Faker                              | 40.21.0     | MIT License                                        |
| Flask                              | 3.1.3       | BSD-3-Clause                                       |
| GitPython                          | 3.1.50      | BSD-3-Clause                                       |
| Jinja2                             | 3.1.6       | BSD License                                        |
| Mako                               | 1.3.12      | MIT License                                        |
| MarkupSafe                         | 3.0.3       | BSD-3-Clause                                       |
| PyYAML                             | 6.0.3       | MIT License                                        |
| Pygments                           | 2.20.0      | BSD-2-Clause                                       |
| SQLAlchemy                         | 2.0.50      | MIT                                                |
| Werkzeug                           | 3.1.8       | BSD-3-Clause                                       |
| aiohappyeyeballs                   | 2.6.2       | Python Software Foundation License                 |
| aiohttp                            | 3.14.1      | Apache-2.0 AND MIT                                 |
| aiosignal                          | 1.4.0       | Apache Software License                            |
| alembic                            | 1.18.5      | MIT                                                |
| annotated-doc                      | 0.0.4       | MIT                                                |
| annotated-types                    | 0.7.0       | MIT License                                        |
| anyio                              | 4.13.0      | MIT                                                |
| asttokens                          | 3.0.1       | Apache 2.0                                         |
| attrs                              | 26.1.0      | MIT                                                |
| blinker                            | 1.9.0       | MIT License                                        |
| boto3                              | 1.43.22     | Apache-2.0                                         |
| botocore                           | 1.43.22     | Apache-2.0                                         |
| cachetools                         | 7.1.4       | MIT                                                |
| category_encoders                  | 2.9.0       | Other/Proprietary License                          |
| certifi                            | 2026.6.17   | Mozilla Public License 2.0 (MPL 2.0)               |
| cffi                               | 2.0.0       | MIT                                                |
| charset-normalizer                 | 3.4.7       | MIT                                                |
| click                              | 8.4.1       | BSD-3-Clause                                       |
| cloudpickle                        | 3.1.2       | BSD License                                        |
| comm                               | 0.2.3       | BSD License                                        |
| contourpy                          | 1.3.3       | BSD License                                        |
| copulas                            | 0.14.0      | Free for non-commercial use                        |
| cryptography                       | 48.0.1      | Apache-2.0 OR BSD-3-Clause                         |
| ctgan                              | 0.11.1      | Free for non-commercial use                        |
| cuda-bindings                      | 13.3.1      | LicenseRef-NVIDIA-SOFTWARE-LICENSE                 |
| cuda-pathfinder                    | 1.5.5       | Apache-2.0                                         |
| cuda-toolkit                       | 13.0.2      | UNKNOWN                                            |
| cycler                             | 0.12.1      | BSD License                                        |
| databricks-sdk                     | 0.119.0     | Apache Software License                            |
| debugpy                            | 1.8.21      | MIT License                                        |
| decorator                          | 5.3.1       | BSD-2-Clause                                       |
| deepecho                           | 0.8.1       | BUSL-1.1                                           |
| docker                             | 7.1.0       | Apache-2.0                                         |
| executing                          | 2.2.1       | MIT License                                        |
| fastapi                            | 0.136.3     | MIT                                                |
| filelock                           | 3.29.1      | MIT                                                |
| flask-cors                         | 6.0.5       | MIT                                                |
| fonttools                          | 4.63.0      | MIT                                                |
| frozenlist                         | 1.8.0       | Apache-2.0                                         |
| fsspec                             | 2026.4.0    | BSD-3-Clause                                       |
| gitdb                              | 4.0.12      | BSD License                                        |
| google-auth                        | 2.55.1      | Apache Software License                            |
| graphene                           | 3.4.3       | MIT                                                |
| graphql-core                       | 3.2.11      | MIT License                                        |
| graphql-relay                      | 3.2.0       | MIT License                                        |
| graphviz                           | 0.21        | MIT                                                |
| greenlet                           | 3.5.1       | MIT AND PSF-2.0                                    |
| gunicorn                           | 26.0.0      | MIT                                                |
| h11                                | 0.16.0      | MIT License                                        |
| httpcore                           | 1.0.9       | BSD-3-Clause                                       |
| httpx                              | 0.28.1      | BSD License                                        |
| huey                               | 3.0.3       | UNKNOWN                                            |
| idna                               | 3.18        | BSD-3-Clause                                       |
| importlib_metadata                 | 9.0.0       | Apache-2.0                                         |
| iniconfig                          | 2.3.0       | MIT                                                |
| ipykernel                          | 7.2.0       | BSD-3-Clause                                       |
| ipython                            | 9.14.0      | BSD-3-Clause                                       |
| ipython_pygments_lexers            | 1.1.1       | BSD License                                        |
| itsdangerous                       | 2.2.0       | BSD License                                        |
| jedi                               | 0.20.0      | MIT License                                        |
| jmespath                           | 1.1.0       | MIT License                                        |
| joblib                             | 1.5.3       | BSD-3-Clause                                       |
| jupyter_client                     | 8.8.0       | BSD License                                        |
| jupyter_core                       | 5.9.1       | BSD-3-Clause                                       |
| kiwisolver                         | 1.5.0       | BSD License                                        |
| matplotlib                         | 3.11.0      | Python Software Foundation License                 |
| matplotlib-inline                  | 0.2.2       | BSD-3-Clause                                       |
| mlflow                             | 3.14.0      | Apache Software License                            |
| mlflow-skinny                      | 3.14.0      | Apache Software License                            |
| mlflow-tracing                     | 3.14.0      | Apache Software License                            |
| mpmath                             | 1.3.0       | BSD License                                        |
| multidict                          | 6.7.1       | Apache License 2.0                                 |
| narwhals                           | 2.22.0      | MIT                                                |
| nest-asyncio                       | 1.6.0       | BSD License                                        |
| networkx                           | 3.6.1       | BSD-3-Clause                                       |
| numpy                              | 2.4.6       | BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 |
| nvidia-cublas                      | 13.1.1.3    | LicenseRef-NVIDIA-Proprietary                      |
| nvidia-cuda-cupti                  | 13.0.85     | Other/Proprietary License                          |
| nvidia-cuda-nvrtc                  | 13.0.88     | Other/Proprietary License                          |
| nvidia-cuda-runtime                | 13.0.96     | LicenseRef-NVIDIA-Proprietary                      |
| nvidia-cudnn-cu13                  | 9.20.0.48   | LicenseRef-NVIDIA-Proprietary                      |
| nvidia-cufft                       | 12.0.0.61   | Other/Proprietary License                          |
| nvidia-cufile                      | 1.15.1.6    | Other/Proprietary License                          |
| nvidia-curand                      | 10.4.0.35   | Other/Proprietary License                          |
| nvidia-cusolver                    | 12.0.4.66   | Other/Proprietary License                          |
| nvidia-cusparse                    | 12.6.3.3    | Other/Proprietary License                          |
| nvidia-cusparselt-cu13             | 0.8.1       | NVIDIA Proprietary Software                        |
| nvidia-nccl-cu13                   | 2.29.7      | LicenseRef-NVIDIA-Proprietary                      |
| nvidia-nvjitlink                   | 13.0.88     | Other/Proprietary License                          |
| nvidia-nvshmem-cu13                | 3.4.5       | LicenseRef-NVIDIA-Proprietary                      |
| nvidia-nvtx                        | 13.0.85     | Other/Proprietary License                          |
| opentelemetry-api                  | 1.43.0      | Apache-2.0                                         |
| opentelemetry-proto                | 1.43.0      | Apache-2.0                                         |
| opentelemetry-sdk                  | 1.43.0      | Apache-2.0                                         |
| opentelemetry-semantic-conventions | 0.64b0      | Apache-2.0                                         |
| packaging                          | 26.2        | Apache-2.0 OR BSD-2-Clause                         |
| pandas                             | 2.3.3       | BSD License                                        |
| parso                              | 0.8.7       | MIT License                                        |
| patsy                              | 1.0.2       | BSD License                                        |
| pexpect                            | 4.9.0       | ISC License (ISCL)                                 |
| pillow                             | 12.2.0      | MIT-CMU                                            |
| platformdirs                       | 4.10.0      | MIT                                                |
| plotly                             | 6.8.0       | MIT                                                |
| pluggy                             | 1.6.0       | MIT License                                        |
| prompt_toolkit                     | 3.0.52      | BSD License                                        |
| propcache                          | 0.5.2       | Apache Software License                            |
| protobuf                           | 6.33.6      | 3-Clause BSD License                               |
| psutil                             | 7.2.2       | BSD-3-Clause                                       |
| psycopg                            | 3.3.4       | LGPL-3.0-only                                      |
| psycopg-binary                     | 3.3.4       | LGPL-3.0-only                                      |
| ptyprocess                         | 0.7.0       | ISC License (ISCL)                                 |
| pure_eval                          | 0.2.3       | MIT License                                        |
| pyarrow                            | 24.0.0      | Apache-2.0                                         |
| pyasn1                             | 0.6.3       | BSD-2-Clause                                       |
| pyasn1_modules                     | 0.4.2       | BSD License                                        |
| pycparser                          | 3.0         | BSD-3-Clause                                       |
| pydantic                           | 2.13.4      | MIT                                                |
| pydantic_core                      | 2.46.4      | MIT                                                |
| pyparsing                          | 3.3.2       | MIT                                                |
| pytest                             | 9.1.1       | MIT                                                |
| python-dateutil                    | 2.9.0.post0 | Apache Software License; BSD License               |
| python-dotenv                      | 1.2.2       | BSD-3-Clause                                       |
| pytz                               | 2026.2      | MIT License                                        |
| pyzmq                              | 27.1.0      | BSD License                                        |
| rdt                                | 1.19.0      | Free for non-commercial use                        |
| requests                           | 2.34.2      | Apache Software License                            |
| ruff                               | 0.16.0      | MIT                                                |
| s3transfer                         | 0.18.0      | Apache Software License                            |
| scikit-learn                       | 1.9.0       | BSD-3-Clause                                       |
| scipy                              | 1.17.1      | BSD License                                        |
| sdmetrics                          | 0.25.0      | MIT License                                        |
| sdv                                | 1.32.1      | Free for non-commercial use                        |
| six                                | 1.17.0      | MIT License                                        |
| skops                              | 0.14.0      | UNKNOWN                                            |
| smmap                              | 5.0.3       | BSD License                                        |
| sqlparse                           | 0.5.5       | BSD License                                        |
| stack-data                         | 0.6.3       | MIT License                                        |
| starlette                          | 1.2.1       | BSD-3-Clause                                       |
| statsmodels                        | 0.14.6      | BSD License                                        |
| sympy                              | 1.14.0      | BSD License                                        |
| threadpoolctl                      | 3.6.0       | BSD License                                        |
| torch                              | 2.12.0      | BSD-3-Clause                                       |
| tornado                            | 6.5.6       | Apache Software License                            |
| tqdm                               | 4.67.3      | MPL-2.0 AND MIT                                    |
| traitlets                          | 5.15.0      | BSD License                                        |
| triton                             | 3.7.0       | MIT License                                        |
| typing-inspection                  | 0.4.2       | MIT                                                |
| typing_extensions                  | 4.15.0      | PSF-2.0                                            |
| tzdata                             | 2026.2      | Apache-2.0                                         |
| urllib3                            | 2.7.0       | MIT                                                |
| uvicorn                            | 0.49.0      | BSD-3-Clause                                       |
| yarl                               | 1.24.2      | Apache-2.0                                         |
| zipp                               | 4.1.0       | MIT                                                |
