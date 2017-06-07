import pygame
import random

def main():
	pygame.init()
		
	tela = pygame.display.set_mode([640,704])

	pygame.display.set_caption("PROTOGAME") 

	relogio=pygame.time.Clock()

	cor_branca=(255,255,255)
	cor_azul=(108,194,236)
	cor_verde=(152,231,114)
	cor_preta=(0,0,0)
	cor_amarela=(149,160,63)

	imgfundo_filename = 'tabuleiro.png'
	imgfundo=pygame.image.load(imgfundo_filename).convert()

	person_filename = 'personagem.png'
	person=pygame.image.load(person_filename).convert_alpha()
	
	posicao=[0,64]

	img_protomini_filename = 'img_protomini.png'
	img_protomini=pygame.image.load(img_protomini_filename).convert_alpha()

	img_protozord_filename = 'img_protozord.png'
	img_protozord = pygame.image.load(img_protozord_filename).convert_alpha()

	img_pedagio_filename = 'img_pedagio.png'
	img_pedagio=pygame.image.load(img_pedagio_filename).convert_alpha()

	img_tesouro_filename = 'img_tesouro.png'
	img_tesouro=pygame.image.load(img_tesouro_filename).convert_alpha()


	sair=False
	
	pygame.font.init()
	fonte_padrao = pygame.font.get_default_font()
	fonte_protomini = pygame.font.SysFont(fonte_padrao,40)
	fonte_protozord = pygame.font.SysFont(fonte_padrao,30)
	fonte_pedagio = pygame.font.SysFont(fonte_padrao,35)
	fonte_tesouro = pygame.font.SysFont(fonte_padrao,30)

	audio_protozord = pygame.mixer.Sound('audio_protozord.ogg')
	audio_protomini = pygame.mixer.Sound('audio_protomini.ogg')
	audio_tesouro = pygame.mixer.Sound('audio_tesouro.ogg')
	audio_pedagio = pygame.mixer.Sound('audio_pedagio.ogg')

	life= 100
	gold=25
	weapon=100
	
	while sair != True: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair=True 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and posicao[0] < 576: 
					posicao[0]=posicao[0]+64
				if event.key == pygame.K_DOWN and posicao[1] < 640:
					posicao[1]=posicao[1]+64
				if event.key == pygame.K_LEFT and posicao[0] > 0:
					posicao[0]=posicao[0]-64
				if event.key == pygame.K_UP and posicao[1] > 64:
					posicao[1]=posicao[1]-64
			a=random.randint(0,10)*64
			b=random.randint(0,10)*64
			if posicao[0]==a and posicao[1]==b:
				text2 = fonte_protozord.render('Você encontrou um protozord, voce perdeu',1,cor_branca)
				tela.blit(text2,[0,0])
				imgfundo.blit(img_protozord,[100,128])
				audio_protozord.play()
			c=random.randint(0,10)*64
			d=random.randint(0,10)*64
			if posicao[0]==c and posicao[1]==d:
				life = life - random.randint(1,30)
				weapon = weapon - random.randint(1,30)
				gold=gold+1
				text1 = fonte_protomini.render('protomini a vista, agr vc tem: '+str(life)+' de vida, '+ str(weapon)+' de arma e '+str(gold)+ ' ouros',1,cor_branca)
				tela.blit(text1,[0,0])
				imgfundo.blit(img_protomini,[100,128])
				audio_protomini.play()
			e=random.randint(0,10)*64
			f=random.randint(0,10)*64
			if posicao[0]==e and posicao[1]==f:
				gold=gold+random.randint(1,5)
				text4 = fonte_tesouro.render('Você encontrou um baú, ganhou 5 moedas, agr possui '+str(gold)+' moedas',1,cor_branca)
				tela.blit(text4,[0,0])
				imgfundo.blit(img_tesouro,[100,128])
				audio_tesouro.play()
			g=random.randint(0,10)*64
			h=random.randint(0,10)*64
			if posicao[0]==g and posicao[1]==h:
				gold=gold-random.randint(1,5)
				text3 = fonte_pedagio.render('Você encontrou um pedagio, perdeu 5 moedas de ouro, agr tu tem só '+str(gold),1,cor_branca)
				tela.blit(text3,[0,0])
				imgfundo.blit(img_pedagio,[100,128])
				audio_pedagio.play()			

		relogio.tick(27) 

		tela.blit(imgfundo,[0,64])

		tela.blit(person,posicao)

		pygame.display.update() 

	pygame.quit() 
		
		
main()


