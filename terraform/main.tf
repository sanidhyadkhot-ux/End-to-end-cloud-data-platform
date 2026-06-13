terraform {
  required_version = ">= 1.5.0"
}

# Portfolio IaC template
# Resources planned:
# - Azure Storage Account / Data Lake
# - Azure Databricks Workspace
# - Snowflake Warehouse
# - Key Vault
# - Monitoring Workspace

resource "null_resource" "portfolio_infrastructure_plan" {
  provisioner "local-exec" {
    command = "echo Infrastructure plan for student portfolio project"
  }
}
