from django.db.models import Count
from rest_framework import generics
from rest_framework import permissions

from .models import Board, TodoList
from .serializers import \
    BoardListAPIViewSerializer, \
    BoardCreateAPIViewSerializer, \
    TodoListAPIViewSerializer


class BoardListAPIView(generics.ListAPIView):
    """
    API to get all Boards with counts from todolist for each board
    permission: - Is Authenticated
    """
    serializer_class = BoardListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = Board.objects.annotate(count=Count('todo__board'))
        return queryset


class BoardCreateAPIView(generics.CreateAPIView):
    """
    API to create new Board
    permission" admin only
    """
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]


class BoardUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API for upadate/destroy boards
    to perform, - use row id
    permission: admin only
    """
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Board.objects.all()


class TodoListApiView(generics.ListAPIView):
    """
    API to get list of all todos for boars
    to perform, - use board row id
    permission: for all  Authenticated
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = TodoList.objects.filter(board=self.kwargs['board'])
        return queryset


class TodoListUnDoneApiView(generics.ListAPIView):
    """
    API to get list of all undone todos for boars
    to perform, - use board row id
    permission: for all  Authenticated
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = TodoList.objects.filter(board=self.kwargs['board']).filter(done=False)
        return queryset


class TodoCreateApiView(generics.CreateAPIView):
    """
    API to create a new task for the exact board
    permission: admin only
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]

    def get_queryset(self):
        queryset = TodoList.objects.filter(board=self.kwargs['board']).filter(done=False)
        return queryset


class TodoDeleteApiView(generics.DestroyAPIView):
    """
    API to delete todo
    use todolist row id
    permission: admin only
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]
    queryset = TodoList.objects.all()


class IsOwnerOrAdminPermission(permissions.BasePermission):
    """
    check is object owner or is staff
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class TodoUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    API to update todos
    use todolist row id
    permission: is object owner or admin
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [IsOwnerOrAdminPermission, ]
    queryset = TodoList.objects.all()
