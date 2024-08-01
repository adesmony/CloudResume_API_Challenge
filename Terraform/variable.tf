variable "resource_group_name" {
    description = "Name of Resource Group"
    default = "olowosam-rg"
}
variable "cosmosdb_account_name" {
    description = "Name of CosmosDB Account"
    default = "olowosam-csdb"
}
variable "cosmosdb_sqldb_name" {
    description = "Name of CosmosDB SQL"
    default = "olowosam-csdb-SQL"
}
variable "cosmosdb_container_name" {
    description = "Name of CosmosDB Container"
    default = "olowosam-csdb-Cntnr"
}
variable "storage_account_name" {
    description = "Name of Storage Account"
    default = "olowosamsa"
}
variable "app_service_plan" {
    description = "Name of App Service Plan"
    default = "olowosamsa-app-plan"
}
variable "linux_function_app" {
    description = "Name of Function App"
    default = "olowosamsa-funct-app"        
}