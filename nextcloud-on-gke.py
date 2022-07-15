from diagrams import Cluster, Diagram, Node, Edge
from diagrams.k8s.compute import Pod
from diagrams.gcp.compute import KubernetesEngine
from diagrams.k8s.network import Ing
from diagrams.gcp.network import LoadBalancing
from diagrams.onprem.network import Nginx
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
    
    