from etl import pipeline_calcular_kpi_de_vendas_consolidado



if __name__ == "__main__":
    pasta_argumento: str = 'data'
    formato_de_saida: list = ['csv'] 
    pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento,formato_de_saida)