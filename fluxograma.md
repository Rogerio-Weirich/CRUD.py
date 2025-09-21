# Fluxograma para o sistema CRUD:

[ INÍCIO ]

MENU PRINCIPAL:

Opções: 
(A) Estudante 
(B) Professor 
(C) Curso 
(D) Turma 
(E) Matrícula 
(X) Sair 
Escolha uma opção 
Se = (X) Sair  
Salva dados 
[ FIM ]  

Senão se = (A) Estudante ou (B) Professor
Exibe: "Opção selecionada: {Estudante|Professor}" 
MENU SECUNDÁRIO
(A) Adicionar 
Solicita: Nome, Sobrenome, CPF, Curso 
Valida entradas 
Confirma 
Se sim: Adiciona à lista, exibe lista 
Se não: Cancela, volta ao submenu  
(B) Listar 
Exibe: ID, Nome, Sobrenome, CPF, Curso  
Volta ao submenu  
(C) Editar  
Exibe lista, seleciona índices  
Escolhe: Nome, Sobrenome, CPF, Curso  
Valida: confirma, atualiza e exibe lista atualizada 
Cancela: Volta ao submenu  
(D) Excluir  
Exibe lista, seleciona índices  
Confirma  
Se sim: Remove da lista, atualiza turmas/matrículas  
Se não: Cancela e exibe lista atualizada  
Volta ao submenu 
(X) Voltar  
Retorna ao MENU PRINCIPAL  
(Q) Sair  
Salva dados  
[ FIM ]

(C) Curso  
MENU SECUNDÁRIO  
(A) Adicionar, (C) Editar, (D) Excluir 
Exibe: "Você não pode alterar cursos" 
Aguarda [ENTER]  
Volta ao submenu  
(B) Listar  
Exibe cursos disponíveis 
Seleciona curso  
Se válido: Exibe turmas, professor, alunos  
Se inválido: Mensagem de erro 
Volta ao submenu  
(X) Voltar  
Retorna ao MENU PRINCIPAL  
(Q) Sair  
Salva dados  
[ FIM ]

(D) Turma  
MENU SECUNDÁRIO  
(A) Adicionar  
Seleciona curso, professor  
Valida: Limite de turmas, curso do professor  
Confirma  
Se sim: Adiciona turma, exibe turmas  
Se não: Cancela  
Volta ao submenu  
(B) Listar  
Exibe: ID, Curso, Professor, Alunos  
Volta ao submenu  
(C) Editar  
Seleciona turma  
Escolhe: Professor ou Curso  
Valida, atualiza, exibe turmas  
Cancela: Volta ao submenu  
(D) Excluir  
Seleciona turma, confirma  
Se sim: Remove turma e matrículas, exibe turmas 
Se não: Cancela  
Volta ao submenu  
(X) Voltar  
Retorna ao MENU PRINCIPAL  
(Q) Sair  
Salva dados  
[ FIM ]

(E) Matrícula  
MENU SECUNDÁRIO  
(A) Adicionar  
Seleciona turma, estudante  
Valida: Limite de alunos, curso compatível  
Confirma  
Se sim: Adiciona matrícula, exibe turmas  
Se não: Cancela  
Volta ao submenu 
(B) Listar  
Exibe: Professor, Estudante, Curso, IDs  
Volta ao submenu  
(C) Editar  
Sem ação (vazio)  
Volta ao submenu  
(D) Excluir 
Seleciona turma, estudante 
Confirma  
Se sim: Remove matrícula, exibe matrículas 
Se não: Cancela  
Volta ao submenu
(X) Voltar  
Retorna ao MENU PRINCIPAL  
(Q) Sair  
Salva dados 
[ FIM ]

APÓS CADA OPERAÇÃO  
(Y) Continuar: 
Repete MENU SECUNDÁRIO  
(N) Voltar: 
Retorna ao MENU PRINCIPAL  
(Q) Sair: 
Salva dados 
[ FIM ]