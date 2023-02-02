from lume_demo_package.flow import flow, output_variables

def test_flow_execution(tmp_path):
    flow.run(filename=f"{tmp_path}/test_file.txt", filesystem_identifier="local")
    #assert flow_run.is_successful()
