# cloud-draw-architectur
use Diagram (Diagram as Code)


## Installation · Diagrams
> https://diagrams.mingrammer.com/docs/getting-started/installation

It requires **Python 3.6** or higher, check your Python version first.

It uses [Graphviz](https://www.graphviz.org/) to render the diagram, so you need to [install Graphviz](https://graphviz.gitlab.io/download/) to use **diagrams**. After installing graphviz (or already have it), install the **diagrams**.

> macOS users can download the Graphviz via `brew install graphviz` if you're using [Homebrew](https://brew.sh/). Similarly, Windows users with [Chocolatey](https://chocolatey.org/) installed can run `choco install graphviz`.

```
# using pip (pip3)
$ pip install diagrams

# using pipenv
$ pipenv install diagrams

# using poetry
$ poetry add diagrams
```

## Quick Start

```
# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
```

This code generates below diagram.

```
$ python diagram.py
```

![web service diagram](https://diagrams.mingrammer.com/img/web_service_diagram.png)

It will be saved as `web_service.png` on your working directory.

## Next

See more [Examples](https://diagrams.mingrammer.com/docs/getting-started/examples) or see [Guides](https://diagrams.mingrammer.com/docs/guides/diagram) page for more details.


## for example
>> nextcloud-on-gke.py

![nextcloud_on_google_kubernetes_engine](/image/nextcloud_on_google_kubernetes_engine.png)


