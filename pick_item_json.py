import os
import json

class PickItemJson:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pick_value": ("INT",{"defaultInput": True, "default": 0}),
                "input": ("STRING",{"defaultInput": True, "default": "", "dynamicPrompts": False}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, pick_value, input):
        data = json.loads(input)
        selected = data[pick_value % len(data)]
        return (json.dumps(selected),)
