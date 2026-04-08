% zoologia


% características dos animais

tem_penas(pinguim). 
tem_penas(aguia). 
tem_penas(pardal).

poe_ovos(pinguim).  
poe_ovos(aguia).  
poe_ovos(pardal).

poe_ovos(cobra).    
poe_ovos(tartaruga).

tem_pelos(cachorro). 
tem_pelos(gato). 
tem_pelos(baleia).



% classificacao


% Um animal é ave se tem penas e põe ovos
ave(X) :- 
    tem_penas(X), 
    poe_ovos(X).

% Um animal é mamífero se tem pelos
mamifero(X) :- 
    tem_pelos(X).

% Um animal é réptil se põe ovos e n tem penas
reptil(X) :- 
    poe_ovos(X), 
    \+ tem_penas(X).




% e commerce


% Aqui estão os clientes e quanto dinheiro eles têm
cliente(ana,    500.0).
cliente(pedro,  150.0).
cliente(carlos, 80.0).

% Aqui estão os produtos e seus preços
produto(notebook, 3000.0).
produto(teclado,  120.0).
produto(mousepad, 60.0).
produto(fone,     200.0).

% compra


% Um cliente pode comprar um produto se tiver dinheiro suficiente
pode_comprar(Nome, Item) :-

    % pega o saldo do cliente
    cliente(Nome, Saldo),

    % pega o preço do produto
    produto(Item, Preco),

    % verifica se o saldo é maior ou igual ao preço
    Saldo >= Preco.


% torneio

% Aqui estou dizendo quem venceu quem

venceu(carlos, ana).
venceu(carlos, pedro).
venceu(ana,    pedro).
venceu(pedro,  joao).
venceu(ana,    joao).

% invicto

% Um jogador é invicto se ninguem venceu ele
invicto(Jogador) :-

    % não existe ninguém que venceu esse jogador
    \+ venceu(_, Jogador).



% explicacao


% Zoologia:
% pinguim é ave
% cachorro é mamífero
% cobra é reptil

% Compras:
% ana pode comprar teclado e mousepad
% pedro pode comprar teclado e mousepad
% carlos só pode comprar mousepad

% Torneio:
% carlos é invicto (ninguém venceu ele)
% ana n é invicta (carlos venceu ela)
% pedro n é invicto
% joao n é invicto