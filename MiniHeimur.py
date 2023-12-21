def drawline():
    print('-'*80)

def cheats():
    lista_itens_cheat = ['pot','moeda','revive','booster harvest','xp','quit']
    lista_senhas = ['beta_tester','xopanni','duds','talaodecheque']
    os.system("cls")
    password = input('Digite sua senha:\n\t->')
    if password in lista_senhas:
        print()
    elif password == 'master_comando_11':
        while True:
            os.system("cls")
            print(f'\n\n{lista_itens_cheat}')
            item = input('\nQual Item vai levar, mestre?\n\t->').lower()
            if item == 'quit':
                break
            qtd = int(input('Qual a quantidade?\n\t->'))
            
            if item == 'pot':
                inventory['pot'] += qtd
            elif item == 'moeda':
                inventory['din'] += qtd
            elif item == 'revive':
                inventory['revive'] += qtd
            elif item == 'booster harvest':
                bonus['bonus_harvest'] += qtd
            elif item == 'xp':
                status['exp'] += qtd

def descanso():
    os.system("cls")
    drawline()
    print('\n\tA noite passa, os vagalumes vão embora...\nSem perceber, você adormece, e acorda novamente na noite seguinte...\n')
    drawline()
    status['vida_atual'] = status['vida_total']
    status['mana_atual'] = status['mana_total']
    os.system("pause")

def harvest():
    materiais_harvest = ['Frutas','Ervas','Minérios','Madeiras','Cristais']
    t = random.randint(1,5)

    if status['lvl_harvest'] >= 15:
        os.system("cls")
        i = input('Qual material deseja focar sua colheita?\n(Escreva assim como na lista de materiais...)\n\t->')   
    elif 'colheita' in magias_equipadas:
        os.system("cls")
        i = input('Qual material deseja focar sua colheita?\n(Escreva assim como na lista de materiais...)\n\t->')
    else:
        i = random.choice(materiais_harvest)
        
    y = (t * bonus['bonus_harvest']) + status['lvl_harvest']

    if i == 'Frutas':
        inventory['fruta'] += y
    elif i == 'Ervas':
        inventory['erva'] += y
    elif i == 'Minérios':
        inventory['minerio'] += y
    elif i == 'Madeiras':
        inventory['madeira'] += y
    elif i == 'Cristais':
        inventory['cristal'] += y
    elif i == 'Moedas':
        inventory['din'] += (y * 2)
    
    #ganho de exp
    status['exp_harvest'] += (t + bonus['bonus_harvest'] - 1)
    if i in materiais_harvest or i == 'Moedas':
        os.system("cls")
        drawline()
        print(f'\nCaminhando um pouco pelo ambiente, você encontra:\n{y} {i}\n')
        if status['exp_harvest'] >= ((3 * status['lvl_harvest']) + 20):
            status['exp_harvest'] -= ((3 * status['lvl_harvest']) + 20)
            status['lvl_harvest'] += 1
            print('\nVocê evoluiu sua capacidade de colheita!\n')
        drawline()
        os.system("pause")
    if i not in materiais_harvest:
        os.system("cls")
        drawline()
        print('Material não encontrado!')
        drawline()
        os.system("pause")
         
