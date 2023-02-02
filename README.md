#  Lume Demo Project Model

This repository packages the `LumeDemoModel` in `lume-demo-package/model.py ` for execution with [Prefect](https://docs.prefect.io/) using the flow described in `lume-demo-package/flow/flow.py` using the variables:

<!--- The input and output variable tables are replaced when generating the project in template/hooks/post_gen_project.py-->
# input_variables
|variable name| type |default|
|-------------|------|------:|
|input1       |scalar|      1|
|input2       |scalar|      2|


# output_variables
|variable_name| type |
|-------------|------|
|output1      |image |
|output2      |scalar|
|output3      |scalar|



## Installation

This package may be installed using pip:
```
pip install git+https://github.com/slaclab/lume-services-model-template
```


## Dev

Install dev environment:
```
conda env create -f dev-environment.yml
```

Activate your environment:
```
conda activate lume-demo-repo-dev
```

Install package:
```
pip install -e .
```

Tests can be executed from the root directory using:
```
pytest .
```

### Note
This README was automatically generated using the template defined in https://github.com/slaclab/lume-services-model-template with the following configuration:

```json
{
    "author": "Tia Miceli",
    "email": "miceli@fnal.gov",
    "github_username": "tiamiceli",
    "github_url": "https://github.com/slaclab/lume-services-model-template",
    "project_name": "Lume Demo Project Model", 
    "repo_name": "lume-demo-repo", 
    "package": "lume-demo-package",
    "model_class": "LumeDemoModel"
}
```
