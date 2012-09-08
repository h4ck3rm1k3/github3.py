"""
github3.decorators
==================

This module provides decorators to the rest of the library

"""

from functools import wraps


def requires_auth(func):
    """Decorator to note which object methods require authorization."""
    note = """
    .. note::
        The signature of this function may not appear correctly in
        documentation. Please adhere to the defined parameters and their
        types.
    """
    # Append the above note to each function this is applied to
    func.__doc__ = '\n'.join([func.__doc__, note])

    @wraps(func)
    def auth_wrapper(self, *args, **kwargs):
        auth = False
        if hasattr(self, '_session'):
            auth = self._session.auth or \
                self._session.headers.get('Authorization')

        if auth:
            return func(self, *args, **kwargs)
        else:
            from github3.models import GitHubError
            # Mock a 401 response
            raise GitHubError(type('Faux Request', (object, ),
                {'status_code': 401, 'json': {
                    'message': 'Requires authentication'}}
                ))
    return auth_wrapper