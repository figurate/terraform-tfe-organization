# diagram.py
from diagrams import Diagram
from diagrams.onprem.iac import Terraform
from diagrams.onprem.client import User, Users

with Diagram("Terraform Cloud Organization", show=False, direction="RL"):
     Terraform("tfe organization") << [User("admin"), Users("membership")]
