% fatos cidades
estrada(porto_alegre, caxias).
estrada(caxias, bento_goncalves).
estrada(porto_alegre, pelotas).
estrada(pelotas, rio_grande).

% fatos localizacao
esta_em(chave,    sala).
esta_em(livro,    quarto).
esta_em(carteira, cozinha).

comodo_em(sala,    casa_azul).
comodo_em(quarto,  casa_azul).
comodo_em(cozinha, casa_verde).

% regras
% Conexão direta (apenas o sentido declarado)
pode_viajar(De, Para) :-
    estrada(De, Para).


% Localização no nível da propriedade
localizacao_geral(Objeto, Casa) :-
    esta_em(Objeto, Comodo),
    comodo_em(Comodo, Casa).