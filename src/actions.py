from argparse import ArgumentParser
from typing import List

class AActions:
    """Abstract class for actions"""

    # Mandatory arguments
    _mandatory_arguments: List[str] =  []
    _optional_arguments: List[str] = []

    # Action name
    _name: str = ""

    def __init__(self, arg_parser: ArgumentParser):
        # Set arg parser
        self._arg_parser = arg_parser

    # Verify arguments
    def _verify_arguments(self, args: dict) -> bool:
        # Verify all mandatory arguments are present
        for arg in self._mandatory_arguments:
            if arg not in args.keys() or args[arg] == None:
                print("Missing argument: '" + arg + "' is mandatory for the '" + self._name + "' action.")
                return False
        # Verify that all arguments are valid
        for arg in args.keys():
            if ((arg not in self._mandatory_arguments and arg not in self._optional_arguments) and args[arg] != None) and arg != "action":
                print("Invalid argument: '" + arg + "' is not a valid argument for the '" + self._name + "' action.")
                return False
        return True

    # On execute action
    def _execute(self, args: dict):
        # SHOULD BE OVERWRITTEN
        pass

    # Execute action
    def execute(self, args: dict):
        # SHOULD NOT BE OVERWRITTEN
        # Verify arguments
        if not self._verify_arguments(args):
            return
        # Execute action
        self._execute(args)


# Execute action class
class ExecuteAction(AActions):
    """Execute action class"""

    # Mandatory arguments
    _mandatory_arguments: List[str] = ["project", "workflow"]
    _optional_arguments: List[str] = []

    # Action name
    _name: str = "execute"

    # Init action
    def __init__(self, arg_parser: ArgumentParser):
        super().__init__(arg_parser)

    # Execute action
    def _execute(self, args: dict):
        # Execute action
        print("Executing action '" + self._name + "' with arguments: " + str(args))