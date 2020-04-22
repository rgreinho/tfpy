from terraformpy import Provider
from terraformpy import Resource
from terraformpy import Terraform


def render(stackvars):

    # Terraform configuration.
    Terraform(required_version=stackvars.get("config.terraform.version"))

    # Backend configuration.
    Terraform(
        dict(
            backend=dict(
                gcs=dict(
                    bucket=stackvars.get("config.terraform.backend.gcp.bucket"),
                    prefix=stackvars.stack,
                    credentials=stackvars.get("config.gcp.credentials"),
                )
            )
        )
    )

    # Providers.
    Provider("google", **stackvars.get("config.gcp"))

    # Modules.

    # Resources.
    cluster = Resource(
        "google_container_cluster",
        "cluster",
        name="project-" + stackvars.environment,
        location=stackvars.get("config.gcp.region"),
        # The API requires a node pool or an initial count to be defined; that initial
        # count creates the "default node pool" with that # of nodes. So, we need to set
        # an initial_node_count of 1. This will make a default node pool with
        # server-defined defaults that Terraform will immediately delete as part of
        # Create. This leaves us in our desired state- with a cluster master with no
        # node pools.
        remove_default_node_pool=True,
        initial_node_count=1,
    )
    Resource(
        "google_container_node_pool",
        "preemptible_nodes",
        name="preemptible-node-pool",
        location=stackvars.get("config.gcp.region"),
        cluster=cluster.name,
        # `node_count` represents the number of nodes PER ZONE.
        node_count=1,
        node_config=dict(
            preemptible=True,
            machine_type="n1-standard-1",
            oauth_scopes=[
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring",
            ],
        ),
        # `node_count` represents the number of nodes PER ZONE.
        autoscaling=dict(min_node_count=1, max_node_count=3,),
        management=dict(auto_repair=True, auto_upgrade=True,),
    )
