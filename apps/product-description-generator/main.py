import writer as wf
import writer.ai
from prompts import base_prompts, user_prompt, seo_keywords

# This is the base template for the Product Description Generator tutorial.
# More documentation is available at https://developer.writer.com

# Initialize state here
wf.init_state({
    "form": {
        "title": "",
        "description": "",
        "keywords": ""
    },
    "message": "Fill in the inputs and click \"Generate\" to get started.",
})