def calcular_arma():
    if equipamentos['arma'] == 'espada':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq']
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def']
        if 'espada' not in armas:
            armas.append('espada')
    elif equipamentos['arma'] == 'espada grande':
        equipamentos['atq_arma'] = (atributos['for'] / 2) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 2) + status['lvl']
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 2
        if 'espada grande' not in armas:
            armas.append('espada grande')
    elif equipamentos['arma'] == 'ultra espada grande':
        equipamentos['atq_arma'] = atributos['dex'] + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (status['lvl'] * 1.25)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 4
        if 'ultra espada grande' not in armas:
            armas.append('ultra espada grande')
    elif equipamentos['arma'] == 'bazuca':
        equipamentos['atq_arma'] = (atributos['dex'] * 1.25) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['dex'] / 2) + (atributos['int'] / 2) + status['lvl']
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 4
        if 'ka boom' not in magias:
            magias.append('ka boom')
        if 'queima roupa' not in magias:
            magias.append('queima roupa')
        if 'bazuca' not in armas:
            armas.append('bazuca')
    elif equipamentos['arma'] == 'arco':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq'] + 2 
        equipamentos['dano_player'] =  (atributos['dex'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def']
        if 'perfurador' not in magias:
            magias.append('perfurador')
        if 'arco' not in armas:
            armas.append('arco')
    elif equipamentos['arma'] == 'ultra arco':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + (bonus['bonus_atq'] * 2) + 2 
        equipamentos['dano_player'] =  (atributos['dex'] / 2) + status['lvl']
        equipamentos['def_armadura'] = (atributos['con'] / 4) + (atributos['dex'] / 4) + bonus['bonus_def']
        if 'perfurador' not in magias:
            magias.append('perfurador')
            magias.append('perfurador do dragão')
        if 'ultra arco' not in armas:
            armas.append('ultra arco')
    elif equipamentos['arma'] == 'sol prateado':
        equipamentos['atq_arma'] = (atributos['int'] / 4) + (atributos['con'] / 4) +  bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['int'] / 2) + (atributos['con'] / 4) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 4.5
        if 'ruby' and 'bash' not in magias:
            magias.append('ruby')
            magias.append('bash')
        if 'sol prateado' not in armas:
            armas.append('sol prateado')
    elif equipamentos['arma'] == 'lua dourada':
        equipamentos['atq_arma'] = (atributos['dex'] / 4) + (atributos['con'] / 4) +  bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (atributos['con'] / 4) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 4.5
        if 'dragon punch' and 'rise' not in magias:
            magias.append('dragon punch')
            magias.append('rise')
        if 'lua dourada' not in armas:
            armas.append('lua dourada')
    elif equipamentos['arma'] == 'lança':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + (status['lvl'] / 4)
        if 'lança' not in armas:
            armas.append('lança')
    elif equipamentos['arma'] == 'cajado':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq']
        equipamentos['dano_player'] =  (atributos['int'] / 2) + status['lvl']
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] - 2
        if 'meteoro' not in magias:
            magias.append('meteoro')
        if 'cajado' not in armas:
            armas.append('cajado')
    elif equipamentos['arma'] == 'varinha' or equipamentos['arma'] == 'grimório':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq']
        equipamentos['dano_player'] =  (atributos['int'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] 
        if 'bolt' not in magias:
            magias.append('bolt')
        if 'varinha' not in armas:
            armas.append('varinha')
    elif equipamentos['arma'] == 'escudo':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq']
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (status['lvl'] / 4)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + (bonus['bonus_def'] * 2)
        if 'bash' not in magias:
            magias.append('bash')
            magias.append('rise')
        if 'escudo' not in armas:
            armas.append('escudo')
    elif equipamentos['arma'] == 'manoplas':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + (bonus['bonus_atq'] * 1.5)
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['dex'] / 2) + bonus['bonus_def']
        if 'dragon punch' not in magias:
            magias.append('dragon punch')
        if 'manoplas' not in armas:
            armas.append('manoplas')
    elif equipamentos['arma'] == 'pistola' or equipamentos['arma'] == 'revolver':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq'] + 4 
        equipamentos['dano_player'] =  (atributos['dex'] / 4) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def']
        if 'turno extra' not in magias:
            magias.append('turno extra')
        if 'disparo carregado' not in magias:
            magias.append('disparo carregado')
        if 'revolver' not in armas:
            armas.append('revolver')
    elif equipamentos['arma'] == 'escopeta':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq'] + 1.5 
        equipamentos['dano_player'] =  (atributos['dex'] / 4) + (atributos['con'] / 4) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 2
        if 'disparo carregado' not in magias:
            magias.append('disparo carregado')
        if 'queima roupa' not in magias:
            magias.append('queima roupa')
        if 'escopeta' not in armas:
            armas.append('escopeta')
    elif equipamentos['arma'] == 'orbe':
        equipamentos['atq_arma'] = (atributos['dex'] / 4) + (atributos['int'] / 4) + bonus['bonus_atq']
        equipamentos['dano_player'] =  (atributos['int'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] 
        if 'ruby' not in magias:
            magias.append('ruby')
        if 'orbe' not in armas:
            armas.append('orbe')
    elif equipamentos['arma'] == 'foice':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 4) + (atributos['int'] / 4) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + (status['lvl'] / 4)
        if 'colheita' not in magias:
            magias.append('colheita')
        if 'foice' not in armas:
            armas.append('foice')
    elif equipamentos['arma'] == 'chicote':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 4) + (atributos['dex'] / 4) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def']
        if 'domo acorrentado' not in magias:
            magias.append('domo acorrentado')
        if 'chicote' not in armas:
            armas.append('chicote')
    elif equipamentos['arma'] == 'machado':
        equipamentos['atq_arma'] = (atributos['for'] / 2) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['for'] / 2) + status['lvl']
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def'] + 2
        if 'machado' not in armas:
            armas.append('machado')
    elif equipamentos['arma'] == 'amizade':
        equipamentos['atq_arma'] = (atributos['con'] / 2) + bonus['bonus_atq'] 
        equipamentos['dano_player'] =  (atributos['con'] / 2) + status['lvl']
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def']
        if 'talk no jutsu' not in magias:
            magias.append('talk no jutsu')
        if 'amizade' not in armas:
            armas.append('amizade')
    elif equipamentos['arma'] == 'dm_weapon_testing':
        equipamentos['atq_arma'] = (atributos['dex'] / 2) + bonus['bonus_atq']
        equipamentos['dano_player'] =  (atributos['for'] / 2) + (status['lvl'] / 2)
        equipamentos['def_armadura'] = (atributos['con'] / 2) + bonus['bonus_def']
        if 'bash' not in magias:
            magias.append('dragon punch')
            magias.append('bash')
            magias.append('rise')
            magias.append('bolt')
            magias.append('meteoro')
            magias.append('perfurador')
            magias.append('perfurador do dragão')
            magias.append('turno extra')
            magias.append('disparo carregado')
            magias.append('ruby')
            magias.append('colheita')
            magias.append('talk no jutsu')
            magias.append('domo acorrentado')
            magias.append('queima roupa')
            magias.append('ka boom')
        if 'dm_weapon_testing' not in armas:
            armas.append('dm_weapon_testing')

def selecionar_arma():
    while True:
        drawline()
        print('\n\tVocê acorda perdido, sem memórias...\n\tMilhares de armas a sua volta...\n\tVocê escolhe uma delas, finalmente.\n\n')
        drawline()
        equipamentos['arma'] = input('Qual arma teu coração escolheu?\n->').lower()
        if equipamentos['arma'] not in lista_de_armas:
            equipamentos['arma'] = ''
            os.system("cls")
            continue
        else:
            calcular_arma()
            os.system("cls")
            break

def atribuir_pontos():
    while status['pts_restantes'] != 0:
        os.system("cls")
        drawline()
        print(f'Você tem {status["pts_restantes"]} Pontos sobrando!')
        atr_add_for = int(input('Adicionar pontos em Força:\n->'))
        atr_add_dex = int(input('Adicionar pontos em Destreza:\n->'))
        atr_add_con = int(input('Adicionar pontos em Constituição:\n->'))
        atr_add_int = int(input('Adicionar pontos em Inteligência:\n->'))

        if (atr_add_con + atr_add_for + atr_add_dex + atr_add_int) == status['pts_restantes']:
            status['pts_restantes'] = 0
            atributos['for'] += atr_add_for
            atributos['dex'] += atr_add_dex
            atributos['con'] += atr_add_con
            atributos['int'] += atr_add_int
        else:
            print('\n\nValores Inválidos!\n\n\n')
            os.system("pause")
            continue

        status['vida_total'] = status['lvl'] + (atributos['con'] * 2)
        status['vida_atual'] = status['vida_total']
        status['mana_total'] = (status['lvl'] / 2) + atributos['int']
        status['mana_atual'] = status['mana_total']

def trocar_arma():
    while True:
        os.system("cls")
        drawline()
        print('\n')
        for i in (armas):
            print(f'-{str(i).capitalize()}')
        print('\n')
        drawline()
        nova_arma = input('\nQual arma deseja levar?\n->').lower()
        if nova_arma not in armas:
            print('\n\nVocê não possuí essa arma!!!\n\n')
            os.system("pause")
            continue
        elif nova_arma in armas:
            equipamentos['arma'] = nova_arma
            calcular_arma()
            print('\n\nTroca sucedida!\n\n')
            os.system("pause")
            break

