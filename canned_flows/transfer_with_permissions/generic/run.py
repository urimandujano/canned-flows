import yaml
from canned_flows.utils import format_and_print
from globus_automate_client import create_flows_client

with open(
    "canned_flows/transfer_with_permissions/generic/sample-input.yml"
) as flow_input_file:
    flow_input = yaml.safe_load(flow_input_file)

fc = create_flows_client()
resp = fc.run_flow(
    "",
    flow_scope=None,
    flow_input=flow_input,
    monitor_by=[],
    manage_by=[],
    label="A Run of the Flow ",
)

format_and_print(resp)
