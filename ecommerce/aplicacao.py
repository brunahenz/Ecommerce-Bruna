
from ecommerce.exportador_relatorio import (
    ExportadorCSV,
    ExportadorHTML,
)
from ecommerce.importador import CriadorImportador
from ecommerce.leitor import CriadorLeitor
from ecommerce.servico_importacao import ServicoImportacao


def montar_aplicacao(formato_relatorio: str = "csv"):
    if formato_relatorio == "csv":
        exportador = ExportadorCSV()
    elif formato_relatorio == "html":
        exportador = ExportadorHTML()
    else:
        raise ValueError(
            f"Formato de relatório não suportado: {formato_relatorio}"
        )

    return ServicoImportacao(
        criador_leitor=CriadorLeitor,
        criador_importador=CriadorImportador,
        exportador=exportador,
    )
