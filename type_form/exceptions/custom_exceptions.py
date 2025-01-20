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

    def __init__(self, form_id:int):
        self.form_id = form_id

    def __str__(self):
        return f"Form with ID {self.form_id} doesn't exist."

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
    def __init__(self, form_id:int):
        self.form_id=form_id
    
    def __str__(self):
        return f"Layout already exists for form_id {self.form_id}"

class InvalidLayoutException(Exception):
    def __init__(self, layout_id:int):
        self.layout_id=layout_id
    
    def __str__(self):
        return f"Layout with ID {self.layout_id} doesn't exist."

class TabAlreadyExistsException(Exception):
    def __init__(self, layout_id:int):
        self.layout_id=layout_id
    
    def __str__(self):
        return f"Tab already exists for layout_id {self.layout_id}"

class FieldDoesNotBelongToFormException(Exception):
    pass

class InvalidTabException(Exception):
    pass

class InvalidLayoutForFormException(Exception):
    def __init__(self, form_id:int, layout_id:int):
        self.form_id=form_id
        self.layout_id=layout_id

    def __str__(self):
        return f"Layout ID {self.layout_id} is invalid for Form ID {self.form_id}"