def atribuir_magia(slot, magia):
    if magia == 'bash':
        cost = 3
        desc = 'O usuário avança com seu escudo em mãos, indo diretamente de encontro com o inimigo,\nem um empurrão embuído com seu espírito. (Somente Escudos)'
    elif magia == 'dragon punch':
        cost = 5
        desc = 'Forte soco dracônico, que perfura até os mais resistentes dos materiais.\n(Requisito: uma mão livre)'
    elif magia == 'perfurador':
        cost = 4
        desc = 'Prepara uma flecha especial, capaz de atravessar o inimigo "de cabo a rabo".\n(Somente Arcos)'
    elif magia == 'turno extra':
        cost = 2
        desc = 'Faz com que o herói realize ações extras antes do inimigo.'
    elif magia == 'bolt':
        cost = 6
        desc = 'Dispara um raio de energia concentrada no inimigo, fritando ele por dentro.\n(Somente Catalizadores)'
    elif magia == 'colheita':
        cost = 15
        desc = 'Realiza um ataque com energia vampírica, tomando parte da vida do inimigo para si.\n(Somente armas corpo-a-corpo)'
    elif magia == 'disparo carregado':
        cost = 16
        desc = 'Imbuí o próximo disparo com uma quantidade considerável de energia,\naumentando sua precisão e dano. (Somente armas à distância)'
    elif magia == 'rise':
        cost = 20
        desc = 'Levanta suas defesas, aumentando temporáriamente seu status. (Somente Escudos)'
    elif magia == 'meteoro':
        cost = 18
        desc = 'Conjura uma imensa bola flamejante nos céus acima do inimigo.\n(Somente Catalizadores)'
    elif magia == 'ruby':
        cost = 15
        desc = 'Conjura as chamas púrpuras do Nékrigi para corroer o alvo. (Somente Catalizadores)'
    elif magia == 'perfurador do dragão':
        cost = 40
        desc = 'Extraindo o máximo potêncial da flecha-artifício, atravessa o alvo,\ne destrói sua alma completamente no processo. (Somente Arcos)'
    elif magia == 'talk no jutsu':
        cost = 50
        desc = '"Eu quero domar o lobo." Tenta convencer o seu alvo a abaixar sua arma,\ne voltar para a casa. (Somente Escudos)'
    elif magia == 'domo acorrentado':
        cost = 43
        desc = 'Restringe os movimentos do alvo por um período de tempo.'
    elif magia == 'queima roupa':
        cost = 36
        desc = 'realiza um disparo extremamente próximo do inimigo,\nprocurando por pontos fracos enquanto imbuí sua energia. (Somente armas à distância)'
    elif magia == 'ka boom':
        cost = 60
        desc = 'A próxima coisa que você vai ver, com certeza não vai ser o inimigo vivo.\n(Somente Bazuca)'

    if slot == '1':
        ctrl_magias["custo1"] = cost
        ctrl_magias["desc1"] = desc
    elif slot == '2':
        ctrl_magias['custo2'] = cost
        ctrl_magias['desc2'] = desc
    
def trocar_magia():
    os.system("cls")
    drawline()
    print(f'\n\tMagias Equipadas:\n')
    print(f'Slot 1 - [{magias_equipadas[0].capitalize()}]')
    print(f'Descrição:\n{ctrl_magias["desc1"]}\n')
    print(f'Custo:   {ctrl_magias["custo1"]}\n\n')
    print(f'Slot 2 - [{magias_equipadas[1].capitalize()}]')
    print(f'Descrição:\n{ctrl_magias["desc2"]}\n')
    print(f'Custo:   {ctrl_magias["custo2"]}\n')
    drawline()
    mag = input('\nDeseja Trocar suas magias equipadas?\n->')
    if mag == 'sim' or mag == 's' or mag == 'ss':
        while True:
            os.system("cls")
            drawline()
            print('\n\tMagias Aprendidas:')
            for i in magias:
                i = i.capitalize()
                print(f'- {i}')
            print('')
            drawline()
        
            magia_nova = input('\nQual magia deseja levar em sua jornada?\n\t->').lower()
            slot_escolhido = input('\nQual slot deseja coloca-la?\n\t->')
            if magia_nova not in (magias):
                print('\nEssa escolha não faz muito sentido...\n\n')
                os.system("pause")
                break
            else:
                atribuir_magia(slot_escolhido, magia_nova)
                if slot_escolhido == '1':
                    del magias_equipadas[0]
                    magias_equipadas.insert(0, magia_nova)
                    break
                elif slot_escolhido == '2':
                    del magias_equipadas[1]
                    magias_equipadas.insert(1, magia_nova)
                    break
                
def mostrar_inventario():
    os.system("cls")
    drawline()
    print('\tColetáveis')
    print(f'Ervas: {inventory["erva"]}')
    print(f'Frutas: {inventory["fruta"]}')
    print(f'Minérios: {inventory["minerio"]}')
    print(f'Madeiras: {inventory["madeira"]}')
    print(f'Cristais: {inventory["cristal"]}')
    print('\tItens:')
    print(f'Poção: {inventory["pot"]}')
    print(f'Elixires: {inventory["elx"]}')
    print(f'Dinheiro: {inventory["din"]}')
    print(f'Fragmentos: {inventory["shard"]}')
    print(f'Revives: {inventory["revive"]}')
    print(f'Kit Captura: {inventory["kit_capt"]}')
    drawline()

    troca = input('Deseja Trocar de arma?\n->').lower()
    if troca == 'sim' or troca == 'ss' or troca == 's':
        trocar_arma()

def mostrar_status():
    os.system("cls")
    drawline()
    print('\t--Atributos--')
    print(f'Força: {atributos["for"]}')
    print(f'Destreza: {atributos["dex"]}')
    print(f'Constituição: {atributos["con"]}')
    print(f'Inteligência: {atributos["int"]}')
    print('\t--Bônus--')
    print(f'Bônus Ataque: {bonus["bonus_atq"]}')
    print(f'Bônus Defesa: {bonus["bonus_def"]}')
    print(f'Bônus Healing: {bonus["bonus_heal"]}')
    print(f'Bônus Elixir: {bonus["bonus_elx"]}')
    print(f'Bônus Colheita: {bonus["bonus_harvest"]}')
    print(f'Bônus Libra: {bonus["bonus_libra"]}')
    print(f'Bônus Dinheiro: {bonus["bonus_din"]}')
    print('\t--Somadores--')
    print(f'Ataque: {equipamentos["atq_arma"]}')
    print(f'Dano Base: {equipamentos["dano_player"]}')
    print(f'Defesa: {equipamentos["def_armadura"]}')
    print('\t--Estatísticas--')
    print(f'Vida: {status["vida_atual"]}/{status["vida_total"]}')
    print(f'Mana: {status["mana_atual"]}/{status["mana_total"]}')
    print(f'Experiência: {status["exp"]}/{15 + (status["lvl"] * inimigo["mult_rank"])}')
    print(f'Nível: {status["lvl"]}')
    print(f'Exp. Colheita: {status["exp_harvest"]}/{(3 * status["lvl_harvest"]) + 20}')
    print(f'Nível Colheita: {status["lvl_harvest"]}')
    print(f'Arma Equipada: {equipamentos["arma"].capitalize()}')
    drawline()
    os.system("pause")
    
def checar_preço(qtdx):
    if (qtdx * controle_loja['preço']) <= inventory['din']:
        controle_loja['check'] = True
    else:
        controle_loja['check'] = False

