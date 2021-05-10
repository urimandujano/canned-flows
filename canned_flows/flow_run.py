import yaml
from globus_automate_client import create_flows_client

from canned_flows.utils import format_and_print

with open("canned_flows/move/input.yml") as flow_input_file:
    flow_input = yaml.safe_load(flow_input_file)

fc = create_flows_client()
resp = fc.run_flow(
    "e40b6cec-15eb-4d87-b4f3-8e6b0b59f65a",
    flow_scope=None,
    flow_input=flow_input,
    monitor_by=[],
    manage_by=[],
    label="A Run of the Flow e40b6cec-15eb-4d87-b4f3-8e6b0b59f65a",
)

format_and_print(resp)
