# valeria_spawner

## Install

- Copy `ulkubespawner.py` in `/usr/local/lib/python3.6/dist-packages`.
- Add the following line to `jupyterhub_config.py`

```
from ulkubespawner import ULKubeSpawner
```
- Replace `c.JupyterHub.spawner_class` by :

```
c.JupyterHub.spawner_class = ULKubeSpawner
```