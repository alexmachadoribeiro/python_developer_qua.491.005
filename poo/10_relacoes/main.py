from classes import Aluno, Curso
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    alunos = []
    cursos = []
    matricula = 0

    limpar()
    while True:
        aluno = Aluno(nome="", matricula=0, cpf="")
        curso = Curso(nome_curso="")

        print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}\n")
        print("1 - Cadastrar Aluno.")
        print("2 - Cadastrar Curso.")
        print("3 - Matricular aluno no curso.")
        print("4 - Listar cursos.")
        print("5 - Listar alunos.")
        print("6 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()

        limpar()
        match opcao:
            case "1":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do aluno: ").strip().title()
                    aluno.cpf = input("Informe o CPF do aluno: ").strip()
                    aluno.matricula = matricula

                    alunos.append(aluno)
                    limpar()

                    print(f"Aluno {aluno.nome} matriculado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível cadastrar aluno. {e}.")
                finally:
                    continue
            case "2":
                try:
                    curso.nome_curso = input("Informe o curso: ").strip().title()

                    cursos.append(curso)
                    limpar()

                    print(f"Curso {curso.nome_curso} cadastrado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível cadastrar curso. {e}.")
                finally:
                    continue
            case "3":
                try:
                    print(f"{'-'*10} Lista de alunos {'-'*10}\n")
                    for aluno in alunos:
                        print(f"Nome: {aluno.nome}")
                        print(f"Matrícula: {aluno.matricula}")
                        print(f"CPF: {aluno.cpf}")
                        print('-'*40)
                    # FIXME - Não foi possível matricular aluno no curso. argument of type 'int' is not iterable.
                    # inscricao = int(input("Informe a matrícula: "))
                    # for aluno in alunos:
                    #     aluno = {
                    #         'nome': aluno.nome,
                    #         'matricula': aluno.matricula,
                    #         'cpf': aluno.cpf
                    #     }
                    #     if inscricao in aluno['matricula']:
                    #         break
                    #     else:
                    #         ...

                    # limpar()

                    # print(f"{'-'*10} Lista de cursos {'-'*10}")
                    # for curso in cursos:
                    #     print(f"Curso: {curso.nome_curso}")
                    # curso_inscricao = input("Curso desejado: ").strip().title()

                    # aluno.inscrever_curso(curso_inscricao)
                    # limpar()

                    # print(f"Aluno {aluno.nome} inscrito no curso {curso.nome_curso} com sucesso.")
                except Exception as e:
                    print(f"Não foi possível matricular aluno no curso. {e}.")
                finally:
                    continue
            case "4":
                cursos.nome_curso.sort()
                for curso in cursos:
                    print(f"Curso: {curso.nome_curso}")
                    print("Alunos:")
                    curso.listar_alunos().sort()
                    for aluno in curso.listar_alunos():
                        print(aluno)
                    print('-'*40)
            case "5":
                alunos.nome.sort()
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")
                    print(f"Matrícula: {aluno.matricula}")
                    print(f"CPF: {aluno.cpf}")
                    print("Cursos matriculados: ")
                    aluno.listar_cursos().sort()
                    for curso in aluno.listar_cursos():
                        print(curso)
                    print('-'*40)
            case "6":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue
    
    # # alunos
    # aluno01 = Aluno("Fulano", 101, "111.111.111-11")
    # aluno02 = Aluno("Cicrano", 102, "222.222.222-22")
    # aluno03 = Aluno("Beltrano", 103, "333.333.333-33")
    # aluno04 = Aluno("João", 104, "444.444.444-44")
    # aluno05 = Aluno("Maria", 105, "555.555.555-55")
    # aluno06 = Aluno("José", 106, "666.666.666-66")

    # # cursos
    # curso01 = Curso("Python Developer")
    # curso02 = Curso("IA com Python")
    # curso03 = Curso("Desenvolvedor Java")

    # # inscrevendo os alunos nos cursos
    # aluno01.inscrever_curso(curso01)
    # aluno02.inscrever_curso(curso01)
    # aluno03.inscrever_curso(curso01)

    # aluno04.inscrever_curso(curso02)
    # aluno05.inscrever_curso(curso02)

    # aluno06.inscrever_curso(curso03)

    # # mostrar alunos nos cursos
    # print(f"Curso {curso01.nome_curso} tem os alunos: {curso01.listar_alunos()}.")