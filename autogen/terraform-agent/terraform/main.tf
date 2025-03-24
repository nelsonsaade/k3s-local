provider "kubernetes" {
  config_path = "/root/.kube/config"
}

variable "namespace_name" {}

resource "kubernetes_namespace" "dynamic_ns" {
  metadata {
    name = var.namespace_name
  }
}
