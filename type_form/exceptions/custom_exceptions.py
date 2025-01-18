class UserAlreadyPresentException(Exception):
    pass

class InvalidUserException(Exception):
    pass

class WorkspaceAlreadyExistsException(Exception):
    pass

class InvalidWorkspaceException(Exception):
    pass

class AlreadyInvitedException(Exception):
    pass

class InvalidInvitationException(Exception):
    pass

class AlreadyAcceptedException(Exception):
    pass

class FormAlreadyExistsException(Exception):
    pass

class InvalidFormException(Exception):
    pass

class FieldAlreadyExistsException(Exception):
    pass

class InvalidFieldException(Exception):
    pass

class MaximumInvitesLimitReachedException(Exception):
    pass

class SettingsAlreadyExistsException(Exception):
    pass

class InvalidFormFieldException(Exception):
    pass

class InvalidSettingsException(Exception):
    pass

class InvitationExpiredException(Exception):
    pass

class LayoutAlreadyExistsException(Exception):
    pass

class InvalidLayoutException(Exception):
    pass

class TabAlreadyExistsException(Exception):
    pass

class FieldDoesNotBelongToFormException(Exception):
    pass

class InvalidTabException(Exception):
    pass