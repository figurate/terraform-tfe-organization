# diagram.py
from diagrams import Diagram
from diagrams.onprem.iac import Terraform

with Diagram("Terraform Cloud Organization", show=False, direction="RL"):
     Terraform("tfe organization")
