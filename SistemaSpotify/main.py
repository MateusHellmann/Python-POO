from classes.musica import Musica
from classes.playlist import Playlist

musicas = []
playlists = []
    
def cadastrarMusica():
    while True:
        try:
            tituloMusica = input("Digite o titulo da música (0 para cancelar): ")
            
            if tituloMusica == "0":
                break
            
            artistaMusica = str(input("Digite o artista da música: "))
            albumMusica = str(input("Digite o álbum da música: "))
            duracaoMusica = float(input("Digite a duração da música em minutos: "))
            
            musica = Musica(tituloMusica, artistaMusica, albumMusica, duracaoMusica)
            
            musicas.append(musica)
            
            print(f"\nMúsica '{musica.titulo}' cadastrada.\n")

            continuar = input("Deseja cadastrar outra música? (S/N) ")
            
            if continuar.lower() == "s":
                continue
            else:
                break
            
        except Exception:
            print("\nValor inválido.")
            
def listarMusicas():
    if musicas:
        print("\nMúsicas cadastradas:")
        print(
            f"{'ID':<5}"
            f"{'Título':<30}"
            f"{'Artista':<25}"
            f"{'Álbum':<25}"
            f"{'Duração':<10}"
        )
        print("-"*95)
        for contMusicas, musica in enumerate(musicas):
            print(
                f"{contMusicas:<5}"
                f"{musica.titulo:<30}"
                f"{musica.artista:<25}"
                f"{musica.album:<25}"
                f"{musica.duracao:<10} minutos"
            )
    else:
        print("\nNenhuma música cadastrada.")
            
def criarPlaylist():
    while True:
        try:
            nomePlaylist = input("Digite o nome da playlist (0 para cancelar): ")
            
            if nomePlaylist == "0":
                break
            
            playlist = Playlist(nomePlaylist)
            
            playlists.append(playlist)
            
            print(f"\nPlaylist '{playlist.nomePlaylist}' cadastrada.\n")

            continuar = input("Deseja cadastrar outra playlist? (S/N) ")
            
            if continuar.lower() == "s":
                continue
            else:
                break
            
        except Exception:
            print("\nValor inválido.")
            
def selecionarPlaylist() -> Playlist:
    if playlists:
        while True:
            print("\nPlaylists cadastradas:")
            print(
                f"{'ID':<5}"
                f"{'Playlist':<30}"
                f"{'Qtde. de Músicas':<5}"
            )
            print("-"*95)
                
            for contPlaylist, playlist in enumerate(playlists):
                print(
                    f"{contPlaylist:<5}"
                    f"{playlist.nomePlaylist:<30}"
                    f"{len(playlist.listaMusicas):<5}"
                )
                
            try:
                buscaPlaylist = int(input("\nSelecione a playlist digitando seu ID: "))
                if playlists[buscaPlaylist]:
                    return playlists[buscaPlaylist]
                else:
                    raise Exception
            except Exception:
                print("\nValor inválido")
    else:
        print("\nNenhuma playlist cadastrada.")
        return None
            
def selecionarMusica(metodo, playlist :Playlist = None):
    if metodo == "adicionar":
        if musicas:
            while True:
                listarMusicas()
                    
                try:
                    buscaMusica = int(input("\nDigite o ID da música que deseja adicionar: "))
                    if musicas[buscaMusica]:
                        return musicas[buscaMusica]
                    else:
                        raise Exception
                except Exception:
                    print("\nValor inválido")
        else:
            print("\nNenhum produto cadastrado.")
            return None
    elif metodo == "remover":
        if playlist.listaMusicas:
            while True:
                playlist.listarMusicas()
                    
                try:
                    buscaMusica = int(input("\nDigite o ID da música que deseja remover: "))
                    if playlist.listaMusicas[buscaMusica]:
                        return playlist.listaMusicas[buscaMusica]
                    else:
                        raise Exception
                except Exception:
                    print("\nValor inválido")
        else:
            print(f"\nNão existe nenhuma música na playlist '{playlist.nomePlaylist}'.")
            return None
            
def adicionarMusicaPlaylist():
    playlist = selecionarPlaylist()
    if playlist:
        musica = selecionarMusica("adicionar")
        
        if musica:
            playlist.adicionarMusica(musica)
    
    
def removerMusicaPlaylist():
    playlist = selecionarPlaylist()
    if playlist:
        musica = selecionarMusica("remover", playlist)
        
        if musica:
            playlist.removerMusica(musica)
    
def exibirPlaylist():
    playlist = selecionarPlaylist()
    
    if playlist:
        playlist.listarMusicas()

while True:
    print("\nSistema de Playlist")
    print("1 - Cadastrar música")
    print("2 - Listar músicas cadastradas")
    print("3 - Criar playlist")
    print("4 - Adicionar música à playlist")
    print("5 - Remover música da playlist")
    print("6 - Exibir playlist")
    print("0 - Sair")
    
    try:
        op = int(input("\nDigite o número da opcao desejada: "))
    except Exception:
        print("\nValor inválido")
        continue
    
    match op:
        case 0:
            print("\nSaindo do sistema...\n")
            break
        
        case 1:
            cadastrarMusica()
            
        case 2:
            listarMusicas()
            
        case 3:
            criarPlaylist()
        
        case 4:
            adicionarMusicaPlaylist()
        
        case 5:
            removerMusicaPlaylist()
            
        case 6:
            exibirPlaylist()
        
        case _:
            print("Opção inválida\n")
                