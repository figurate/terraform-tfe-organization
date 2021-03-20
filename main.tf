/**
 * # Terraform Cloud Organization
 *
 * ![Terraform Cloud Organization](terraform_cloud_organization.png)
 */
resource "tfe_organization" "organization" {
  email                    = var.admin
  name                     = var.name
  collaborator_auth_policy = var.collaborator_auth_policy
}

resource "tfe_organization_membership" "membership" {
  count        = length(var.membership)
  email        = var.membership[count.index]
  organization = tfe_organization.organization.name
}
