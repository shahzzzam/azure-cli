#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.15.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentVM(Model):
    """
    Deployment operation parameters.

    :param str uri: URI referencing the template. Default value:
     "https://azuretemplatehost.blob.core.windows.net/templatehost/CreateVM/azuredeploy.json"
     .
    :param str content_version: If included it must match the ContentVersion
     in the template.
    :param str deployment_parameter__artifacts_location_value: The container
     URI of the template.
    :param str deployment_parameter_os_publisher_value: The OS publisher of
     the OS image.
    :param str deployment_parameter_admin_password_value: Password for the
     Virtual Machine.
    :param str deployment_parameter_ip_address_type_value: Dynamic or Static
     IP address allocation.
    :param str deployment_parameter_storage_type_value: The VM storage type.
    :param str deployment_parameter_size_value: The VM Size that should be
     created.
    :param str deployment_parameter_admin_username_value: Username for the
     Virtual Machine.
    :param str deployment_parameter_dns_name_for_public_ip_value: Globally
     unique DNS Name for the Public IP used to access the Virtual Machine.
    :param str deployment_parameter_ip_address_prefix_value: The IP address
     prefix.
    :param str deployment_parameter_virtual_machine_name_value: The VM name
     that is displayed in the portal.
    :param str deployment_parameter_subnet_prefix_value: The subnet address
     type.
    :param str deployment_parameter_os_sku_value: The OS SKU to install.
    :param str deployment_parameter_os_offer_value: The OS Offer to install.
    :param str deployment_parameter_os_version_value: The OS version to
     install.
    :param str mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    """ 

    _validation = {
        'uri': {'required': True},
        'mode': {'required': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'deployment_parameter__artifacts_location_value': {'key': 'properties.parameters._artifactsLocation.value', 'type': 'str'},
        'deployment_parameter_os_publisher_value': {'key': 'properties.parameters.osPublisher.value', 'type': 'str'},
        'deployment_parameter_admin_password_value': {'key': 'properties.parameters.adminPassword.value', 'type': 'str'},
        'deployment_parameter_ip_address_type_value': {'key': 'properties.parameters.ipAddressType.value', 'type': 'str'},
        'deployment_parameter_storage_type_value': {'key': 'properties.parameters.storageType.value', 'type': 'str'},
        'deployment_parameter_size_value': {'key': 'properties.parameters.size.value', 'type': 'str'},
        'deployment_parameter_admin_username_value': {'key': 'properties.parameters.adminUsername.value', 'type': 'str'},
        'deployment_parameter_dns_name_for_public_ip_value': {'key': 'properties.parameters.dnsNameForPublicIP.value', 'type': 'str'},
        'deployment_parameter_ip_address_prefix_value': {'key': 'properties.parameters.ipAddressPrefix.value', 'type': 'str'},
        'deployment_parameter_virtual_machine_name_value': {'key': 'properties.parameters.virtualMachineName.value', 'type': 'str'},
        'deployment_parameter_subnet_prefix_value': {'key': 'properties.parameters.subnetPrefix.value', 'type': 'str'},
        'deployment_parameter_os_sku_value': {'key': 'properties.parameters.osSKU.value', 'type': 'str'},
        'deployment_parameter_os_offer_value': {'key': 'properties.parameters.osOffer.value', 'type': 'str'},
        'deployment_parameter_os_version_value': {'key': 'properties.parameters.osVersion.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    def __init__(self, content_version=None, deployment_parameter__artifacts_location_value=None, deployment_parameter_os_publisher_value=None, deployment_parameter_admin_password_value=None, deployment_parameter_ip_address_type_value=None, deployment_parameter_storage_type_value=None, deployment_parameter_size_value=None, deployment_parameter_admin_username_value=None, deployment_parameter_dns_name_for_public_ip_value=None, deployment_parameter_ip_address_prefix_value=None, deployment_parameter_virtual_machine_name_value=None, deployment_parameter_subnet_prefix_value=None, deployment_parameter_os_sku_value=None, deployment_parameter_os_offer_value=None, deployment_parameter_os_version_value=None, **kwargs):
        self.uri = "https://azuretemplatehost.blob.core.windows.net/templatehost/CreateVM/azuredeploy.json"
        self.content_version = content_version
        self.deployment_parameter__artifacts_location_value = deployment_parameter__artifacts_location_value
        self.deployment_parameter_os_publisher_value = deployment_parameter_os_publisher_value
        self.deployment_parameter_admin_password_value = deployment_parameter_admin_password_value
        self.deployment_parameter_ip_address_type_value = deployment_parameter_ip_address_type_value
        self.deployment_parameter_storage_type_value = deployment_parameter_storage_type_value
        self.deployment_parameter_size_value = deployment_parameter_size_value
        self.deployment_parameter_admin_username_value = deployment_parameter_admin_username_value
        self.deployment_parameter_dns_name_for_public_ip_value = deployment_parameter_dns_name_for_public_ip_value
        self.deployment_parameter_ip_address_prefix_value = deployment_parameter_ip_address_prefix_value
        self.deployment_parameter_virtual_machine_name_value = deployment_parameter_virtual_machine_name_value
        self.deployment_parameter_subnet_prefix_value = deployment_parameter_subnet_prefix_value
        self.deployment_parameter_os_sku_value = deployment_parameter_os_sku_value
        self.deployment_parameter_os_offer_value = deployment_parameter_os_offer_value
        self.deployment_parameter_os_version_value = deployment_parameter_os_version_value
        self.mode = "Incremental"
