"""Generated client library for binaryauthorization version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.binaryauthorization.v1beta1 import binaryauthorization_v1beta1_messages as messages


class BinaryauthorizationV1beta1(base_api.BaseApiClient):
  """Generated client library for service binaryauthorization version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://binaryauthorization.googleapis.com/'

  _PACKAGE = u'binaryauthorization'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'BinaryauthorizationV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new binaryauthorization handle."""
    url = url or self.BASE_URL
    super(BinaryauthorizationV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_attestors = self.ProjectsAttestorsService(self)
    self.projects_policy = self.ProjectsPolicyService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsAttestorsService(base_api.BaseApiService):
    """Service class for the projects_attestors resource."""

    _NAME = u'projects_attestors'

    def __init__(self, client):
      super(BinaryauthorizationV1beta1.ProjectsAttestorsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates an attestor, and returns a copy of the new.
attestor. Returns NOT_FOUND if the project does not exist,
INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the
attestor already exists.

      Args:
        request: (BinaryauthorizationProjectsAttestorsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Attestor) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors',
        http_method=u'POST',
        method_id=u'binaryauthorization.projects.attestors.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'attestorId'],
        relative_path=u'v1beta1/{+parent}/attestors',
        request_field=u'attestor',
        request_type_name=u'BinaryauthorizationProjectsAttestorsCreateRequest',
        response_type_name=u'Attestor',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an attestor. Returns NOT_FOUND if the.
attestor does not exist.

      Args:
        request: (BinaryauthorizationProjectsAttestorsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors/{attestorsId}',
        http_method=u'DELETE',
        method_id=u'binaryauthorization.projects.attestors.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'BinaryauthorizationProjectsAttestorsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an attestor.
Returns NOT_FOUND if the attestor does not exist.

      Args:
        request: (BinaryauthorizationProjectsAttestorsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Attestor) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors/{attestorsId}',
        http_method=u'GET',
        method_id=u'binaryauthorization.projects.attestors.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'BinaryauthorizationProjectsAttestorsGetRequest',
        response_type_name=u'Attestor',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (BinaryauthorizationProjectsAttestorsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IamPolicy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors/{attestorsId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'binaryauthorization.projects.attestors.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'BinaryauthorizationProjectsAttestorsGetIamPolicyRequest',
        response_type_name=u'IamPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists attestors.
Returns INVALID_ARGUMENT if the project does not exist.

      Args:
        request: (BinaryauthorizationProjectsAttestorsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAttestorsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors',
        http_method=u'GET',
        method_id=u'binaryauthorization.projects.attestors.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/attestors',
        request_field='',
        request_type_name=u'BinaryauthorizationProjectsAttestorsListRequest',
        response_type_name=u'ListAttestorsResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

      Args:
        request: (BinaryauthorizationProjectsAttestorsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IamPolicy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors/{attestorsId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'binaryauthorization.projects.attestors.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'BinaryauthorizationProjectsAttestorsSetIamPolicyRequest',
        response_type_name=u'IamPolicy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (BinaryauthorizationProjectsAttestorsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors/{attestorsId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'binaryauthorization.projects.attestors.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'BinaryauthorizationProjectsAttestorsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates an attestor.
Returns NOT_FOUND if the attestor does not exist.

      Args:
        request: (Attestor) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Attestor) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/attestors/{attestorsId}',
        http_method=u'PUT',
        method_id=u'binaryauthorization.projects.attestors.update',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='<request>',
        request_type_name=u'Attestor',
        response_type_name=u'Attestor',
        supports_download=False,
    )

  class ProjectsPolicyService(base_api.BaseApiService):
    """Service class for the projects_policy resource."""

    _NAME = u'projects_policy'

    def __init__(self, client):
      super(BinaryauthorizationV1beta1.ProjectsPolicyService, self).__init__(client)
      self._upload_configs = {
          }

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (BinaryauthorizationProjectsPolicyGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IamPolicy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/policy:getIamPolicy',
        http_method=u'GET',
        method_id=u'binaryauthorization.projects.policy.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'BinaryauthorizationProjectsPolicyGetIamPolicyRequest',
        response_type_name=u'IamPolicy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

      Args:
        request: (BinaryauthorizationProjectsPolicySetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IamPolicy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/policy:setIamPolicy',
        http_method=u'POST',
        method_id=u'binaryauthorization.projects.policy.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'BinaryauthorizationProjectsPolicySetIamPolicyRequest',
        response_type_name=u'IamPolicy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (BinaryauthorizationProjectsPolicyTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/policy:testIamPermissions',
        http_method=u'POST',
        method_id=u'binaryauthorization.projects.policy.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'BinaryauthorizationProjectsPolicyTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(BinaryauthorizationV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetPolicy(self, request, global_params=None):
      r"""A policy specifies the attestors that must attest to.
a container image, before the project is allowed to deploy that
image. There is at most one policy per project. All image admission
requests are permitted if a project has no policy.

Gets the policy for this project. Returns a default
policy if the project does not have one.

      Args:
        request: (BinaryauthorizationProjectsGetPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/policy',
        http_method=u'GET',
        method_id=u'binaryauthorization.projects.getPolicy',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'BinaryauthorizationProjectsGetPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def UpdatePolicy(self, request, global_params=None):
      r"""Creates or updates a project's policy, and returns a copy of the.
new policy. A policy is always updated as a whole, to avoid race
conditions with concurrent policy enforcement (or management!)
requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT
if the request is malformed.

      Args:
        request: (Policy) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('UpdatePolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdatePolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/policy',
        http_method=u'PUT',
        method_id=u'binaryauthorization.projects.updatePolicy',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='<request>',
        request_type_name=u'Policy',
        response_type_name=u'Policy',
        supports_download=False,
    )
