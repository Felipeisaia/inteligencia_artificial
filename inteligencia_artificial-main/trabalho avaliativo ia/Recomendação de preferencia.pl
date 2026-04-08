%cardapio

% ingredientes q cada prato tem

ingrediente(salada,   alface).
ingrediente(salada,   tomate).
ingrediente(salada,   cenoura).

ingrediente(omelete,  ovo).
ingrediente(omelete,  queijo).
ingrediente(omelete,  sal).

ingrediente(bowl,     arroz).
ingrediente(bowl,     feijao).
ingrediente(bowl,     couve).


%ingredientes veganos

vegano(alface).
vegano(tomate).
vegano(cenoura).
vegano(arroz).
vegano(feijao).
vegano(couve).
vegano(sal).


%streaming

%filmes e o gênero de cada um

filme(matrix,            acao).
filme(john_wick,         acao).
filme(mario_galaxy,   animacao).
filme(up,                animacao).
filme(parasita,          drama).
filme(o_poderoso_chefao, drama).


% Aqui estou dizendo o gosto de cada usuário

usuario_gosta(ana,   acao).
usuario_gosta(ana,   drama).
usuario_gosta(pedro, animacao).



% Regra para saber se um prato é vegano
prato_vegano(Prato) :-

    % o prato só é vegano se todos os ingredientes forem veganos

    % "não pode existir um ingrediente do prato que n seja vegano"

    \+ (ingrediente(Prato, Item),
        \+ vegano(Item)).


% recomendar filmes para um usuário
recomendar(Filme, Usuario) :-

    % Primeiro verifica qual genero o usuario curte
    usuario_gosta(Usuario, Genero),

    % Depois procura um filme desse mesmo genero
    filme(Filme, Genero).



% prato_vegano:
% se tiver algum ingrediente não vegano -> não é vegano
%se todos forem veganos -> é vegano

% recomendarr:
%  recomenda filmes com base no gosto do usuário
% - pega o genero que ele gosta e sugere filmes daquele genero