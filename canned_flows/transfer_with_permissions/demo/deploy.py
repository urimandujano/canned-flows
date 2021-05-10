import yaml
from canned_flows.utils import format_and_print
from globus_automate_client import create_flows_client

with open(
    "canned_flows/transfer_with_permissions/demo/definition.yml"
) as flow_def_file:
    flow_def = yaml.safe_load(flow_def_file)

with open("canned_flows/transfer_with_permissions/demo/schema.yml") as flow_schema_file:
    flow_schema = yaml.safe_load(flow_schema_file)


fc = create_flows_client()
resp = fc.deploy_flow(
    flow_def,
    title="Title",
    subtitle="SubTitle",
    description="Description",
    keywords=[],
    visible_to=["public"],
    runnable_by=["all_authenticated_users"],
    administered_by=[],
    input_schema=flow_schema,
)
format_and_print(resp)
