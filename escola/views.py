from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import CursoSerializer, AlunoSerializer, MatriculaSerializer, ListaMatriculaAlunosSerializer, ListaAlunosMatriculadosSerializer

class AlunosViewSets(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSets(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSets(viewsets.ModelViewSet):
    """Matriculas dos alunos(as)"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAlunos(generics.ListAPIView):
    """Listando as matriculas dos alunos(as)"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(Aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunosSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Liatando Alunos em no curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(Curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer


