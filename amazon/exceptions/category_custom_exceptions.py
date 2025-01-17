class CategoryAlreadyExistsException(Exception):
    pass

class CategoryDoesNotExistException(Exception):
    def __init__(self, category_id:int):
        self.category_id = category_id

    def __str__(self):
        return f"{self.category_id} does not exist"