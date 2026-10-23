
class ServicoImportacao:
    """Coordena leitura, importação e exportação de lançamentos."""

    def __init__(
        self,
        criador_leitor,
        criador_importador,
        exportador,
    ):
        self.criador_leitor = criador_leitor
        self.criador_importador = criador_importador
        self.exportador = exportador

    def executar(
        self,
        caminho_entrada: str,
        banco: str,
        caminho_saida: str,
    ) -> list:
        leitor = self.criador_leitor.criar(caminho_entrada)
        registros = leitor.ler_registros(caminho_entrada)

        importador = self.criador_importador.criar(banco)
        lancamentos = importador.importar(registros)

        self.exportador.exportar(lancamentos, caminho_saida)

        return lancamentos
