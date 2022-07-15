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


# For example
## NextCloud on GKE
> nextcloud-on-gke.py

```
from diagrams import Cluster, Diagram, Node, Edge
from diagrams.k8s.compute import Pod
from diagrams.gcp.compute import KubernetesEngine
from diagrams.gcp.network import LoadBalancing
from diagrams.onprem.network import Internet
from diagrams.onprem.client import Client
from diagrams.onprem.client import Users
from diagrams.custom import Custom

with Diagram("NextCloud on Google Kubernetes Engine", show=True):

    internet_01 = Internet("Internet")
    users_01 = Users("ユーザー・端末")
        
    with Cluster("Google Cloud Platform"):

        gcp_lb = LoadBalancing("Cloud Load Balancing")


        with Cluster("Google Kubernetes Engine Cluster"):
            myapp_ing = KubernetesEngine("")
            with Cluster("Node"):
                myapp_node = KubernetesEngine("Node")
                myapp_pods = Pod("NextCloud")

                cc_nextcloud = Custom("NextCloud", "./Custom/nextcloud.png")

    users_01 - internet_01 >> Edge(headport="c", tailport="c", minlen="1", lhead='cluster_Kubernetes') >> gcp_lb
    gcp_lb >> Edge(headport="c", tailport="c", minlen="1", lhead='cluster_MyApp') >> myapp_ing >> Edge(headport="c", tailport="c", minlen="1", lhead='cluster_MyApp pods') >> myapp_node >> myapp_pods << cc_nextcloud 
```

![nextcloud_on_google_kubernetes_engine](/image/nextcloud_on_google_kubernetes_engine.png)




