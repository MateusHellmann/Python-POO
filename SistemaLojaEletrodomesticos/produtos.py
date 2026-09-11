class Categoria:
    def __init__(self, nome: str, percentual_comissao: float):
        self.nome = nome
        if percentual_comissao < 0:
            raise ValueError("O percentual de comissão não pode ser negativo.")
        self._percentual_comissao = percentual_comissao

    def get_percentual_comissao(self) -> float:
        return self._percentual_comissao

    def get_nome(self) -> str:
        return self.nome

    def get_descricao(self) -> str:
        return f"Categoria('{self.nome}', {self._percentual_comissao}%)"


class Produto:
    def __init__(
        self,
        id: str,
        nome: str,
        preco: float,
        quantidade_estoque: int,
        categoria: Categoria,
        prazo_garantia_meses: int,
    ):
        self.id = id
        self.nome = nome
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self._preco = preco
        self._quantidade_estoque = quantidade_estoque
        self.categoria = categoria
        self.prazo_garantia_meses = prazo_garantia_meses

    def _validar_preco(self, preco: float) -> float:
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        return preco

    def _validar_quantidade(self, quantidade: int) -> int:
        if quantidade < 0:
            raise ValueError("A quantidade em estoque não pode ser negativa.")
        return quantidade

    def get_preco(self) -> float:
        return self._preco

    def set_preco(self, novo_preco: float) -> None:
        self._preco = self._validar_preco(novo_preco)

    def get_quantidade_estoque(self) -> int:
        return self._quantidade_estoque

    def dar_baixa_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade a dar baixa deve ser positiva.")
        if quantidade > self._quantidade_estoque:
            raise ValueError(
                f"Estoque insuficiente para {self.nome}. "
                f"Disponível: {self._quantidade_estoque}, solicitado: {quantidade}"
            )
        self._quantidade_estoque -= quantidade

    def repor_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade de reposição deve ser positiva.")
        self._quantidade_estoque += quantidade

    def descricao_detalhada(self) -> str:
        return (
            f"{self.nome} | Categoria: {self.categoria.nome} | "
            f"Preço: R$ {self._preco:.2f} | Garantia: {self.prazo_garantia_meses} meses"
        )

    def __str__(self) -> str:
        return f"{self.nome} (R$ {self._preco:.2f})"


class LinhaBranca(Produto):
    def __init__(
        self,
        id: str,
        nome: str,
        preco: float,
        quantidade_estoque: int,
        categoria: Categoria,
        prazo_garantia_meses: int,
        consumo_energia_kwh_mes: float,
        classificacao_eficiencia: str,
    ):
        super().__init__(id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses)
        self.consumo_energia_kwh_mes = consumo_energia_kwh_mes
        self.classificacao_eficiencia = classificacao_eficiencia

    def descricao_detalhada(self) -> str:
        base = super().descricao_detalhada()
        return (
            f"{base} | Consumo: {self.consumo_energia_kwh_mes} kWh/mês | "
            f"Eficiência: {self.classificacao_eficiencia}"
        )


class Eletroportatil(Produto):
    VOLTAGENS_VALIDAS = ("110V", "220V", "Bivolt")

    def __init__(
        self,
        id: str,
        nome: str,
        preco: float,
        quantidade_estoque: int,
        categoria: Categoria,
        prazo_garantia_meses: int,
        voltagem: str,
    ):
        super().__init__(id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses)
        if voltagem not in self.VOLTAGENS_VALIDAS:
            raise ValueError(f"Voltagem inválida. Use uma das opções: {self.VOLTAGENS_VALIDAS}")
        self.voltagem = voltagem

    def descricao_detalhada(self) -> str:
        base = super().descricao_detalhada()
        return f"{base} | Voltagem: {self.voltagem}"
