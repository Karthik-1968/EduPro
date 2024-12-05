from edu_core.build.serializers.definitions.BasicTodo.BasicTodoSerializer import BasicTodoSerializer
from edu_core.build.serializers.definitions.BasicTodo.BasicTodoSerializer import BasicTodoType
from edu_core.build.serializers.definitions.TodoId.TodoIdSerializer import TodoIdSerializer
from edu_core.build.serializers.definitions.TodoId.TodoIdSerializer import TodoIdType

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize

class TodoType(BasicTodoType, TodoIdType):
    def __init__(self, **validated_data):
        BasicTodoType.__init__(self, **validated_data)
        TodoIdType.__init__(self, **validated_data)
        

class TodoSerializer(BasicTodoSerializer, TodoIdSerializer):
    def create(self, validated_data):
        
        basicTodoSerializer, _ = deserialize(BasicTodoSerializer, validated_data, many=False, partial=True)
        validated_data.update(basicTodoSerializer.__dict__)
        
        todoIdSerializer, _ = deserialize(TodoIdSerializer, validated_data, many=False, partial=True)
        validated_data.update(todoIdSerializer.__dict__)
        
        return TodoType(**validated_data)
