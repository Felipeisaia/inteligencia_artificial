
% FATOS (inf do sistema)

% Aqui sao as disciplinas existentes
%m= matematica
%c= calculo
%a = algebra
%f= fisica

disciplina(m).
disciplina(c).
disciplina(a).
disciplina(f).

% Aqui tem  os pré-requisitos entre disciplinas
% Ex: para fazer cálculo, precisa ter feito matemática
pre_requisito(m, c).
pre_requisito(m, f).
pre_requisito(c, a).

% Disciplinas que cada aluno já concluiu
completou(joao, m).
completou(joao, c).
completou(maria, m).

% Notas dos alunos nas disciplinas
nota(joao, matematica, 8.5).
nota(joao, calculo, 6.0).
nota(maria, matematica, 7.0).
nota(maria, fisica, 5.5).




% regras (logic do sistema)


% Regra para saber se o aluno pode cursar uma disciplina
pode_cursar(Aluno, Disciplina) :-

    % verifica se a disciplina existe
    disciplina(Disciplina),

    % n pode existir um pre-requisito que o aluno n tenha feito
    %ou seja:
    %Se faltar algum pre-requisito -> não pode cursar
    % Se tiver todos -> pode cursar
    \+ (pre_requisito(Prereq, Disciplina),
        \+ completou(Aluno, Prereq)).



% Regra para saber se o aluno foi aprovado
aprovado(Aluno, Disciplina) :-

    %Pega a nota do aluno na disciplina
    nota(Aluno, Disciplina, Valor),

    %Se a nota for maior ou igual a 7, ele está aprovado
    Valor >= 7.0.



% Regra para saber se o aluno foi reprovado
reprovado(Aluno, Disciplina) :-

    % Pega a nota do aluno
    nota(Aluno, Disciplina, Valor),

    % Se a nota for menor que 7, ele está reprovado
    Valor < 7.0.


%MINHAS CONSULTAS QUE EU TESTEI
pode_cursar(joao, a) = true (completou calculo e matematica)
pode_cursar(maria, a) = false (não completou calculo)
aprovado(joao, m) = true (nota 8.5)
reprovado(joao, c) = true (nota 6.0)

