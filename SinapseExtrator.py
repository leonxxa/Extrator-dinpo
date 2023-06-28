# -*- coding: utf-8 -*-
#pyinstaller --onefile --log-level=DEBUG SinapseExtrator.py
###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os,re, csv, time
import datetime
from tika import parser
from pytesseract import pytesseract
import subprocess
import sys, traceback
import locale
import urllib
import tika


tika.TikaClientOnly = True
locale.setlocale(locale.LC_ALL, '')

global imgPF, sup 

sup = '.\\imng\\inter2.png'
imgPF = '.\\imng\\PF3.png'


class TelaMain ( wx.Frame ):
	def __init__( self, parent ):

		self.count = 0
		self.v = Validar()
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sinapse Extrator (DIP/PF) - versão 1.01", pos = wx.DefaultPosition, size = wx.Size( 590,355 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.SetSizeHints( wx.Size( 565,355) )
		self.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )

		sizerMain = wx.BoxSizer( wx.VERTICAL )
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( imgPF, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,77 ), 0 )

		bSizer31.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( imgPF, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,77 ), 5 )

		bSizer31.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Diretoria de Inteligência Policial - DIP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		sizerMain.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Sinapse Extrator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		sizerMain.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 1 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerMain.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 15 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_filePicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, u"Selecione uma pasta", u"*.*")


		bSizer2.Add( self.m_filePicker1, 1, wx.ALL, 5 )
		sizerMain.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

		self.textSup = wx.StaticText(self, wx.ID_ANY, u'Entre em contato', wx.DefaultPosition, wx.DefaultSize, 0)
		self.textSup.Wrap(-1)
		self.textSup.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		bSizer5.Add(self.textSup, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		sizerMain.Add( bSizer5, 1, wx.EXPAND, 5 )
		imageFile = sup
		image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.button1 = wx.BitmapButton(self, id=-1, bitmap=image1,pos=(2, 2), size = (image1.GetWidth()+5, image1.GetHeight()+5))
		self.button1.Bind(wx.EVT_BUTTON, self.Suporte)
		bSizer5.Add( self.button1, 0, wx.ALL, 5 )


		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Extrair", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_button4.Bind(wx.EVT_BUTTON, self.OnClicked)

		bSizer3.Add( self.m_button4, 0, wx.ALIGN_RIGHT|wx.ALL|wx.BOTTOM, 5 )

		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button41.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_button41.Bind(wx.EVT_BUTTON, self.Cancelar)
		bSizer3.Add( self.m_button41, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.checkOCR = wx.CheckBox( self, wx.ID_ANY, u"Extrair com OCR ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkOCR.SetValue(False)
		self.checkOCR.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.checkOCR.Bind(wx.EVT_CHECKBOX, self.EventoCheck)
		self.checkOCR.SetToolTip(u'Marque a caixa de seleção para extrair informações de imagens')
		bSizer3.Add( self.checkOCR, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
		bSizer3.Add(bSizer4, 0, wx.ALL, 5)

		self.gauge = wx.Gauge(self, range = 20, size = (590, 28), style = wx.GA_HORIZONTAL)

		bSizer3.Add( self.gauge, 0, wx.ALL, 5 )
		
		sizerMain.Add( bSizer3, 1, wx.EXPAND, 5 )
		self.SetSizer( sizerMain )
		self.Layout()

		self.Centre( wx.BOTH )



	def	Suporte(self, event):
		self.Mensagem('Suporte', 'Desenvolvido por: Jonatan Eckstein, Pedro Wallace\nJohnatan Sousa, Leonardo Pereira\n\nSuporte: cadastro.cintepol@pf.gov.br\n\nTelefone: (61)2024-8764 ou (61)2024-8898')

	def Cancelar(self, event):
		exit()
		
	
	def EventoCheck(self, event):
		pass

	def java_local(self, caminho_completo):
		comando = '"OpenJDKJRE64\\bin\\java" -jar tika-app-2.2.1.jar --encoding=UTF-8 --text "' + str(caminho_completo) + '"'
		resposta_comando = subprocess.run(comando, capture_output=True, shell=True)
		return resposta_comando.stdout.decode("utf-8")

	def OnClicked(self, event):

		try: 
			comando = 'java.exe -version'
			resposta_comando = subprocess.run(comando, capture_output=True, shell=True)
			#content = resposta_comando.stderr.decode("latin-1")
			content = resposta_comando.stderr.decode(errors="ignore")
			tem_java = False if content.find("java version") == -1 else True

			if tem_java == False:
				continuar = self.Mensagem2('Aviso', u'O Java não está instaldo nesta máquina, por isso o processo será mais lento. Deseja continuar?\nPara instalar o java copie o link: https://java.com/en/download/manual.jsp ')
				if continuar == False:
					exit()

			caminho = (r'..\Tesseract\tesseract.exe')
			pytesseract.tesseract_cmd = caminho
			diretorio = self.m_filePicker1.GetPath()
			marcado = self.checkOCR.GetValue()

			total = 0
			self.gauge.SetRange(total)
			for caminho,dir,arqs in os.walk(diretorio):
				total = total + len(arqs)
			self.gauge.SetRange(total)

			log = open('resultado.log', 'a')
			log_erro = open('erro.log', 'w')

			nome_arquivo = str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S-"+'Extrator'))+'.csv'
			with open(nome_arquivo, 'a', newline ='') as file:
				writer = csv.writer(file, delimiter = ';', quotechar='"', quoting = csv.QUOTE_MINIMAL)
				writer.writerow(['Caminho', 'Tipo', 'Valor', 'Normalizado'])
				for caminho, dirs, arqs in os.walk(diretorio):
					for arq in arqs:
						self.count = self.count + 1
						self.gauge.SetValue(self.count)

						caminho_completo = caminho + '\\' + arq
						if tem_java == False:
							content = self.java_local(caminho_completo)
						else:
							try:
								parsed = parser.from_file(caminho_completo)
								content = parsed['content']
							except:
								content = self.java_local(caminho_completo)

						text = ""

						if marcado and not content:
							try:
								content = pytesseract.image_to_string(caminho + '\\' + arq)
							except Exception as e:
								log_erro.write(caminho + '\\' + arq + ': '+ str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+'\n')


						if content:
							log.write(caminho + '\\' + arq+'\n')
							cpfs = re.findall(r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}', content)
							cnpjs = (re.findall(r'[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}', content))
							passaportes = re.findall(r"[A-Z][A-Z][0-9]{6}", content)
							rnes = re.findall(r"[A-Z][0-9]{6}-?[A-Z0-9]", content)
							titulos = re.findall(r"[0-9]{8}[01][0-9]{3}", content)
							organizacoes = re.findall(r"(300 ESPARTANOS|AMIGO DOS AMIGOS|ANJOS DA MORTE|ANTI[ -]BALA|BALA NA CARA|BONDE DO MALUCO|BONDE DOS 13|BONDE DOS 40|BONDE DOS CACHORROS|CEROL FINO|COMANDO BALA VOA|COMANDO CHICO BALA|COMANDO DA PAZ|COMANDO DEMOCRATICO DA LIBERDADE|COMANDO DO PITTY|COMANDO VERMELHO|COMBOIO DO C[AÃ]O|COMISS[AÃ]O DA PAZ|CONS[OÓ]RCIO DO CRIME|EQUIPE REX|FAM[IÍ]LIA DO NORTE|FRENTE PATRIOTICA MANOEL RODRIGUEZ|GUARDI[OÕ]ES DO ESTADO|IFARA|KATIARA|LIGA DA JUSTI[CÇ]A|M[AÁ]FIA PARANAENSE|MASSA|MATA RINDO|MIL[IÍ]CIA [AÁ]GUIAS DE MIRRA|MIL[IÍ]CIA DE JACAREPAGU[AÁ]|MIL[IÍ]CIA FAM[IÍ]LIA [EÉ] N[OÓ]S|MORADORES DE RUA|NOVO CANGA[CÇ]O|OKAIDA|OPERA[CÇ][AÃ]O JU[IÍ]ZO FINAL|OS ABERTOS|OS PRIMEIRA|PAZ,\s?LIBERDADE E DIREITO|PAZ,\s?LIBERDADE E JUSTI[CÇ]A|POVO DE ISRAEL|PCC|PRIMEIRA GUERRILHA DO NORTE|PRIMEIRO COMANDO DA CAPITAL|PRIMEIRO COMANDO DA MAIORIA|PRIMEIRO COMANDO DA PARA[IÍ]BA|PRIMEIRO COMANDO DE VIT[OÓ]RIA|PRIMEIRO COMANDO DO MARANH[AÃ]O|PRIMEIRO COMANDO DO NORTE|PRIMEIRO COMANDO DO PARAN[AÁ]|PRIMEIRO GRUPO CATARINENSE|RAIO A|RAIO B|SINDICATO DO CRIME|SINDICATO DO RIO GRANDE DO NORTE|TAURAS|TERCEIRO COMANDO|TERCEIRO COMANDO PURO|THUNDERCATS)", content,re.IGNORECASE)
							#tels = re.findall(r"\b(55)?(\(?[0-9]{2}?\)?[ ]?[0-9]{5}\-?[0-9]{4})\b", content)
							tels = re.findall(r"\b\(?[0-9]{2}\)?[ \-][0-9]{5}\-?[0-9]{4}\b", content)
							identidades = re.findall(r"(([0-9]{1})(|.?)([0-9]{3})(|.?)([0-9]{3})-?([0-9]{1}|X|x)?(\ ?\-?\ ?)(SSP|DETRAN|PC|SESP|SDS|IFP|SJS|SPTC|DPF|ITEP|SEJUSP|SSDS|SESEG|SEGUP|IGP|MTE|POLITEC|PM|SESDC|POL\.CIVIL|SEGUP|POLITEC|POM|SECC|SEJUSP|SESP|SJS|SJTC|SJTS|SPTC|INI)(\/|\-)(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO|PF)|([0-9]{2})(|.?)([0-9]{3})(|.?)([0-9]{3})(|-?)([0-9]{1})-?([0-9]{1}|X|x)?(\ ?\-?\ ?)(SSP|DETRAN|PC|SESP|SDS|IFP|SJS|SPTC|DPF|ITEP|SEJUSP|SSDS|SESEG|SEGUP|IGP|MTE|POLITEC|PM|SESDC|POL\.CIVIL|SEGUP|POLITEC|POM|SECC|SEJUSP|SESP|SJS|SJTC|SJTS|SPTC|INI)(\/|\-)(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO|PF))", content)
							#identidades = re.findall(r"(([0-9]{1,2})?.?([0-9]{3}).?([0-9]{3})-?([0-9]{1}|X|x)?(\ ?\-?\ ?)(SSP|DETRAN|PC|SESP|SDS|IFP|SJS|SPTC|DPF|ITEP|SEJUSP|SSDS|SESEG|SEGUP|IGP|MTE|POLITEC|PM|SESDC|POL\.CIVIL|SEGUP|POLITEC|POM|SECC|SEJUSP|SESP|SJS|SJTC|SJTS|SPTC|INI)(\/|\-)(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO|PF))", content)
							ceps = re.findall(r"\b[0-9]{2}\.?[0-9]{3}[-][0-9]{3}\b", content)
							placas = re.findall(r"\b[a-z]{3}[ -][0-9][a-z0-9][0-9]{2}\b", content, re.IGNORECASE)
							#placas = re.findall(r"[a-zA-Z]{3}[-]?[0-9][A-Za-z0-9][0-9]{2}", content)
							emails = re.findall(r"([a-z-Z0-9.]+\@[a-z0-9]+\.[a-z]+)(\.[a-z]+)?", content)
							urls = re.findall(r"([a-z]{3,}\:\/\/[\S]{10,}|www.[a-z]{2,}\.[a-z]{3}(\.)?([a-z]{2})?)", content)
							ips = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(?:a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}", content)
							

							if cpfs:
								for cpf in cpfs:
									if self.v.cpf(cpf.replace('.', '').replace('-', '')):
										cpf_tratado = '{}'.format(cpf.replace('.', '').replace('-', '').zfill(11))
										cpf_tratado = cpf_tratado[0:3]+cpf_tratado[3:6]+cpf_tratado[6:9]+cpf_tratado[9:]
										writer.writerow([caminho + "\\" + arq, 'CPF', '="{}"'.format(cpf), '="{}"'.format(cpf_tratado) ])
							if cnpjs:
								for cnpj in cnpjs:
									if self.v.cnpj(cnpj.replace('.', '').replace('-', '').replace('/', '')):
										cnpj_tratado = '{}'.format(cnpj.replace('.', '').replace('-', '').replace('/', ''))
										cnpj_tratado = cnpj_tratado[0:2]+cnpj_tratado[2:5]+cnpj_tratado[5:8]+cnpj_tratado[8:12]+cnpj_tratado[12:]
										writer.writerow([caminho + "\\" + arq, 'CNPJ', '="{}"'.format(cnpj), '{}'.format(cnpj_tratado)])

							if passaportes:
								for passaporte in passaportes:
									writer.writerow([caminho + "\\" + arq, 'Passaporte', '="{}"'.format(passaporte)])

							if rnes:
								for rne in rnes:
									writer.writerow([caminho + "\\" + arq, 'RNE', '="{}"'.format(rne)])

							if tels:
								for tel in tels:
									tel_tratado = "".join(re.findall(r'\d+', tel))
									if len(tel_tratado) == 11:
										tel_tratado = "({}) {}-{}".format(tel_tratado[0:2], tel_tratado[2:7], tel_tratado[7:11])
									else:
										tel_tratado = "{}-{}".format(tel_tratado[2:7], tel_tratado[7:11])
									writer.writerow([caminho + "\\"+ arq, 'Telefone', '="{}"'.format(tel),'{}'.format(tel_tratado) ])
							if identidades:
								for identidade in identidades:
									rg_tratado = '{}'.format(identidade[0])
									final_rg = rg_tratado[-6:].replace("-", "/")
									rg_tratado = "".join(re.findall(r'\d+', rg_tratado))
									if len(rg_tratado) == 9:
										rg_tratado = "{}.{}.{}-{}".format(rg_tratado[0:2], rg_tratado[2:5], rg_tratado[5:8], rg_tratado[8])
									else:
										rg_tratado = "{}.{}.{}".format(rg_tratado[0:1], rg_tratado[1:4], rg_tratado[4:7])
									rg_tratado = rg_tratado + final_rg
									writer.writerow([caminho + "\\" + arq, 'Identidade', '{}'.format(identidade[0]), '{}'.format(rg_tratado) ])
				
							if titulos:
								for titulo in titulos:
									if self.v.titulo(titulo):
										print(titulo)
										titulo_tratado = '{}'.format(titulo.replace('.', '').replace('-', '').replace('/', ''))
										titulo_tratado = "{} {} {}".format(titulo_tratado[0:4],titulo_tratado[4:8], titulo_tratado[8:12])
										print(titulo_tratado)
										writer.writerow([caminho + "\\"+ arq, 'Titulo', '="{}"'.format(titulo), '{}'.format(titulo_tratado) ])

							if organizacoes:
								for organizacao in organizacoes:
									organizacao_tratado = organizacao.upper()
									writer.writerow([caminho + "\\"+ arq, 'Organização', '="{}"'.format(organizacao), '{}'.format(organizacao_tratado) ])		

							if ceps:
								for cep in ceps:
									cep_tratado = cep
									writer.writerow([caminho + "\\"+ arq, 'CEP', '="{}"'.format(cep), '{}'.format(cep_tratado)])

							if placas:
								for placa in placas:
									placa_tratado = re.sub(r'\-| ', '', placa)
									writer.writerow([caminho + "\\"+ arq, 'PLACA', '="{}"'.format(placa), '{}'.format(placa_tratado.upper()) ])
							if emails:
								for email in emails:
									email_tratado = email
									writer.writerow([caminho + "\\"+ arq, 'EMAIL', '="{}"'.format(email[0]),'="{}"'.format(email_tratado[0])])
							if urls:
								for url in urls:
									url_tratado = url
									writer.writerow([caminho + "\\"+ arq, 'URL', '="{}"'.format(url[0]),'="{}"'.format(url_tratado[0])])

							if ips:
								for ip in ips:
									ip_tratado = ip
									writer.writerow([caminho + "\\"+ arq, 'IP', '="{}"'.format(ip),'="{}"'.format(ip_tratado)])
						else:
							log_erro.write(caminho + '\\' + arq + ': '+ str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+'\n')

							

				log_erro.close()
				log_erro2 = open('erro.log', 'r')
				linhas = log_erro2.readlines()

				self.Mensagem('Aviso', u'Extração realizada com Sucesso.\n{} arquivos encontrados e analisados\n{} falhas'.format(total, len(linhas)))
		except:
			traceback.print_exc(file=sys.stdout)
	def Mensagem(self, titulo, texto):
		dlg = wx.MessageDialog(self, texto, titulo, wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()

	def Mensagem2(self, titulo, texto):
		dlg = wx.MessageDialog(self, texto, titulo, wx.YES_NO|wx.ICON_QUESTION)
		result = dlg.ShowModal()
		if result == wx.ID_YES:
			return True
		else:
			return False

class Validar:
	def __init__(self):
		pass

	def titulo(self, titulo):
		titulo_lista = []

		for a in titulo:
			a = int(a)
			titulo_lista.append(a)
	
		calculo = titulo_lista[0]*2 + titulo_lista[1]*3 + titulo_lista[2]*4 + titulo_lista[3]*5 + titulo_lista[4]*6 + titulo_lista[5]*7 + titulo_lista[6]*8 + titulo_lista[7]*9 

		primeiro_digito = calculo%11

		calculo2 = titulo_lista[8]*7 + titulo_lista[9]*8 + titulo_lista[10]*9
		segundo_digito = (calculo2%11)


		if primeiro_digito == titulo_lista[10] and segundo_digito == titulo_lista[11]:
			print('Titulo Válido')
			return True
		else:
			print('Titulo Inválido')
			return False



	def cnpj(self, cnpj):

	# Completa com zeros a esquerda
		if len(cnpj) < 14:
			cnpj = '0' * (14 - len(cnpj)) + cnpj
		
		elif len(cnpj) > 14:
			print("CNPJ inválido")
			return False
		
		cnpj_lista = []
		
		for a in cnpj:
			a = int(a)
			cnpj_lista.append(a)

		calculo = (cnpj_lista[0]*5) + (cnpj_lista[1]*4) + (cnpj_lista[2]*3) + (cnpj_lista[3]*2) + (cnpj_lista[4]*9) + (cnpj_lista[5]*8) + (cnpj_lista[6]*7) + (cnpj_lista[7]*6) + (cnpj_lista[8]*5) + (cnpj_lista[9]*4) + (cnpj_lista[10]*3) + (cnpj_lista[11]*2) 

		resto = calculo%11
		
		if(resto<2):
			b = 0
		else:
			b = (11-resto)
			
			

		calculo2 = (cnpj_lista[0]*6) + (cnpj_lista[1]*5) + (cnpj_lista[2]*4) + (cnpj_lista[3]*3) + (cnpj_lista[4]*2) + (cnpj_lista[5]*9) + (cnpj_lista[6]*8) + (cnpj_lista[7]*7) + (cnpj_lista[8]*6) + (cnpj_lista[9]*5) + (cnpj_lista[10]*4) + (cnpj_lista[11]*3) + (cnpj_lista[12]*2)
		resto2 = calculo2%11
		
		if(resto2<2):
			a = 0
			
		else:
			a = 11-resto2
			

		if(b == cnpj_lista[12] and a == cnpj_lista[13]):
			print('CNPJ é válido')
			return True
		else:
			print('CNPJ não é valido')
			return False


	def cpf(self, cpf):

		if len(cpf) < 11:
			cpf = '0' * (11 - len(cpf)) + cpf

		elif len(cpf) > 11:
			print("CNPJ inválido")
			return False

		cpf_numerado = []	

		for a in cpf:
			a = int(a)
			cpf_numerado.append(a)

		for i in range(10):
			if cpf_numerado.count(i) == 11:
				print("CPF inválido")
				return False

		a1 = cpf_numerado[0]*10
		a2 = cpf_numerado[1]*9
		a3 = cpf_numerado[2]*8
		a4 = cpf_numerado[3]*7
		a5 = cpf_numerado[4]*6
		a6 = cpf_numerado[5]*5
		a7 = cpf_numerado[6]*4
		a8 = cpf_numerado[7]*3
		a9 = cpf_numerado[8]*2
		a10 = cpf_numerado[9]
		a11 = cpf_numerado[10]

		resultado = (a1+a2+a3+a4+a5+a6+a7+a8+a9)

		resto = resultado%11

		if resto < 2:
			a10 = 0
			b = a10
		else:
			a10 = (11-resto)
			b = a10
		

		a1 = cpf_numerado[0]*11
		a2 = cpf_numerado[1]*10
		a3 = cpf_numerado[2]*9
		a4 = cpf_numerado[3]*8
		a5 = cpf_numerado[4]*7
		a6 = cpf_numerado[5]*6
		a7 = cpf_numerado[6]*5
		a8 = cpf_numerado[7]*4
		a9 = cpf_numerado[8]*3
		a10 = cpf_numerado[9]*2

		resultado2 = (a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)

		resto2 = resultado2%11

		if resto2 < 2:
			a11 = 0
			c = a11
		else:
			a11 = (11-resto2)
			c = a11

		if c == cpf_numerado[10] and b == cpf_numerado[9]:
			print("CPF é valido")
			return True
		else:
			print("CPF inválido")
			return False

				

if __name__ == '__main__':
	app = wx.App()
	frame = TelaMain(None)
	frame.Show()
	app.MainLoop()




