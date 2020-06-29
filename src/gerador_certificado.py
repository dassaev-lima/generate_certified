from PIL import Image,ImageDraw, ImageFont

class GeradorCertificado:
    def __init__(self):
        self.nome_arquivo = ''
        self.lista_alunos = []

    def ler_arquivo(self,arquivo):
        arquivo = open(arquivo,'r')
        return arquivo.read()
        

    def gerar_certificado(self):
        
        dados = self.ler_arquivo('font/alunos')

        for elemento in dados.split('\n'):
            self.lista_alunos.append(elemento)

        for aluno in self.lista_alunos:    
            im = Image.open("certificado_modelo.png").convert('RGBA')
            txt = Image.new('RGBA', im.size, (255,255,255,0))
            fnt = ImageFont.truetype('font/Lato/Lato-Regular.ttf', 200)
            d = ImageDraw.Draw(txt)

            if len(aluno) <= 25:
                d.text((640,1000), f"{aluno}", font=fnt, fill=(0,0,0,255))
                out = Image.alpha_composite(im, txt)
                nome_aluno = aluno.split()
                self.nome_arquivo = nome_aluno[0]
                out.save(f'./imgs/{self.nome_arquivo}.png')
                print(f'gerado o certificado do aluno: {aluno}')
            else:
                print('O nome do aluno Ultrapassou o valor de caracteres permitidos')
 