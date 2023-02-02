import copy
from typing import Dict
import numpy as np
from lume_model.models import BaseModel
from lume_model.variables import InputVariable, OutputVariable

from lume-demo-package import INPUT_VARIABLES, OUTPUT_VARIABLES



class LumeDemoModel(BaseModel):
    input_variables = copy.deepcopy(INPUT_VARIABLES)
    output_variables = copy.deepcopy(OUTPUT_VARIABLES)

    def __init__(self, **settings_kwargs):
        """Initialize the model. If additional settings are required, they can be 
        passed and handled here. For models that are wrapping model loads
        from other frameworks, this can be used for loading weights, referencing
        data files, etc.
        
        """
        super().__init__()

        # handle settings if any
        # if settings_kwargs is not None:
        # ...

    def evaluate(
        self, input_variables: Dict[str, InputVariable]
    ) -> Dict[str, OutputVariable]:
        """The evaluate method accepts input variables, performs the model execution,
        then returns a dictionary mapping variable name to output variable.

        Args:
            input_variables (Dict[str, InputVariable]): Dictionary of LUME-model input
                variables with values assigned.

        Returns:
            Dict[str, OutputVariable]: Dictionary of LUME-model output variables with
                values assigned.

        """

	self.output_variables["output1"].value = np.random.uniform(
		input_variables["input1"].value,  # lower dist bound
		input_variables["input2"].value,  # upper dist bound
		(50, 50),
	)
	self.output_variables["output2"].value = input_variables["input1"].value
	self.output_variables["output3"].value = input_variables["input2"].value


        return self.output_variables
