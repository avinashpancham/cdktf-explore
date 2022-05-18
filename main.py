from constructs import Construct
from cdktf import App, TerraformStack
from imports.azurerm import AzurermProvider, ResourceGroup, StorageAccount

LOCATION = "westeurope"


class Infra(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AzurermProvider(self, "Azurerm", features={})

        rg = ResourceGroup(
            self,
            "cdktf-demo",
            name="cdktf-demo",
            location=LOCATION,
        )

        datalake = StorageAccount(
            self,
            "cdktfdatalake",
            name="cdktfdatalake",
            location=LOCATION,
            resource_group_name=rg.name,
            account_replication_type="LRS",
            account_tier="Standard",
        )


app = App()
Infra(app, "python-azure")

app.synth()