def compra_efetuada(qtdx):
    os.system("cls")
    drawline()
    print('\n\tCOMPRA EFETUADA COM SUCESSO!\n')
    drawline()
    inventory['din'] -= qtdx * controle_loja['preço']
    os.system("pause")

def compra_negada():
    os.system("cls")
    drawline()
    print('\n\tERRO DURANTE A COMPRA!!!\n')
    print('\tTem certeza que tem dinheiro suficiente?\n\tOu que escolheu um item correto?...\n')
    drawline()
    os.system("pause")

def loja():
    while True:
        controle_loja['check'] = False
        os.system("cls")
        drawline()
        print('Bem vindo ao mercador andarilho...\n')
        print(f'-Poção:\t\t10$\t({inventory["pot"]})')
        print(f'-Elixir:\t15$\t({inventory["elx"]})')
        print(f'-Kit Captura:\t30$\t({inventory["kit_capt"]})')
        print(f'-Revive:\t1500$\t({inventory["revive"]})')
        print(f'-Bônus Libra:\t150$\t({bonus["bonus_libra"]})')
        print(f'-Bônus Heal:\t250$\t({bonus["bonus_heal"]})')
        print(f'-Bônus Elixir:\t300$\t({bonus["bonus_elx"]})')
        print(f'-Bônus Moedas:\t370$\t({bonus["bonus_din"]})')
        print(f'\n\nCarteira: {inventory["din"]}$')
        print('Ou "Sair"...')
        drawline()
        print('\nO que deseja comprar?')
        item = input('->').lower()
        if item == 'sair':
            break
        print('\nE qual será a quantidade?\n(Somente números inteiros...)')
        qtd = int(input('->'))

        if item == 'poção' or item == 'pot':
            controle_loja['preço'] = 10
            checar_preço(qtd)
            if controle_loja['check'] == True:
                inventory['pot'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'elixir' or item == 'elx':
            controle_loja['preço'] = 15
            checar_preço(qtd)
            if controle_loja['check'] == True:
                inventory['elx'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'revive':
            controle_loja['preço'] = 1500
            checar_preço(qtd)
            if controle_loja['check'] == True:
                inventory['revive'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'libra' or item == 'bonus libra':
            controle_loja['preço'] = 150
            checar_preço(qtd)
            if controle_loja['check'] == True:
                bonus['bonus_libra'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'dinheiro' or item == 'bonus dinheiro' or item == 'din' or item == 'bonus din':
            controle_loja['preço'] = 370
            checar_preço(qtd)
            if controle_loja['check'] == True:
                bonus['bonus_din'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'heal' or item == 'bonus heal':
            controle_loja['preço'] = 250
            checar_preço(qtd)
            if controle_loja['check'] == True:
                bonus['bonus_heal'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'bonus elixir' or item == 'bonus elx':
            controle_loja['preço'] = 300
            checar_preço(qtd)
            if controle_loja['check'] == True:
                bonus['bonus_elx'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()
        elif item == 'kit captura' or item == 'kit':
            controle_loja['preço'] = 30
            checar_preço(qtd)
            if controle_loja['check'] == True:
                inventory['kit_capt'] += qtd
                compra_efetuada(qtd)
            else:
                compra_negada()

def craft_sucedido():
    os.system("cls")
    drawline()
    print('\nCrafting realizado com sucesso!!!\n')
    drawline()
    os.system("pause")
    
def craft_falha():
    os.system("cls")
    drawline()
    print('\nMateriais insuficientes!!!\n')
    drawline()
    os.system("pause")

def checar_posse_arma(arma):
    if arma in armas:
        os.system("cls")
        drawline()
        print('\nVocê ja tem essa arma!!!\n')
        drawline()
        os.system("pause")
    else:
        armas.append(arma)
        controle_loja['harvest'] = True
    
def checar_materiais(item,bqtd):
    controle_loja['harvest'] = False
    if item == 'Poção':
        qtd = int(input('Quantas poções deseja fazer?\n\t->'))
        if (inventory['cristal'] >= qtd) and (inventory['erva'] >= qtd * 7) and (inventory['fruta'] >= qtd * 10):
            inventory['pot'] += qtd
            inventory['erva'] -= qtd * 7
            inventory['fruta'] -= qtd * 10
            inventory['cristal'] -= qtd
            controle_loja['harvest'] = True
    
    elif item == 'Booster Harvest':
        if (inventory['cristal'] >= bqtd) and (inventory['erva'] >= bqtd) and (inventory['fruta'] >= bqtd) and (inventory['madeira'] >= bqtd) and (inventory['minerio'] >= bqtd):
            inventory['cristal'] -= bqtd
            inventory['erva'] -= bqtd
            inventory['fruta'] -= bqtd
            inventory['madeira'] -= bqtd
            inventory['minerio'] -= bqtd
            bonus['bonus_harvest'] += 1
            controle_loja['harvest'] = True
           
    else:
        if item == 'Espada':
            if (inventory['madeira'] >= 20) and (inventory['minerio'] >= 40) and (inventory['cristal'] >= 10):
                arma_craft = 'espada'
                checar_posse_arma(arma_craft)
                inventory['madeira'] -= 20
                inventory['minerio'] -= 40
                inventory['cristal'] -= 10
        if item == 'Espada Grande':
            if (inventory['madeira'] >= 30) and (inventory['minerio'] >= 80) and (inventory['cristal'] >= 20):
                arma_craft = 'espada grande'
                checar_posse_arma(arma_craft)
                inventory['madeira'] -= 30
                inventory['minerio'] -= 80
                inventory['cristal'] -= 20
        if item == 'Arco':
            if (inventory['madeira'] >= 70) and (inventory['minerio'] >= 20) and (inventory['cristal'] >= 15):
                arma_craft = 'arco'
                checar_posse_arma(arma_craft)
                inventory['madeira'] -= 70
                inventory['minerio'] -= 20
                inventory['cristal'] -= 15
        if item == 'Revolver':
            if (inventory['madeira'] >= 15) and (inventory['minerio'] >= 70) and (inventory['cristal'] >= 30):
                arma_craft = 'revolver'
                checar_posse_arma(arma_craft)
                inventory['madeira'] -= 15
                inventory['minerio'] -= 70
                inventory['cristal'] -= 30
        if item == 'Cajado':
            if (inventory['madeira'] >= 90) and (inventory['minerio'] >= 5) and (inventory['cristal'] >= 40):
                arma_craft = 'cajado'
                checar_posse_arma(arma_craft)
                inventory['madeira'] -= 90
                inventory['minerio'] -= 5
                inventory['cristal'] -= 40
        if item == 'Escudo':
            if (inventory['madeira'] >= 80) and (inventory['minerio'] >= 90) and (inventory['cristal'] >= 5):
                arma_craft = 'escudo'
                checar_posse_arma(arma_craft)
                inventory['madeira'] -= 80
                inventory['minerio'] -= 90
                inventory['cristal'] -= 5
            
def craft_item():
    os.system("cls")
    b = 20 * bonus['bonus_harvest']
    lista_itens_craftaveis = ['Booster Harvest','Espada','Espada Grande','Arco','Revolver','Cajado','Escudo','Poção']
    drawline()
    print('\tMateriais:\n')
    print(f'Ervas:\t\t{inventory["erva"]}')
    print(f'Frutas:\t\t{inventory["fruta"]}')
    print(f'Minérios:\t{inventory["minerio"]}')
    print(f'Madeiras:\t{inventory["madeira"]}')
    print(f'Cristais:\t{inventory["cristal"]}')
    drawline()
    print('\tItens "craftaveis":\n')
    print(f'Booster Harvest: \t',end='')
    print(f'Mad.:{b}, Erv.:{b}, Frt.: {b}, Min.: {b}, Cri.: {b}')
    print(f'Poção: \t\t\t',end='')
    print('Ervas: 7, Frutas: 10, Cristais: 1')
    print(f'Espada: \t\t',end='')
    print('Madeiras: 20, Minérios: 40, Cristais: 10')
    print(f'Espada Grande: \t\t',end='')
    print('Madeiras: 30, Minérios: 80, Cristais: 20')
    print(f'Arco: \t\t\t',end='')
    print('Madeiras: 70, Minérios: 20, Cristais: 15')
    print(f'Revolver: \t\t',end='')
    print('Madeiras: 15, Minérios: 70, Cristais: 30')
    print(f'Cajado: \t\t',end='')
    print('Madeiras: 90, Minérios: 05, Cristais: 40')
    print(f'Escudo: \t\t',end='')
    print('Madeiras: 80, Minérios: 90, Cristais: 05')
    drawline()
    craft = input('Qual item deseja craftar?\n(Case travado, escreva assim como indicado a cima...)\n\t->')
    if craft not in lista_itens_craftaveis:
        os.system("cls")
        drawline()
        print('Este item não existe!!!')
        drawline()
        os.system("pause")
    else:
        checar_materiais(craft,b)
        if controle_loja['harvest'] == True:
            craft_sucedido()
        else:
            craft_falha()

def inimigos_menores():
    inimigo['mult_din'] = 0.5
    inimigo['mult_exp'] = 0.5
    inimigo['mult_shard'] = 0
    inimigo['s_esp'] = False
    inimigo['esp'] = False

def inimigos_medios():
    inimigo['s_esp'] = False
    inimigo['mult_din'] = 1
    inimigo['mult_exp'] = 1
    inimigo['mult_shard'] = 0.5

def inimigos_maiores():
    inimigo['s_esp'] = False
    inimigo['esp'] = True
    inimigo['mult_din'] = 1.5
    inimigo['mult_exp'] = 1.5
    inimigo['mult_shard'] = 1

def atribuir_inimigo(nome,local):
    inimigo['nome'] = nome
    inimigo['lvl'] = random.randint(status['lvl'] - 5, status['lvl'] + 5)
    if inimigo['lvl'] <= 0 or status['lvl'] == 1:
        inimigo['lvl'] = 1
    #Rank baixo:
    if local == 'baixo':
        if nome == 'Carniçal':
            inimigo['vida'] = 20
            inimigo['atq'] = 3
            inimigo['def'] = 1
            inimigo['dano'] = 2 + (inimigo['lvl'] / 2)
            inimigos_menores()
        elif nome == 'Lobo':
            inimigo['vida'] = 15
            inimigo['atq'] = 1
            inimigo['def'] = 2
            inimigo['dano'] = 3 + (inimigo['lvl'] / 4)
            inimigos_menores()
        elif nome == 'Javali':
            inimigo['vida'] = 15
            inimigo['atq'] = 2
            inimigo['def'] = 3
            inimigo['dano'] = 1 + (inimigo['lvl'] / 2)
            inimigos_menores()
        elif nome == 'Keeper':
            inimigo['vida'] = 75 + (inimigo['lvl'] / 4)
            inimigo['atq'] = 7
            inimigo['def'] = 8
            inimigo['dano'] = 9 + (inimigo['lvl'] / 4)
            inimigo['esp'] = True
            inimigos_medios()
        elif nome == 'Cultista':
            inimigo['vida'] = 60 + (inimigo['lvl'] / 2)
            inimigo['atq'] = 8
            inimigo['def'] = 9
            inimigo['dano'] = 5 + (inimigo['lvl'] / 2)
            inimigo['esp'] = False
            inimigos_medios()
        elif nome == 'Espectro':
            inimigo['vida'] = 50
            inimigo['atq'] = 7
            inimigo['def'] = 7 + (inimigo['lvl'] / 2)
            inimigo['dano'] = 7 + (inimigo['lvl'] / 2)
            inimigo['esp'] = False
            inimigos_medios()
        elif nome == 'Vampiro Menor':
            inimigo['vida'] = 125 + (2 * inimigo['lvl'])
            inimigo['atq'] = 15
            inimigo['def'] = 14 + (inimigo['lvl'] / 4)
            inimigo['dano'] = 10 + (inimigo['lvl'] / 2)
            inimigos_maiores()
        elif nome == 'Espectro do Pesadelo':
            inimigo['vida'] = 150
            inimigo['atq'] = 12
            inimigo['def'] = 17 
            inimigo['dano'] = 15 + (inimigo['lvl'] / 4)
            inimigos_maiores()
    #Rank Elevado:
    elif local == 'alto':
        if nome == 'Espectro Sangrento':
            inimigo['vida'] = 0
    #Rank Mestre:
    #Rank Aureo:
    
def selecionar_baixo():
    select = random.randint(1,100)
    loc = 'baixo'
    if select > 90:
        inimigos = ['Vampiro Menor','Espectro do Pesadelo']
    elif select <= 90 and select > 50:
        inimigos = ['Keeper','Cultista','Espectro']  
    elif select <= 50:
        inimigos = ['Carniçal','Lobo','Javali']    
    enemy = random.choice(inimigos)
    atribuir_inimigo(enemy,loc)
        
def selecionar_elevado():
    select = random.randint(1,100)
    loc = 'alto'
    if select > 90:
        inimigos = ['Lycano Cinzento','Serpe Alada']
    elif select <= 90 and select >= 56:
        inimigos = ['Lycano Noviço','Filho do Vazio','Bispo de Sangue']
    elif select > 10 and select < 56:
        inimigos = ['Espectro Sangrento','Cria do Kósmo']
    elif select <= 10:
        selecionar_baixo()
    enemy = random.choice(inimigos)
    atribuir_inimigo(enemy,loc)
        
def selecionar_mestre():
    select = random.randint(1,100)
    loc = 'mestre'
    if select > 90:
        inimigos = ['Lycano Berseker','Lycano Branquiço','Dragão Negro','Serpe Anciã']
    elif select <= 90 and select >= 56:
        inimigos = ['Papa de Sangue','Quetzal','Dragão Prateado']
    elif select > 10 and select < 56:
        inimigos = ['Espectro do Fim','Dragão Branco','Lorde Vampiro']
    elif select <= 10:
        selecionar_elevado()
    enemy = random.choice(inimigos)
    atribuir_inimigo(enemy,loc)
        
def selecionar_aureo():
    select = random.randint(1,100)
    loc = 'aureo'
    if select == 100:
        inimigos = ['Pólemos','Ígetis','Krymmenós']
    elif select >= 90 and select < 100:
        inimigos = ['Asómatos','Drákonos','Pagónia']
    elif select > 40 and select < 90:
        inimigos = ['Chrysós','Skótadi','Fós']
    elif select <= 40:
        selecionar_mestre()
    enemy = random.choice(inimigos)
    atribuir_inimigo(enemy,loc)
    
def selecionar_tier():
    if status['lvl'] <= 50:
        game['tier'] = 'Tier Baixo'
        inimigo['mult_rank'] = 1
        selecionar_baixo()
    elif status['lvl'] <= 100:
        game['tier'] = 'Tier Elevado'
        inimigo['mult_rank'] = 2
        selecionar_elevado()
    elif status['lvl'] <= 150:
        game['tier'] = 'Tier Mestre'
        inimigo['mult_rank'] = 3
        selecionar_mestre()
    elif status['lvl'] >= 200:
        game['tier'] = 'Tier Aureo'
        inimigo['mult_rank'] = 5
        selecionar_aureo()

def libra():
    os.system("cls")
    rol_libra = random.randint(1,20) + bonus['bonus_libra']
    drawline()
    if rol_libra > 16:
        print('\n\t\t!!!A Libra foi um sucesso!!!\n\tVocê consegue ler os seguintes status de seu inimigo:\n')
        print(f'Vida:\t\t{inimigo["vida"]}')
        print(f'Ataque\t\t{inimigo["atq"]}')
        print(f'Defesa\t\t{inimigo["def"]}')
        print(f'Dano Base:\t{inimigo["dano"]}\n')
    else:
        print('\n\tA Libra falhou!!!\nTente evoluir seu nível de libra...\n')
        turno_inimigo()
    drawline()
    os.system("pause")

def turno_player():
    rol_atq = random.randint(1,20) + equipamentos['atq_arma']
    rol_def = random.randint(1,20) + inimigo['def'] - ctrl_magias['debuff_ruby']
    pt_crit = rol_def + 16
    if rol_atq >= pt_crit:
        mensagem = 'Um acerto crítico!!!'
        dano = (status['lvl'] + equipamentos['dano_player']) * 2
    elif rol_atq > rol_def:
        mensagem = 'Você acertou o inimigo!'
        dano = random.randint(1,status['lvl']) + equipamentos['dano_player']
    else:
        mensagem = 'O inimigo se defendeu!'
        dano = 0
    inimigo['vida'] -= dano
    os.system("cls")
    drawline()
    print(f'\n\t{mensagem}\n\tDano causado: {dano}\n')
    drawline()
    os.system("pause")

def turno_inimigo():
    rol_atq = random.randint(1,20) + inimigo['atq']
    rol_def = random.randint(1,20) + equipamentos['def_armadura'] + bonus['bonus_rise']
    pt_crit = rol_def + 16
    if rol_atq >= pt_crit:
        mensagem = 'Um acerto crítico!!!'
        dano = (inimigo['lvl'] + inimigo['dano']) * 2
    elif rol_atq > rol_def:
        mensagem = 'O inimigo te acertou!'
        dano = random.randint(1,inimigo['lvl']) + inimigo['dano'] 
    else:
        mensagem = 'Você se defendeu!'
        dano = 0
    status['vida_atual'] -= dano

    #efeitos de magias
    if ctrl_magias['rise_cont'] != 0:
        ctrl_magias['rise_cont'] -= 1
    elif ctrl_magias['rise_cont'] == 0:
        bonus['bonus_rise'] = 0
    if ctrl_magias['ruby_cont'] != 0:
        ctrl_magias['ruby_cont'] -= 1
        corrosion = random.randint(1,status['lvl']) * (inimigo['mult_rank'] / 2)
        inimigo['vida'] -= corrosion
        os.system("cls")
        drawline()
        print(f'\n\tO inimigo está afetado pela Corrosão de Ruby!!!\n\tDano Sofrido: {corrosion}\n')
        drawline()
        os.system("pause")
    elif ctrl_magias['ruby_cont'] == 0:
        ctrl_magias['debuff_ruby'] = 0

    #mensagem final
    os.system("cls")
    drawline()
    print(f'\n\t{mensagem}\n\tDano sofrido: {dano}\n\tVida restante: {status["vida_atual"]}\n')
    drawline()
    os.system("pause")
    
def usar_itens():
    os.system("cls")
    drawline()
    print(f'\nPoções:\t\t{inventory["pot"]}')
    print(f'Elixires:\t{inventory["elx"]}')
    print(f'Kit de Captura: {inventory["kit_capt"]}\n')
    drawline()
    i = input('\n\tQual item deseja usar?\n->')
    #Utilizar os itens:
    if (i == 'pot' or i == 'poção' or i == 'pocao') and (inventory['pot'] > 0):
        heal = random.randint(1,6)
        inventory['pot'] -= 1
        status['vida_atual'] += (heal  + (status['lvl'] / 4)) * bonus['bonus_heal']
        if status['vida_atual'] > status['vida_total']:
            status['vida_atual'] = status['vida_total']
        os.system("cls")
        drawline()
        print(f'\n\n\tVocê curou {(heal + (status["lvl"] / 4)) * bonus["bonus_heal"]}\n\n')
        drawline()
        os.system("pause")
    elif (i == 'elixir' or i == 'elx') and (inventory['elx'] > 0):
        inventory['elx'] -= 1
        heal = random.randint(1,4)
        status['mana_atual'] += (heal  + (status['lvl'] / 4)) * bonus['bonus_elx']
        if status['mana_atual'] > status['mana_total']:
            status['mana_atual'] = status['mana_total']
        turno_inimigo()

def option_reviver():
    os.system("cls")
    drawline()
    if inventory['revive'] > 0:
        choose = input('\nVocê sente que ainda pode continuar, deseja voltar?...\n\t->')
        if choose == 'sim' or choose == 'ss' or choose == 's':
            inventory['revive'] -= 1
            pontos['revive'] += 1
            status['vida_atual'] = (status['vida_total'] / 4)
        else:
            retornar_dados()
    else:
        print('\nA sua jornada termina aqui, herói...\nMas talvez ainda não seja a hora de dar adeus...\nDesejo que seja "Até a próxima", e não mais um "adeus"...\n')
        drawline()
        os.system("pause")
        retornar_dados()

def conferir_exp(): 
    evoluiu = False
    while status['exp'] >= (15 + (status['lvl'] * inimigo['mult_rank'])):
        status['exp'] -= (15 + (status['lvl'] * inimigo['mult_rank']))
        status['lvl'] += 1
        status['pts_restantes'] += 3
        print('\nVocê Evoluiu!!!\n')
        evoluiu = True
    if evoluiu == True:
        os.system("pause")
        atribuir_pontos()
    calcular_arma()

def recompensas_combate():
    money = (random.randint(1,20) + bonus['bonus_din']) * inimigo['mult_din']
    exp_gain = random.randint(1,10) * inimigo['mult_exp']
    shard_chance = random.randint(1,100)
    if shard_chance <= 15:
        shard_gain = random.randint(1,5) * inimigo['mult_rank']
    else:
        shard_gain = 0
    inventory['shard'] += shard_gain
    status['exp'] += exp_gain
    inventory['din'] += money
    os.system("cls")
    drawline()
    print('\n\tVocê derrotou o inimigo!!!\n\tEspólios de batalha:')
    print(f'Moedas: {money}')
    print(f'Experiência: {exp_gain}')
    if shard_gain != 0:
        print(f'Fragmentos: {shard_gain}')
    print()
    drawline()
    os.system("pause")
    conferir_exp()

def pm_invalido():
    os.system("cls")
    drawline()
    print('\nQuantidade de PMs insuficientes!\n')
    drawline()
    os.system("pause")

def arma_invalida():
    os.system("cls")
    drawline()
    print('\nVocê não consegue conjurar esta magia usando essa arma!\n')
    drawline()
    os.system("pause")

def conferir_pm(slot):
    ctrl_magias['confere'] = True
    if slot == '1':
        if status['mana_atual'] < ctrl_magias['custo1']:
            ctrl_magias['confere'] = False
            pm_invalido()
        else:
            status['mana_atual'] -= ctrl_magias['custo1']
    elif slot == '2':
        if status['mana_atual'] < ctrl_magias['custo2']:
            ctrl_magias['confere'] = False
            pm_invalido()
        else:
            status['mana_atual'] -= ctrl_magias['custo2']

def msg_magia_dano(nome,dano):
    os.system("cls")
    drawline()
    print(f'\n\tVocê conjurou {nome}!!!\nO inimigo sofreu {dano} de dano!!!\n')
    drawline()
    os.system("pause")
    inimigo['vida'] -= dano

def efeitos_magias(slot):
    if slot == '1':
        i = 0
    elif slot == '2':
        i = 1
    escudos = ('dm_weapon_testing','escudo','amizade','sol prateado','lua dourada')
    corpo = ('dm_weapon_testing','espada','espada grande','ultra espada grande','lua dourada','lança','manopla','foice','chicote','machado')
    distancia = ('dm_weapon_testing','revolver','arco','escopeta','bazuca','ultra arco')
    catalisadores = ('dm_weapon_testing','varinha','cajado','sol prateado','orbe')
    
    if magias_equipadas[i] == 'bash':
        if equipamentos['arma'] not in escudos:
            arma_invalida()
        else:
            nome_magia = 'Bash'
            dano = ((atributos['for'] / 2) + (atributos['con'] / 2)) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()

    elif magias_equipadas[i] == 'dragon punch':
        if equipamentos['arma'] not in ('amizade', 'manopla','espada','escudo','chicote','sol prateado'):
            arma_invalida()
        else:
            nome_magia = 'Dragon Punch'
            dano = atributos['for'] * (random.randint(1,6)) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()

    elif magias_equipadas[i] == 'bolt':
        if equipamentos['arma'] not in catalisadores:
            arma_invalida()
        else:
            nome_magia = 'Elemental Bolt'
            dano = (atributos['int'] * 1.5) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()
        
    elif magias_equipadas[i] == 'perfurador':
        if equipamentos['arma'] not in ('arco','ultra arco'):
            arma_invalida()
        else:
            nome_magia = 'Flecha Elemental Perfuradora'
            dano = (3.5 * random.randint(1,atributos['dex'])) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()

    elif magias_equipadas[i] == 'turno extra':
        turno_player()
        turno_player()
        if inimigo['mult_rank'] >= 2:
            turno_player()
        if inimigo['mult_rank'] >= 5:
            turno_player()
        turno_inimigo()

    elif magias_equipadas[i] == 'rise':
        if equipamentos['arma'] not in escudos:
            arma_invalida()
        else:
            ctrl_magias['rise_cont'] = 2 + inimigo['mult_rank']
            bonus['bonus_rise'] = (atributos['int'] / 4) + (atributos['con'] / 4) + 3

    elif magias_equipadas[i] == 'meteoro':
        if equipamentos['arma'] not in catalisadores:
            arma_invalida()
        else:
            nome_magia = 'Chuva de Meteoros'
            dano = (atributos['int'] * 2.25) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()

    elif magias_equipadas[i] == 'disparo carregado':
        if equipamentos['arma'] not in distancia:
            arma_invalida()
        else:
            nome_magia = 'Disparo Energizado'
            dano = ((atributos['dex'] * 1.5) + (atributos['int'] * 0.5)) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()

    elif magias_equipadas[i] == 'ruby':
        if equipamentos['arma'] not in catalisadores:
            arma_invalida()
        else:
            ctrl_magias['ruby_cont'] = 2 + inimigo['mult_rank']
            ctrl_magias['debuff_ruby'] = (atributos['int'] / 4) * inimigo['mult_rank']
            if inimigo['vida'] > 0:
                turno_inimigo()
                
    elif magias_equipadas[i] == 'colheita':
        if equipamentos['arma'] not in corpo:
            arma_invalida()
        else:
            nome_magia = 'Colheita Sangrenta'
            dano = (status['vida_total'] - status['vida_atual']) / 3
            status['vida_atual'] += dano
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()
                
    elif magias_equipadas[i] == 'perfurador do dragão':
        if equipamentos['arma'] not in ('arco','ultra arco'):
            arma_invalida()
        else:
            nome_magia = 'Flecha Dracônica Perfuradora'
            dano = (5.75 * random.randint(1,atributos['dex'])) * inimigo['mult_rank']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()
        
    elif magias_equipadas[i] == 'ka boom':
        if equipamentos['arma'] not in ('bazuca'):
            arma_invalida()
        else:
            nome_magia = '1...2...3... Boooooooooooooooooom!'
            dano = (atributos['int'] * 7.5) + (atributos['dex'] * 1.25)
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()
                
    elif magias_equipadas[i] == 'queima roupa':
        if equipamentos['arma'] not in distancia:
            arma_invalida()
        else:
            nome_magia = 'Disparo Queima Roupa'
            dano = random.randint(5,atributos['con']) * atributos['dex']
            msg_magia_dano(nome_magia,dano)
            if inimigo['vida'] > 0:
                turno_inimigo()

def usar_magia():
    os.system("cls")
    drawline()
    print(f'\n\tMagias Equipadas:\n')
    print(f'Slot 1 - [{magias_equipadas[0].capitalize()}]')
    print(f'Descrição:\n{ctrl_magias["desc1"]}\n')
    print(f'Custo:   {ctrl_magias["custo1"]}\n\n')
    print(f'Slot 2 - [{magias_equipadas[1].capitalize()}]')
    print(f'Descrição:\n{ctrl_magias["desc2"]}\n')
    print(f'Custo:   {ctrl_magias["custo2"]}\n')
    drawline()
    choose = input('\nQual slot deseja castar?\n\t->')
    if choose == '1' or choose == '2':
        conferir_pm(choose)
        if ctrl_magias['confere'] == True:
            efeitos_magias(choose)
    else:
        os.system("cls")
        drawline()
        print('\nSlot de magia Inválido!!!\n')
        drawline()
        os.system("pause")

def combate_core():
    while True:
        os.system("cls")
        drawline()
        print(f'\n\t\tVocê encontrou um  {inimigo["nome"]} !!!\n\t\t   Nível {inimigo["lvl"]}    {game["tier"]}\n')
        drawline()
        print(f'\n\t[Vida Atual: {status["vida_atual"]}]')
        print(f'\t[Mana Atual: {status["mana_atual"]}]')
        if ctrl_magias['rise_cont'] != 0:
            print(f'\t[Turnos Restantes (Rise): {ctrl_magias["rise_cont"]}]')
            print(f'\t[Bônus do Rise: {bonus["bonus_rise"]}]')
        if ctrl_magias['ruby_cont'] != 0:
            print(f'\t[Turnos Restantes (Ruby): {ctrl_magias["ruby_cont"]}]')
            print(f'\t[Debuff do Ruby: {ctrl_magias["debuff_ruby"]}]')
        choice = input('\n\tO que deseja fazer?\n\n[1] - Lutar\n[2] - Castar Magia\n[3] - Libra\n[4] - Utilizar Itens\n[5] - Fugir\n\n->')
        if choice == '1':
            turno_player()
            if inimigo['vida'] > 0:
                turno_inimigo()
        elif choice == '2':
            usar_magia()
        elif choice == '3':
            libra()
        elif choice == '4':
            usar_itens()
        elif choice == '5':
            fuga = random.randint(1,20)
            if game['tier'] == 'Tier Baixo':
                fuga += 7
            if fuga >  13:
                break
            else:
                os.system("cls")
                drawline()
                print('\n\tVocê não conseguiu fugir!\n')
                drawline()
                os.system("pause")
                turno_inimigo()
        if inimigo['vida'] <= 0 or status['vida_atual'] <= 0:
            ctrl_magias['rise_cont'] = 0
            ctrl_magias['ruby_cont'] = 0
            break
    if status['vida_atual'] <= 0:
        option_reviver()
    elif status['vida_atual'] > 0 and inimigo['vida'] <= 0:
        recompensas_combate()

def retornar_dados():
    os.system("cls")
    print(f'Revives Utilizados: {pontos["revive"]}')
    os.system("pause")
    game['game_over'] = 1

import random
import os
#Main Code
#--Variáveis
atributos = {'for': 0,'dex': 0,'con': 0,'int': 0}
status = {'pts_restantes': 12,'vida_total': 0,'vida_atual': 0,'mana_total': 0,'mana_atual': 0,'lvl': 1,'exp': 0,'lvl_harvest': 1,'exp_harvest': 0}
equipamentos = {'atq_arma': 1,'def_armadura': 1,'dano_player': 0,'arma': ''}
inventory = {'din': 30,'shard': 0,'pot': 5,'elx': 2,'revive': 1,'kit_capt': 0,'erva': 0,'fruta': 0,'minerio': 0,'madeira': 0,'cristal': 0}
game = {'game_over': 0,'tier': ' '}
lista_de_armas = ['arco','espada','espada grande','lança','cajado','varinha','grimório','escudo','manoplas','orbe','foice','chicote','amizade','pistola','revolver','machado','escopeta','bazuca','ultra espada grande','ultra arco','sol prateado','lua dourada','dm_weapon_testing']
bonus = {'bonus_atq': 0,'bonus_def': 0,'bonus_harvest': 1,'bonus_libra': 0,'bonus_heal': 1,'bonus_elx': 1,'bonus_din': 0,'bonus_rise': 0}
controle_loja = {'preço': 0,'check': 0,'harvest': False}
magias_equipadas = ['-None-','-None-']
inimigo = {'nome': '','lvl': 0,'atq': 0,'def': 0,'vida': 0,'dano': 0,'mult_rank': 0,'mult_exp': 0,'mult_din': 0,'mult_shard': 0,'esp': False,'s_esp': False}
ctrl_magias = {'custo1': 0,'custo2': 0,'desc1': '','desc2': '','confere': True,'rise_cont': 0,'ruby_cont': 0,'debuff_ruby': 0}
magias = []
armas = []
pontos = {'revive': 0}

#--Main Cicle
atribuir_pontos()
selecionar_arma()
while game['game_over'] == 0:
    os.system("cls")
    drawline()
    print('Você está ao pé de uma fogueira, vagalumes rodeiam o céu estrelado...\n')
    print('O que deseja fazer?\n\t-Caçar\n\t-Descansar\n\t-Buscar\n\t-Inventário\n\t-Status\n\t-Manufaturar item\n\t-Comprar\n\t-Magias\n\t-Desistir')
    escolha = input('->').lower()
    if escolha == 'descansar' or escolha == 'd':
        descanso()
    elif escolha == 'caçar' or escolha == 'c':
        selecionar_tier()
        combate_core()
    elif escolha == 'buscar' or escolha == 'b':
        harvest()
    elif escolha == 'inventario' or escolha == 'inv':
        mostrar_inventario()
    elif escolha == 'status' or escolha == 'stts':
        mostrar_status()
    elif escolha == 'comprar' or escolha == 'loja':
        loja()
    elif escolha == 'manufaturar item' or escolha == 'manufatura' or escolha == 'craft':
        craft_item()
    elif escolha == 'arma':
        trocar_arma()
    elif escolha == 'magias':
        trocar_magia()
    elif escolha == 'desistir':
        retornar_dados()
    elif escolha == 'system_comando':
        cheats()
    elif escolha == 'refresh':
        conferir_exp()