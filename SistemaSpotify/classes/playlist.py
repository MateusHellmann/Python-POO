from .musica import Musica

class Playlist:
    def __init__(self, nomePlaylist):
        self.nomePlaylist = nomePlaylist
        self.listaMusicas = []
        
    def adicionarMusica(self, musica:Musica):
        if musica not in self.listaMusicas:
            self.listaMusicas.append(musica)
            print(f"\nMúsica '{musica.titulo}' adicionado à playlist '{self.nomePlaylist}'.")
        else:
            print(f"\nMúsica '{musica.titulo}' já existe na playlist '{self.nomePlaylist}'.")
        
    def removerMusica(self, musica:Musica):
        self.listaMusicas.remove(musica)
        print(f"\nMúsica '{musica.titulo}' removida da playlist '{self.nomePlaylist}'.")
        
    def listarMusicas(self):
        if self.listaMusicas:
            duracaoTotal = 0
            print(f"\nPlaylist '{self.nomePlaylist}'")
            print(f"Quantidade de músicas: {len(self.listaMusicas)}")
            print(f"\nMúsicas da playlist:")
            print(
                f"{'ID':<5}"
                f"{'Título':<30}"
                f"{'Artista':<25}"
                f"{'Álbum':<25}"
                f"{'Duração':<10}"
            )
            print("-"*95)
            for contMusicas, musica in enumerate(self.listaMusicas):
                print(
                    f"{contMusicas:<5}"
                    f"{musica.titulo:<30}"
                    f"{musica.artista:<25}"
                    f"{musica.album:<25}"
                    f"{musica.duracao:<10} minutos"
                )
                duracaoTotal += musica.duracao
            print(f"\nDuração total: {len(self.listaMusicas)} minutos")
        else: 
            print(f"\nNão existe nenhuma música na playlist '{self.nomePlaylist}'.")