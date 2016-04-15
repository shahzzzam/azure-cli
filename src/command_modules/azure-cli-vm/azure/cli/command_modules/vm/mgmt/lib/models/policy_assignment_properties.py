#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.15.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PolicyAssignmentProperties(Model):
    """
    Policy Assignment properties.

    :param str scope: Gets or sets the policy assignment scope.
    :param str display_name: Gets or sets the policy assignment display name.
    :param str policy_definition_id: Gets or sets the policy definition Id.
    """ 

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
    }

    def __init__(self, scope=None, display_name=None, policy_definition_id=None, **kwargs):
        self.scope = scope
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
