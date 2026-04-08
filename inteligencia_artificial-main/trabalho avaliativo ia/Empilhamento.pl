% fatos


%pilha de blocos

% A está em cima de B
sobre(a, b).

% B está em cima de C
sobre(b, c).

% D está em cima de E
sobre(d, e).

% Esses blocos estão no chão
no_chao(c).
no_chao(e).


% REGRAS


% Regra para saber se um bloco esta abaixo de outro
abaixo(X, Y) :-

    % Se Y esta sobre X, então X esta abaixo de Y
    sobre(Y, X).


% Regra para saber se um bloco esta livre (nada em cima dele)
bloco_livre(X) :-

    % n existe nenhum bloco em cima de X
    \+ sobre(_, X).

% explicacao


% abaixo(X, Y)
% serve para inverter a relação
% se Y está em cima de X, então X está abaixo de Y

% bloco_livre(X):
% verifica se o bloco não tem nada em cima
% o "_" significa qualquer bloco
% então ele testa se NÃO existe ninguém sobre X