<!---[![pytest](https://github.com/ffreemt/set-env/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/set-env/actions)-->
# set-env-colab-kaggle-dotenv
[![pytest](https://github.com/ffreemt/set-env/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/set-env/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/set-env-colab-kaggle-dotenv.svg)](https://badge.fury.io/py/set-env-colab-kaggle-dotenv)

Set an environ variable from colab, kaggle or dotenv (search default .env/dotenv/env)

### Why `set_env`

colab and kaggle both provide a way to manage secrets (typically API tokens).

`set_env` is mainly for running ipynb (jupyter notebook) files in colab/kaggle or cloud instance when we need to set an environ variable, for example, `HF_TOKEN` to download models or datasets from huggingdace hub, other scenarios include `WANDB_API_KEY` or `NGROK_AUTHCODE` or `OPENAI_API_KEY` etc.

When running an ipynb in a cloud instance, we may use `dotenv` (`pip install python-dotenv`) to set environ varibales based on `.env`.

### Install it
```
pip install set-env-colab-kaggle-dotenv
```

### Setup Secrets or Upload `.env`

* In colab, set Secrets

    <img src="https://github.com/ffreemt/set-env/raw/main/img/colab.png" width="300" />

    <!---![](img/colab.png)-->

* In kaggle, set Add-ons/Secrets

    <img src="https://github.com/ffreemt/set-env/raw/main/img/kaggle.png" width="300" />

    <!---![](./img/kaggle.png)-->

* In other jupyter environ/cloud instance, upload .env, with contents, e.g.
```
HF_TOKEN=...
WANDB_API_KEY=...
```
In some cases, files start with a dot are not allowed. Rename `.env` to `dotenv` or `env` instead, `set_env` will auto-search for `.env`, `dotenv` and `env`.

## Use it
```
from set_env import set_env

# e.g.
set_env("HF_TOKEN")
set_env("WANDB_API_KEY")
set_env("NGROK_AUTHCODE")
```

Sometimes we want to set HF_TOKEN to HF_TOKEN_W (with write-permission).
```
from set_env import set_env
set_env(env_var="HF_TOKEN", source_var="HF_TOKEN_W")
```
This is effectively equivalent to `os.environ["HF_TOKEN"] = get_secret("HF_TOKEN_W")` when in colab or kaggle, or `os.environ["HF_TOKEN"] = dotenv.dotenv_values().get("HF_TOKEN_W")`.
