# Terraform Cloud Organization

![Terraform Cloud Organization](terraform\_cloud\_organization.png)

## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| tfe | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| admin | Email address of the organization admin | `any` | n/a | yes |
| membership | A list of organization team member email addresses | `list(string)` | `[]` | no |
| name | Name of the organization | `any` | n/a | yes |

## Outputs

No output.

