import yaml
from canned_flows.utils import format_and_print
from globus_automate_client import create_flows_client

with open("canned_flows/move/generic/definition.yml") as flow_def_file:
    flow_def = yaml.safe_load(flow_def_file)

with open("canned_flows/move/generic/schema.yml") as flow_schema_file:
    flow_schema = yaml.safe_load(flow_schema_file)


fc = create_flows_client()
resp = fc.deploy_flow(
    flow_def,
    title="Title",
    subtitle="SubTitle",
    description="Description",
    keywords=[],
    visible_to=["public"],
    runnable_by=["all_authenticated_users"],  # Group ID
    administered_by=[],
    input_schema=flow_schema,
)
format_and_print(resp)
