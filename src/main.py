from gerador_certificado import GeradorCertificado

if __name__ == "__main__":
    
    gerador_certificado = GeradorCertificado()

    try:
        gerador_certificado.gerar_certificado()
    except Exception as ex:
        print(f'Algo deu errado {ex}')