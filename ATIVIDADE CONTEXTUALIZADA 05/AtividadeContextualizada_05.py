#Atividade Contextualizada 05

#QUESTÃO 1, letra a

listanome = ['regiao','estado','municipio','coduf','codmun','codRegiaoSaude','nomeRegiaoSaude','data','semanaEpi','populacaoTCU2019','casosAcumulado','casosNovos','obitosAcumulado','obitosNovos','Recuperadosnovos','emAcompanhamentoNovos','interior/metropolitana']
lista = [['Norte', 'AC', 'Sena Madureira', 12, 120050, 12002, 'BAIXO ACRE E PURUS', '2020-04-11 00:00:00', 15, 45848.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Rodrigues Alves', 12, 120042, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-07-04 00:00:00', 27, 18930.0, 97, 0, 4, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '2020-04-25 00:00:00', 17, 17722.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Piranhas', 27, 270710, 27010, '10ª REGIAO DE SAUDE', '2020-07-10 00:00:00', 28, 25039.0, 45, 0, 2, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Itamarati', 13, 130195, 13007, 'REGIONAL JURUA', '2020-06-11 00:00:00', 24, 7851.0, 78, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Amaturá', 13, 130006, 13009, 'ALTO SOLIMOES', '2020-07-11 00:00:00', 28, 11536.0, 464, 8, 8, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '2020-07-02 00:00:00', 27, 121364.0, 4090, 36, 66, 1, ' ', ' ', 1.0], ['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '2020-08-25 00:00:00', 35, 7780.0, 535, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Lajedinho', 29, 291900, 29011, 'ITABERABA', '2020-07-29 00:00:00', 31, 3783.0, 3, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'São Domingos', 29, 292895, 29025, 'SERRINHA', '2020-03-28 00:00:00', 13, 9058.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Apuiarés', 23, 230090, 23002, '2ª REGIAO CAUCAIA', '2020-05-24 00:00:00', 22, 14600.0, 19, 0, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Uruoca', 23, 231390, 23011, '11ª REGIAO SOBRAL', '2020-07-30 00:00:00', 31, 13840.0, 453, 16, 15, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-06-05 00:00:00', 23, 3015268.0, 14208, 1285, 202, 6, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-02 00:00:00', 14, 3015268.0, 370, 15, 4, 1, ' ', ' ', 1.0], ['Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '2020-06-10 00:00:00', 24, 30586.0, 108, 4, 7, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-06-03 00:00:00', 23, 30867.0, 43, 1, 3, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Nova Roma', 52, 521490, 52007, 'NORDESTE II', '2020-08-10 00:00:00', 33, 3264.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Castelândia', 52, 520505, 52015, 'SUDOESTE I', '2020-05-26 00:00:00', 22, 3435.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Coroatá', 21, 210360, 21007, 'CODO', '2020-06-15 00:00:00', 25, 65296.0, 238, 0, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Vitorino Freire', 21, 211300, 21002, 'BACABAL', '2020-08-11 00:00:00', 33, 31523.0, 1392, 12, 24, 2, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Taquaraçu de Minas', 31, 316830, 31016, 'BELO HORIZONTE/ NOVA LIMA/ CAETE ', '2020-05-23 00:00:00', 21, 4077.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Sudeste', 'MG', 'Andrelândia', 31, 310280, 31090, 'LIMA DUARTE', '2020-08-18 00:00:00', 34, 12224.0, 49, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Dourados', 50, 500370, 50003, 'DOURADOS', '2020-06-01 00:00:00', 23, 222949.0, 306, 27, 2, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Paranhos', 50, 500635, 50003, 'DOURADOS', '2020-04-01 00:00:00', 14, 14228.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Rondonópolis', 51, 510760, 51013, 'SUL MATOGROSSENSE', '2020-06-14 00:00:00', 25, 232491.0, 497, 52, 12, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Feliz Natal', 51, 510370, 51014, 'TELES PIRES', '2020-05-30 00:00:00', 22, 14192.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Anajás', 15, 150070, 15014, 'MARAJO II', '2020-05-08 00:00:00', 19, 29277.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Breves', 15, 150180, 15014, 'MARAJO II', '2020-05-23 00:00:00', 21, 102701.0, 432, 7, 50, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Guarabira', 25, 250630, 25002, '2ª REGIAO', '2020-05-30 00:00:00', 22, 58833.0, 557, 12, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-07-29 00:00:00', 31, 22819.0, 309, 11, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Salgadinho', 26, 261210, 26006, 'LIMOEIRO', '2020-04-21 00:00:00', 17, 10919.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Terra Nova', 26, 261520, 26011, 'SALGUEIRO', '2020-07-16 00:00:00', 29, 10096.0, 6, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Currais', 22, 220323, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-04-18 00:00:00', 16, 4954.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Corrente', 22, 220290, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-05-01 00:00:00', 18, 26644.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Sabáudia', 41, 412270, 41016, '16ª RS APUCARANA', '2020-05-10 00:00:00', 20, 6827.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Porto Rico', 41, 412020, 41014, '14ª RS PARANAVAI', '2020-08-03 00:00:00', 32, 2559.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Santa Maria Madalena', 33, 330460, 33009, 'SERRANA', '2020-07-28 00:00:00', 31, 10404.0, 75, 0, 2, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Seropédica', 33, 330555, 33005, 'METROPOLITANA I', '2020-06-26 00:00:00', 26, 82312.0, 429, 4, 23, 0, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Pendências', 24, 240990, 24008, '8ª REGIAO DE SAUDE - ACU', '2020-06-16 00:00:00', 25, 15129.0, 93, 6, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'São José do Campestre', 24, 241230, 24005, '5ª REGIAO DE SAUDE - SANTA CRUZ', '2020-05-25 00:00:00', 22, 12856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-20 00:00:00', 17, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Alvorada DOeste', 11, 110034, 11003, 'CENTRAL', '2020-07-01 00:00:00', 27, 14411.0, 18, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '2020-05-18 00:00:00', 21, 21926.0, 12, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '2020-08-19 00:00:00', 34, 11950.0, 237, 3, 4, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Jari', 43, 431113, 43002, 'REGIAO 02', '2020-08-12 00:00:00', 33, 3503.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Vila Flores', 43, 432330, 43025, 'REGIAO 25', '2020-08-23 00:00:00', 35, 3385.0, 77, 5, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Porto Belo', 42, 421350, 42005, 'FOZ DO RIO ITAJAI', '2020-06-06 00:00:00', 23, 21388.0, 26, 2, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Presidente Nereu', 42, 421410, 42004, 'ALTO VALE DO ITAJAI', '2020-04-13 00:00:00', 16, 2287.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Nossa Senhora Aparecida', 28, 280445, 28003, 'ITABAIANA', '2020-06-11 00:00:00', 24, 8796.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Japoatã', 28, 280340, 28007, 'PROPRIA', '2020-04-28 00:00:00', 18, 13434.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sud Mennucci', 35, 355230, 35022, 'LAGOS DO DRS II', '2020-06-11 00:00:00', 24, 7718.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sandovalina', 35, 354550, 35112, 'ALTA SOROCABANA', '2020-06-13 00:00:00', 24, 4302.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Gurupi', 17, 170950, 17005, 'ILHA DO BANANAL', '2020-07-23 00:00:00', 30, 86647.0, 717, 39, 7, 1, ' ', ' ', 0.0], ['Norte', 'TO', 'Riachinho', 17, 171855, 17002, 'BICO DO PAPAGAIO', '2020-05-20 00:00:00', 21, 4645.0, 2, 0, 0, 0, ' ', ' ', 0.0]]
tupla = (('Norte', 'AC', 'Sena Madureira', 12, 120050, 12002, 'BAIXO ACRE E PURUS', '2020-04-11 00:00:00', 15, 45848.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'AC', 'Rodrigues Alves', 12, 120042, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-07-04 00:00:00', 27, 18930.0, 97, 0, 4, 0, ' ', ' ', 0.0), ('Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '2020-04-25 00:00:00', 17, 17722.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'AL', 'Piranhas', 27, 270710, 27010, '10ª REGIAO DE SAUDE', '2020-07-10 00:00:00', 28, 25039.0, 45, 0, 2, 0, ' ', ' ', 0.0), ('Norte', 'AM', 'Itamarati', 13, 130195, 13007, 'REGIONAL JURUA', '2020-06-11 00:00:00', 24, 7851.0, 78, 0, 1, 0, ' ', ' ', 0.0), ('Norte', 'AM', 'Amaturá', 13, 130006, 13009, 'ALTO SOLIMOES', '2020-07-11 00:00:00', 28, 11536.0, 464, 8, 8, 0, ' ', ' ', 0.0), ('Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '2020-07-02 00:00:00', 27, 121364.0, 4090, 36, 66, 1, ' ', ' ', 1.0), ('Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '2020-08-25 00:00:00', 35, 7780.0, 535, 0, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'BA', 'Lajedinho', 29, 291900, 29011, 'ITABERABA', '2020-07-29 00:00:00', 31, 3783.0, 3, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'BA', 'São Domingos', 29, 292895, 29025, 'SERRINHA', '2020-03-28 00:00:00', 13, 9058.0, 1, 1, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'CE', 'Apuiarés', 23, 230090, 23002, '2ª REGIAO CAUCAIA', '2020-05-24 00:00:00', 22, 14600.0, 19, 0, 5, 0, ' ', ' ', 0.0), ('Nordeste', 'CE', 'Uruoca', 23, 231390, 23011, '11ª REGIAO SOBRAL', '2020-07-30 00:00:00', 31, 13840.0, 453, 16, 15, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-06-05 00:00:00', 23, 3015268.0, 14208, 1285, 202, 6, ' ', ' ', 1.0), ('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-02 00:00:00', 14, 3015268.0, 370, 15, 4, 1, ' ', ' ', 1.0), ('Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '2020-06-10 00:00:00', 24, 30586.0, 108, 4, 7, 0, ' ', ' ', 0.0), ('Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-06-03 00:00:00', 23, 30867.0, 43, 1, 3, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'GO', 'Nova Roma', 52, 521490, 52007, 'NORDESTE II', '2020-08-10 00:00:00', 33, 3264.0, 1, 1, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'GO', 'Castelândia', 52, 520505, 52015, 'SUDOESTE I', '2020-05-26 00:00:00', 22, 3435.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'MA', 'Coroatá', 21, 210360, 21007, 'CODO', '2020-06-15 00:00:00', 25, 65296.0, 238, 0, 2, 0, ' ', ' ', 0.0), ('Nordeste', 'MA', 'Vitorino Freire', 21, 211300, 21002, 'BACABAL', '2020-08-11 00:00:00', 33, 31523.0, 1392, 12, 24, 2, ' ', ' ', 0.0), ('Sudeste', 'MG', 'Taquaraçu de Minas', 31, 316830, 31016, 'BELO HORIZONTE/ NOVA LIMA/ CAETE ', '2020-05-23 00:00:00', 21, 4077.0, 0, 0, 0, 0, ' ', ' ', 1.0), ('Sudeste', 'MG', 'Andrelândia', 31, 310280, 31090, 'LIMA DUARTE', '2020-08-18 00:00:00', 34, 12224.0, 49, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MS', 'Dourados', 50, 500370, 50003, 'DOURADOS', '2020-06-01 00:00:00', 23, 222949.0, 306, 27, 2, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MS', 'Paranhos', 50, 500635, 50003, 'DOURADOS', '2020-04-01 00:00:00', 14, 14228.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MT', 'Rondonópolis', 51, 510760, 51013, 'SUL MATOGROSSENSE', '2020-06-14 00:00:00', 25, 232491.0, 497, 52, 12, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MT', 'Feliz Natal', 51, 510370, 51014, 'TELES PIRES', '2020-05-30 00:00:00', 22, 14192.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'PA', 'Anajás', 15, 150070, 15014, 'MARAJO II', '2020-05-08 00:00:00', 19, 29277.0, 1, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'PA', 'Breves', 15, 150180, 15014, 'MARAJO II', '2020-05-23 00:00:00', 21, 102701.0, 432, 7, 50, 0, ' ', ' ', 0.0), ('Nordeste', 'PB', 'Guarabira', 25, 250630, 25002, '2ª REGIAO', '2020-05-30 00:00:00', 22, 58833.0, 557, 12, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-07-29 00:00:00', 31, 22819.0, 309, 11, 2, 0, ' ', ' ', 0.0), ('Nordeste', 'PE', 'Salgadinho', 26, 261210, 26006, 'LIMOEIRO', '2020-04-21 00:00:00', 17, 10919.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'PE', 'Terra Nova', 26, 261520, 26011, 'SALGUEIRO', '2020-07-16 00:00:00', 29, 10096.0, 6, 0, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'PI', 'Currais', 22, 220323, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-04-18 00:00:00', 16, 4954.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'PI', 'Corrente', 22, 220290, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-05-01 00:00:00', 18, 26644.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'PR', 'Sabáudia', 41, 412270, 41016, '16ª RS APUCARANA', '2020-05-10 00:00:00', 20, 6827.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'PR', 'Porto Rico', 41, 412020, 41014, '14ª RS PARANAVAI', '2020-08-03 00:00:00', 32, 2559.0, 2, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'RJ', 'Santa Maria Madalena', 33, 330460, 33009, 'SERRANA', '2020-07-28 00:00:00', 31, 10404.0, 75, 0, 2, 0, ' ', ' ', 0.0), ('Sudeste', 'RJ', 'Seropédica', 33, 330555, 33005, 'METROPOLITANA I', '2020-06-26 00:00:00', 26, 82312.0, 429, 4, 23, 0, ' ', ' ', 1.0), ('Nordeste', 'RN', 'Pendências', 24, 240990, 24008, '8ª REGIAO DE SAUDE - ACU', '2020-06-16 00:00:00', 25, 15129.0, 93, 6, 5, 0, ' ', ' ', 0.0), ('Nordeste', 'RN', 'São José do Campestre', 24, 241230, 24005, '5ª REGIAO DE SAUDE - SANTA CRUZ', '2020-05-25 00:00:00', 22, 12856.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-20 00:00:00', 17, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RO', 'Alvorada DOeste', 11, 110034, 11003, 'CENTRAL', '2020-07-01 00:00:00', 27, 14411.0, 18, 0, 1, 0, ' ', ' ', 0.0), ('Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '2020-05-18 00:00:00', 21, 21926.0, 12, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '2020-08-19 00:00:00', 34, 11950.0, 237, 3, 4, 0, ' ', ' ', 0.0), ('Sul', 'RS', 'Jari', 43, 431113, 43002, 'REGIAO 02', '2020-08-12 00:00:00', 33, 3503.0, 2, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'RS', 'Vila Flores', 43, 432330, 43025, 'REGIAO 25', '2020-08-23 00:00:00', 35, 3385.0, 77, 5, 1, 0, ' ', ' ', 0.0), ('Sul', 'SC', 'Porto Belo', 42, 421350, 42005, 'FOZ DO RIO ITAJAI', '2020-06-06 00:00:00', 23, 21388.0, 26, 2, 1, 0, ' ', ' ', 0.0), ('Sul', 'SC', 'Presidente Nereu', 42, 421410, 42004, 'ALTO VALE DO ITAJAI', '2020-04-13 00:00:00', 16, 2287.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'SE', 'Nossa Senhora Aparecida', 28, 280445, 28003, 'ITABAIANA', '2020-06-11 00:00:00', 24, 8796.0, 5, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'SE', 'Japoatã', 28, 280340, 28007, 'PROPRIA', '2020-04-28 00:00:00', 18, 13434.0, 1, 1, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'SP', 'Sud Mennucci', 35, 355230, 35022, 'LAGOS DO DRS II', '2020-06-11 00:00:00', 24, 7718.0, 5, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'SP', 'Sandovalina', 35, 354550, 35112, 'ALTA SOROCABANA', '2020-06-13 00:00:00', 24, 4302.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'TO', 'Gurupi', 17, 170950, 17005, 'ILHA DO BANANAL', '2020-07-23 00:00:00', 30, 86647.0, 717, 39, 7, 1, ' ', ' ', 0.0), ('Norte', 'TO', 'Riachinho', 17, 171855, 17002, 'BICO DO PAPAGAIO', '2020-05-20 00:00:00', 21, 4645.0, 2, 0, 0, 0, ' ', ' ', 0.0))
tuplanome = ('regiao','estado','municipio','coduf','codmun','codRegiaoSaude','nomeRegiaoSaude','data','semanaEpi','populacaoTCU2019','casosAcumulado','casosNovos','obitosAcumulado','obitosNovos','Recuperadosnovos','emAcompanhamentoNovos','interior/metropolitana')

#Término do item a


#QUESTÃO 1, letra b

print('Total de casos para o estado do Rio de Janeiro (Lista):')
print('Primeiro dado da lista:')
print(lista[36][10])
print('Segundo dado da lista:')
print(lista[37][10])
print('')
print('Total de casos para o estado do Rio de Janeiro (Tupla):')
print('Primeiro dado da tupla:')
print(tupla[36][10])
print('Segundo dado da lista:')
print(tupla[37][10])

#Término do item b


#QUESTÃO 1, letra c

print('Óbitos acumulados:')
print('')
print(lista[0][1],':',lista[0][12])
print(lista[1][1],':',lista[1][12])
print(lista[2][1],':',lista[2][12])
print(lista[3][1],':',lista[3][12])
print(lista[4][1],':',lista[4][12])
print(lista[5][1],':',lista[5][12])
print(lista[6][1],':',lista[6][12])
print(lista[7][1],':',lista[7][12])
print(lista[8][1],':',lista[8][12])
print(lista[9][1],':',lista[9][12])
print(lista[10][1],':',lista[10][12])
print(lista[11][1],':',lista[11][12])
print(lista[12][1],':',lista[12][12])
print(lista[13][1],':',lista[13][12])
print(lista[14][1],':',lista[14][12])
print(lista[15][1],':',lista[15][12])
print(lista[16][1],':',lista[16][12])
print(lista[17][1],':',lista[17][12])
print(lista[18][1],':',lista[18][12])
print(lista[19][1],':',lista[19][12])
print(lista[20][1],':',lista[20][12])
print(lista[21][1],':',lista[21][12])
print(lista[22][1],':',lista[22][12])
print(lista[23][1],':',lista[23][12])
print(lista[24][1],':',lista[24][12])
print(lista[25][1],':',lista[25][12])
print(lista[26][1],':',lista[26][12])
print(lista[27][1],':',lista[27][12])
print(lista[28][1],':',lista[28][12])
print(lista[29][1],':',lista[29][12])
print(lista[30][1],':',lista[30][12])
print(lista[31][1],':',lista[31][12])
print(lista[32][1],':',lista[32][12])
print(lista[33][1],':',lista[33][12])
print(lista[34][1],':',lista[34][12])
print(lista[35][1],':',lista[35][12])
print(lista[36][1],':',lista[36][12])
print(lista[37][1],':',lista[37][12])
print(lista[38][1],':',lista[38][12])
print(lista[39][1],':',lista[39][12])
print(lista[40][1],':',lista[40][12])
print(lista[41][1],':',lista[41][12])
print(lista[42][1],':',lista[42][12])
print(lista[43][1],':',lista[43][12])
print(lista[44][1],':',lista[44][12])
print(lista[45][1],':',lista[45][12])
print(lista[46][1],':',lista[46][12])
print(lista[47][1],':',lista[47][12])
print(lista[48][1],':',lista[48][12])
print(lista[49][1],':',lista[49][12])
print(lista[50][1],':',lista[50][12])
print(lista[51][1],':',lista[51][12])
print(lista[52][1],':',lista[52][12])
print(lista[53][1],':',lista[53][12])

#Término do item c


#QUESTÃO 1, letra d)

print('Dados corrigidos (Lista):')
lista[28][13]=10
lista[29][13]=10
print(lista[28][13])
print(lista[29][13])

print('Dados corrigidos (Tupla):')
tupla[28][13]=10
tupla[29][13]=10
print(tupla[28][13])
print(tupla[29][13])

#Término do item d


#QUESTÃO 1, letra e

'''
A operação de correção da letra d) só foi possível para lista, pois a tupla não aceita alterações em sua composição após ser escrita. Assim, não é possível alterar campos da tupla, só da lista.  
'''

#Término do item e


#QUESTÃO 1, letra f

lista = [['Norte', 'AC', 'Sena Madureira', 12, 120050, 12002, 'BAIXO ACRE E PURUS', '2020-04-11 00:00:00', 15, 45848.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Rodrigues Alves', 12, 120042, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-07-04 00:00:00', 27, 18930.0, 97, 0, 4, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '2020-04-25 00:00:00', 17, 17722.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Piranhas', 27, 270710, 27010, '10ª REGIAO DE SAUDE', '2020-07-10 00:00:00', 28, 25039.0, 45, 0, 2, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Itamarati', 13, 130195, 13007, 'REGIONAL JURUA', '2020-06-11 00:00:00', 24, 7851.0, 78, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Amaturá', 13, 130006, 13009, 'ALTO SOLIMOES', '2020-07-11 00:00:00', 28, 11536.0, 464, 8, 8, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '2020-07-02 00:00:00', 27, 121364.0, 4090, 36, 66, 1, ' ', ' ', 1.0], ['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '2020-08-25 00:00:00', 35, 7780.0, 535, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Lajedinho', 29, 291900, 29011, 'ITABERABA', '2020-07-29 00:00:00', 31, 3783.0, 3, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'São Domingos', 29, 292895, 29025, 'SERRINHA', '2020-03-28 00:00:00', 13, 9058.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Apuiarés', 23, 230090, 23002, '2ª REGIAO CAUCAIA', '2020-05-24 00:00:00', 22, 14600.0, 19, 0, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Uruoca', 23, 231390, 23011, '11ª REGIAO SOBRAL', '2020-07-30 00:00:00', 31, 13840.0, 453, 16, 15, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-06-05 00:00:00', 23, 3015268.0, 14208, 1285, 202, 6, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-02 00:00:00', 14, 3015268.0, 370, 15, 4, 1, ' ', ' ', 1.0], ['Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '2020-06-10 00:00:00', 24, 30586.0, 108, 4, 7, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-06-03 00:00:00', 23, 30867.0, 43, 1, 3, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Nova Roma', 52, 521490, 52007, 'NORDESTE II', '2020-08-10 00:00:00', 33, 3264.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Castelândia', 52, 520505, 52015, 'SUDOESTE I', '2020-05-26 00:00:00', 22, 3435.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Coroatá', 21, 210360, 21007, 'CODO', '2020-06-15 00:00:00', 25, 65296.0, 238, 0, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Vitorino Freire', 21, 211300, 21002, 'BACABAL', '2020-08-11 00:00:00', 33, 31523.0, 1392, 12, 24, 2, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Taquaraçu de Minas', 31, 316830, 31016, 'BELO HORIZONTE/ NOVA LIMA/ CAETE ', '2020-05-23 00:00:00', 21, 4077.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Sudeste', 'MG', 'Andrelândia', 31, 310280, 31090, 'LIMA DUARTE', '2020-08-18 00:00:00', 34, 12224.0, 49, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Dourados', 50, 500370, 50003, 'DOURADOS', '2020-06-01 00:00:00', 23, 222949.0, 306, 27, 2, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Paranhos', 50, 500635, 50003, 'DOURADOS', '2020-04-01 00:00:00', 14, 14228.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Rondonópolis', 51, 510760, 51013, 'SUL MATOGROSSENSE', '2020-06-14 00:00:00', 25, 232491.0, 497, 52, 12, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Feliz Natal', 51, 510370, 51014, 'TELES PIRES', '2020-05-30 00:00:00', 22, 14192.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Anajás', 15, 150070, 15014, 'MARAJO II', '2020-05-08 00:00:00', 19, 29277.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Breves', 15, 150180, 15014, 'MARAJO II', '2020-05-23 00:00:00', 21, 102701.0, 432, 7, 50, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Guarabira', 25, 250630, 25002, '2ª REGIAO', '2020-05-30 00:00:00', 22, 58833.0, 557, 12, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-07-29 00:00:00', 31, 22819.0, 309, 11, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Salgadinho', 26, 261210, 26006, 'LIMOEIRO', '2020-04-21 00:00:00', 17, 10919.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Terra Nova', 26, 261520, 26011, 'SALGUEIRO', '2020-07-16 00:00:00', 29, 10096.0, 6, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Currais', 22, 220323, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-04-18 00:00:00', 16, 4954.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Corrente', 22, 220290, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-05-01 00:00:00', 18, 26644.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Sabáudia', 41, 412270, 41016, '16ª RS APUCARANA', '2020-05-10 00:00:00', 20, 6827.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Porto Rico', 41, 412020, 41014, '14ª RS PARANAVAI', '2020-08-03 00:00:00', 32, 2559.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Santa Maria Madalena', 33, 330460, 33009, 'SERRANA', '2020-07-28 00:00:00', 31, 10404.0, 75, 0, 2, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Seropédica', 33, 330555, 33005, 'METROPOLITANA I', '2020-06-26 00:00:00', 26, 82312.0, 429, 4, 23, 0, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Pendências', 24, 240990, 24008, '8ª REGIAO DE SAUDE - ACU', '2020-06-16 00:00:00', 25, 15129.0, 93, 6, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'São José do Campestre', 24, 241230, 24005, '5ª REGIAO DE SAUDE - SANTA CRUZ', '2020-05-25 00:00:00', 22, 12856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-20 00:00:00', 17, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Alvorada DOeste', 11, 110034, 11003, 'CENTRAL', '2020-07-01 00:00:00', 27, 14411.0, 18, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '2020-05-18 00:00:00', 21, 21926.0, 12, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '2020-08-19 00:00:00', 34, 11950.0, 237, 3, 4, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Jari', 43, 431113, 43002, 'REGIAO 02', '2020-08-12 00:00:00', 33, 3503.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Vila Flores', 43, 432330, 43025, 'REGIAO 25', '2020-08-23 00:00:00', 35, 3385.0, 77, 5, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Porto Belo', 42, 421350, 42005, 'FOZ DO RIO ITAJAI', '2020-06-06 00:00:00', 23, 21388.0, 26, 2, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Presidente Nereu', 42, 421410, 42004, 'ALTO VALE DO ITAJAI', '2020-04-13 00:00:00', 16, 2287.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Nossa Senhora Aparecida', 28, 280445, 28003, 'ITABAIANA', '2020-06-11 00:00:00', 24, 8796.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Japoatã', 28, 280340, 28007, 'PROPRIA', '2020-04-28 00:00:00', 18, 13434.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sud Mennucci', 35, 355230, 35022, 'LAGOS DO DRS II', '2020-06-11 00:00:00', 24, 7718.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sandovalina', 35, 354550, 35112, 'ALTA SOROCABANA', '2020-06-13 00:00:00', 24, 4302.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Gurupi', 17, 170950, 17005, 'ILHA DO BANANAL', '2020-07-23 00:00:00', 30, 86647.0, 717, 39, 7, 1, ' ', ' ', 0.0], ['Norte', 'TO', 'Riachinho', 17, 171855, 17002, 'BICO DO PAPAGAIO', '2020-05-20 00:00:00', 21, 4645.0, 2, 0, 0, 0, ' ', ' ', 0.0]]

listaMunicipios = [['Norte', 'RR', 'Amajari', 14, 140002, 14001, 'CENTRO NORTE', '18/08/2020', 34, 12796, 277, 0, 6, 0, ' ', ' ', 0], ['Norte', 'RR', 'Alto Alegre', 14, 140005, 14001, 'CENTRO NORTE', '18/08/2020', 34, 15510, 493, 25, 14, 0, ' ', ' ', 1], ['Norte', 'RR', 'Boa Vista', 14, 140010, 14001, 'CENTRO NORTE', '18/08/2020', 34, 399213, 29978, 408, 444, 5, ' ', ' ', 1],['Norte', 'RR', 'Bonfim', 14, 140015, 14001, 'CENTRO NORTE', '18/08/2020', 34, 12409, 609, 20, 11, 0, ' ', ' ', 1],['Norte', 'RR', 'Cantá', 14, 140017, 14001, 'CENTRO NORTE', '18/08/2020', 34, 18335, 839, 7, 9, 0, ' ', ' ', 1], ['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '18/08/2020', 34, 21926, 750, 2, 8, 0, ' ', ' ', 0], ['Norte', 'RR', 'Caroebe', '14', 140023, 14002, 'SUL', '18/08/2020', 34, 10169, 832, 4, 4, 0, ' ', ' ', 0],['Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '18/08/2020', 34, 11950, 234, 1, 4, 0, ' ', ' ', 0],['Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '18/08/2020', 34, 17853, 1036, 19, 12, 0, ' ', ' ', 1],['Norte', 'RR', 'Normandia', 14, 140040, 14001, 'CENTRO NORTE', '18/08/2020', 34, 11290, 272, 0, 9, 0, ' ', ' ', 0], ['Norte', 'RR', 'Pacaraima', 14, 140045, 14001, 'CENTRO NORTE', '18/08/2020', 34, 17401, 1246, 17, 26, 1, ' ', ' ', 0], ['Norte', 'RR', 'Rorainópolis', 14, 140047, 14002, 'SUL', '18/08/2020', 34, 30163, 1401, 8, 20, 0, ' ', ' ', 0], ['Norte', 'RR', 'São João da Baliza', 14, 140050, 14002, 'SUL', '18/08/2020', 34, 8201, 736, 0, 3, 0, ' ', ' ', 0],['Norte', 'RR', 'São Luiz', 14, 140060, 14002, 'SUL', '18/08/2020', 34, 7986, 197, 2, 2, 0, ' ', ' ', 0], ['Norte', 'RR', 'Uiramutã', 14, 140070, 14001, 'CENTRO NORTE', '18/08/2020', 34, 10559, 596, 2, 2, 0, ' ', ' ', 0]]

lista.append(listaMunicipios)

print(lista)

#Término do item f


#listaEstado = ['Norte', 'RR', ' ', 14, ' ', ' ', ' ', '18/08/2020', 34, 605761, 40183, 518, 574, 6, ' ', ' ', ' ']


#QUESTÃO 1, letra g

lista.remove([0][1])
lista.remove([1][1])
lista.remove([2][1])
lista.remove([3][1])
lista.remove([4][1])
lista.remove([5][1])
lista.remove([6][1])
lista.remove([7][1])
lista.remove([8][1])
lista.remove([9][1])
lista.remove([10][1])
lista.remove([11][1])
lista.remove([12][1])
lista.remove([13][1])
lista.remove([14][1])
lista.remove([15][1])
lista.remove([16][1])
lista.remove([17][1])
lista.remove([18][1])
lista.remove([19][1])
lista.remove([20][1])
lista.remove([21][1])
lista.remove([22][1])
lista.remove([23][1])
lista.remove([24][1])
lista.remove([25][1])
lista.remove([26][1])
lista.remove([27][1])
lista.remove([28][1])
lista.remove([29][1])
lista.remove([30][1])
lista.remove([31][1])
lista.remove([32][1])
lista.remove([33][1])
lista.remove([34][1])
lista.remove([35][1])
lista.remove([36][1])
lista.remove([37][1])
lista.remove([38][1])
lista.remove([39][1])
lista.remove([40][1])
lista.remove([41][1])
lista.remove([42][1])
lista.remove([43][1])
lista.remove([44][1])
lista.remove([45][1])
lista.remove([46][1])
lista.remove([47][1])
lista.remove([48][1])
lista.remove([49][1])
lista.remove([50][1])
lista.remove([51][1])
lista.remove([52][1])
lista.remove([53][1])

print(lista)

#Término do item g


#QUESTÃO 1, letra h

#Número de casos confirmados acumulados

numerosEstadoRR = [40183]

numerosMunicipiosRR = [277, 493, 29978, 609, 839, 750, 832, 234, 1036, 272, 1246, 1401, 736, 197, 596]

if sum(numerosMunicipiosRR) == sum(numerosEstadoRR):
    print(sum(numerosMunicipiosRR))
else:
    print('Os dados da soma dos municípios divergem do estado para data 18/08/2020')

#Término do item h


#QUESTÃO 1, letra i

print(len(lista))

#Término do item i


#QUESTÃO 1, letra j

#Novos óbitos no Brasil

obitosNovosBrasil = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 2, 5, 7, 7, 9, 12, 11, 20, 15, 22, 22, 23, 42, 40, 58, 60, 73, 54, 67, 114, 133, 141, 115, 68, 99, 105, 204, 204, 188, 217, 206, 115, 113, 166, 165, 407, 357, 346, 189, 338, 474, 449, 435, 428, 395, 301, 296, 600, 614, 611, 749, 732, 496, 396, 881, 749, 844, 824, 816, 485, 674, 1179, 888, 1188, 999, 967, 653, 807, 1039, 1086, 1156, 1124, 956, 480, 623, 1262, 1349, 1473, 1005, 904, 525, 679, 1272, 1274, 1239, 909, 892, 612, 627, 1282, 1269, 1238, 1206, 1022, 641, 654, 1374, 1185, 1141, 990, 1109, 552, 692, 1280, 1038, 1252, 1290, 1091, 602, 620, 1254, 1223, 1220, 1214, 1071, 631, 733, 1300, 1233, 1322, 1163, 921, 716, 632, 1367, 1284, 1311, 1156, 1211, 555, 614, 921, 1595, 1129, 1212, 1088, 541, 561, 1154, 1421, 1253, 1079, 905, 572, 703, 1274, 1175, 1262, 1060, 709, 620, 684, 1352, 1212, 1204, 1054, 892, 494, 565, 1271, 1085, 984, 855, 958]

print('Número máximo de novos óbitos no Brasil:\n', max(obitosNovosBrasil))
print('Número mínimo de novos óbitos no Brasil:\n', min(obitosNovosBrasil))

#Término do item j


#QUESTÃO 1, letra k) 

dadosCovidPI = {'Acauã':[22, 220005, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 7084.0, 33, 4, 0, 0, ' ', ' ', 0.0], 'Agricolândia':[22,220010, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 5139.0, 45, 9, 0, 0, ' ', ' ', 0.0], 'Alagoinha do Piauí':[22, 220025, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 7651.0, 92, 9, 1, 1, ' ', ' ', 0.0], 'Alegrete do Piauí':[22, 220027, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 4915.0, 76, 20, 0, 0, ' ', ' ', 0.0],
'Alto Longá':[22, 220030, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 14304.0, 110, 7, 2, 1, ' ', ' ', 0.0], 'Altos':[22, 220040, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 40524.0, 1163, 49, 16, 2, ' ', ' ', 1.0], 'Alvorada do Gurguéia':[22, 220045, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 5419.0, 40, 14, 2, 1, ' ', ' ', 0.0], 'Amarante':[22, 220050, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 17598.0, 245, 14, 5, 1, ' ', ' ', 0.0],
'Angical do Piauí':[22, 220060, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 6788.0, 80, 8, 3, 1, ' ', ' ', 0.0], 'Antônio Almeida':[22, 220080, 22007, 'TABULEIROS DO ALTO PARNAIBA', '2020-08-27 00:00:00', 35, 3164.0, 207, 30, 1, 1, ' ', ' ', 0.0], 'Anísio de Abreu':[22, 220070, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 9880.0, 95, 13, 0, 0, ' ', ' ', 0.0], 'Aroazes':[22, 220090, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 5835.0, 47, 7, 2, 1, ' ', ' ', 0.0],
'Aroeiras do Itaim':[22, 220095, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 2551.0, 59, 16, 0, 0, ' ', ' ', 0.0], 'Arraial':[22, 220100, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4727.0, 2, 1, 0, 0, ' ', ' ', 0.0], 'Assunção do Piauí':[22, 220105, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 7846.0, 122, 15, 1, 1, ' ', ' ', 0.0], 'Avelino Lopes':[22, 220110, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 11289.0, 19, 2, 3, 1, ' ', ' ', 0.0],
'Baixa Grande do Ribeiro':[22, 220115, 22007, 'TABULEIROS DO ALTO PARNAIBA', '2020-08-27 00:00:00', 35, 11586.0, 775, 69, 8, 3, ' ', ' ', 0.0], 'Barra DAlcântara':[22, 220117, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 3951.0, 10, 3, 0, 0, ' ', ' ', 0.0], 'Barras':[22, 220120, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 47066.0, 2327, 64, 49, 3, ' ', ' ', 0.0], 'Barreiras do Piauí':[22, 220130, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 3348.0, 19, 4, 0, 0, ' ', ' ', 0.0],
'Barro Duro':[22, 220140, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 7032.0, 291, 24, 5, 1, ' ', ' ', 0.0], 'Batalha':[22, 220150, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 26857.0, 354, 13, 7, 1, ' ', ' ', 0.0], 'Bela Vista do Piauí':[22, 220155, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 4015.0, 13, 3, 0, 0, ' ', ' ', 0.0], 'Belém do Piauí':[22, 220157, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 3566.0, 82, 8, 2, 1, ' ', ' ', 0.0],
'Beneditinos':[22, 220160, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 10467.0, 196, 19, 8, 1, ' ', ' ', 1.0], 'Bertolínia':[22, 220170, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 5501.0, 129, 9, 1, 1, ' ', ' ', 0.0], 'Betânia do Piauí':[22, 220173, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6205.0, 14, 4, 1, 1, ' ', ' ', 0.0], 'Boa Hora':[22, 220177, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 6781.0, 88, 7, 0, 0, ' ', ' ', 0.0],
'Bocaina':[22, 220180, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 4500.0, 98, 16, 0, 0, ' ', ' ', 0.0], 'Bom Jesus':[22, 220190, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 25179.0, 940, 42, 11, 2, ' ', ' ', 0.0], 'Bom Princípio do Piauí':[22, 220191, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 5630.0, 39, 5, 3, 1, ' ', ' ', 0.0], 'Bonfim do Piauí':[22, 220192, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 5670.0, 68, 30, 1, 1, ' ', ' ', 0.0],
'Boqueirão do Piauí':[22, 220194, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 6407.0, 130, 20, 1, 1, ' ', ' ', 0.0], 'Brasileira':[22, 220196, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 8329.0, 90, 6, 1, 1, ' ', ' ', 0.0], 'Brejo do Piauí':[22, 220198, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 3875.0, 9, 2, 0, 0, ' ', ' ', 0.0], 'Buriti dos Lopes':[22, 220200, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 19781.0, 683, 64, 12, 2, ' ', ' ', 0.0],
'Buriti dos Montes':[22, 220202, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 8244.0, 13, 2, 1, 1, ' ', ' ', 0.0], 'Cabeceiras do Piauí':[22, 220205, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 10586.0, 200, 27, 2, 1, ' ', ' ', 0.0], 'Cajazeiras do Piauí':[22, 220207, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 3559.0, 6, 2, 0, 0, ' ', ' ', 0.0], 'Cajueiro da Praia':[22, 220208, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 7642.0, 259, 25, 7, 1, ' ', ' ', 0.0],
'Caldeirão Grande do Piauí':[22, 220209, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 5776.0, 120, 48, 0, 0, ' ', ' ', 0.0], 'Campinas do Piauí':[22, 220210, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 5613.0, 29, 3, 1, 1, ' ', ' ', 0.0], 'Campo Alegre do Fidalgo':[22, 220211, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 5045.0, 13, 3, 1, 1, ' ', ' ', 0.0], 'Campo Grande do Piauí':[22, 220213, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 5943.0, 98, 10, 1, 1, ' ', ' ', 0.0],
'Campo Largo do Piauí':[22, 220217, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 7279.0, 157, 17, 4, 1, ' ', ' ', 0.0], 'Campo Maior':[22, 220220, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 46833.0, 2011, 85, 41, 3, ' ', ' ', 0.0], 'Canto do Buriti':[22, 220230, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 21187.0, 251, 24, 4, 1, ' ', ' ', 0.0], 'Capitão Gervásio Oliveira':[22, 220245, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4100.0, 19, 2, 1, 1, ' ', ' ', 0.0],
'Capitão de Campos':[22, 220240, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 11417.0, 156, 16, 1, 1, ' ', ' ', 0.0], 'Caracol':[22, 220250, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 10916.0, 169, 14, 2, 1, ' ', ' ', 0.0], 'Caraúbas do Piauí':[22, 220253, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 5868.0, 160, 17, 3, 1, ' ', ' ', 0.0], 'Caridade do Piauí':[22, 220255, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 5067.0, 25, 7, 0, 0, ' ', ' ', 0.0],
'Castelo do Piauí':[22, 220260, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 19716.0, 92, 6, 4, 2, ' ', ' ', 0.0], 'Caxingó':[22, 220265, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 5424.0, 93, 10, 0, 0, ' ', ' ', 0.0], 'Cocal':[22, 220270, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 27787.0, 675, 41, 15, 2, ' ', ' ', 0.0], 'Cocal de Telha':[22, 220271, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 4891.0, 61, 8, 3, 1, ' ', ' ', 0.0],
'Cocal dos Alves':[22, 220272, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 6153.0, 151, 15, 4, 2, ' ', ' ', 0.0], 'Coivaras':[22, 220273, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 4020.0, 85, 10, 1, 1, ' ', ' ', 1.0], 'Colônia do Gurguéia':[22, 220275, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 6484.0, 41, 5, 2, 1, ' ', ' ', 0.0], 'Colônia do Piauí':[22, 220277, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 7656.0, 55, 7, 1, 1, ' ', ' ', 0.0],
'Conceição do Canindé':[22, 220280, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 4803.0, 13, 3, 1, 1, ' ', ' ', 0.0], 'Coronel José Dias':[22, 220285, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4682.0, 24, 5, 1, 1, ' ', ' ', 0.0], 'Corrente':[22, 220290, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 26644.0, 185, 23, 2, 1, ' ', ' ', 0.0], 'Cristalândia do Piauí':[22, 220300, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 8294.0, 7, 2, 0, 0, ' ', ' ', 0.0],
'Cristino Castro':[22, 220310, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 10423.0, 82, 11, 1, 1, ' ', ' ', 0.0], 'Curimatá':[22, 220320, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 11388.0, 135, 14, 1, 1, ' ', ' ', 0.0], 'Currais':[22, 220323, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 4954.0, 99, 15, 1, 1, ' ', ' ', 0.0], 'Curral Novo do Piauí':[22, 220327, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 5343.0, 39, 5, 0, 0, ' ', ' ', 0.0],
'Curralinhos':[22, 220325, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 4443.0, 148, 19, 0, 0, ' ', ' ', 1.0], 'Demerval Lobão':[22, 220330, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 13817.0, 941, 38, 3, 1, ' ', ' ', 1.0], 'Dirceu Arcoverde':[22, 220335, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 7011.0, 58, 7, 1, 1, ' ', ' ', 0.0], 'Dom Expedito Lopes':[22, 220340, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6904.0, 77, 8, 1, 1, ' ', ' ', 0.0],
'Dom Inocêncio':[22, 220345, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 9556.0, 50, 19, 0, 0, ' ', ' ', 0.0], 'Domingos Mourão':[22, 220342, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 4355.0, 15, 4, 0, 0, ' ', ' ', 0.0], 'Elesbão Veloso':[22, 220350, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 14602.0, 256, 26, 7, 1, ' ', ' ', 0.0], 'Eliseu Martins':[22, 220360, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 4915.0, 7, 2, 0, 0, ' ', ' ', 0.0],
'Esperantina':[22, 220370, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 39737.0, 922, 24, 25, 3, ' ', ' ', 0.0], 'Fartura do Piauí':[22, 220375, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 5307.0, 30, 6, 1, 1, ' ', ' ', 0.0], 'Flores do Piauí':[22, 220380, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4463.0, 5, 1, 1, 1, ' ', ' ', 0.0], 'Floresta do Piauí':[22, 220385, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 2558.0, 56, 10, 2, 1, ' ', ' ', 0.0],
'Floriano':[22, 220390, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 59935.0, 1585, 98, 16, 2, ' ', ' ', 0.0], 'Francinópolis':[22, 220400, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 5348.0, 34, 10, 0, 0, ' ', ' ', 0.0], 'Francisco Ayres':[22, 220410, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4348.0, 21, 3, 0, 0, ' ', ' ', 0.0], 'Francisco Macedo':[22, 220415, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 3184.0, 94, 15, 1, 1, ' ', ' ', 0.0],
'Francisco Santos':[22, 220420, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 9319.0, 35, 5, 0, 0, ' ', ' ', 0.0], 'Fronteiras':[22, 220430, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 11625.0, 135, 12, 0, 0, ' ', ' ', 0.0], 'Geminiano':[22, 220435, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 5442.0, 52, 4, 2, 1, ' ', ' ', 0.0], 'Gilbués':[22, 220440, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 10690.0, 94, 13, 1, 1, ' ', ' ', 0.0],
'Guadalupe':[22, 220450, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 10499.0, 70, 5, 1, 1, ' ', ' ', 0.0], 'Guaribas':[22, 220455, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4562.0, 12, 6, 0, 0, ' ', ' ', 0.0], 'Hugo Napoleão':[22, 220460, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 3877.0, 261, 27, 1, 1, ' ', ' ', 0.0], 'Ilha Grande':[22, 220465, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 9426.0, 241, 15, 4, 1, ' ', ' ', 0.0],
'Inhuma':[22, 220470, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 15308.0, 163, 14, 1, 1, ' ', ' ', 0.0], 'Ipiranga do Piauí':[22, 220480, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 9811.0, 118, 14, 0, 0, ' ', ' ', 0.0], 'Isaías Coelho':[22, 220490, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 8549.0, 91, 9, 1, 1, ' ', ' ', 0.0], 'Itainópolis':[22, 220500, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 11530.0, 33, 2, 1, 1, ' ', ' ', 0.0],
'Itaueira':[22, 220510, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 11019.0, 29, 6, 2, 1, ' ', ' ', 0.0], 'Jacobina do Piauí':[22, 220515, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 5741.0, 8, 4, 0, 0, ' ', ' ', 0.0], 'Jaicós':[22, 220520, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 19104.0, 94, 11, 4, 1, ' ', ' ', 0.0], 'Jardim do Mulato':[22, 220525, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 4504.0, 13, 10, 0, 0, ' ', ' ', 0.0],
'Jatobá do Piauí':[22, 220527, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 4865.0, 34, 4, 1, 1, ' ', ' ', 0.0], 'Jerumenha':[22, 220530, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4452.0, 50, 7, 1, 1, ' ', ' ', 0.0], 'Joaquim Pires':[22, 220540, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 14354.0, 715, 271, 8, 1, ' ', ' ', 0.0], 'Joca Marques':[22, 220545, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 5443.0, 326, 32, 1, 1, ' ', ' ', 0.0],
'José de Freitas':[22, 220550, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 39208.0, 926, 71, 16, 2, ' ', ' ', 1.0], 'João Costa':[22, 220535, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 3008.0, 8, 3, 0, 0, ' ', ' ', 0.0], 'Juazeiro do Piauí':[22, 220551, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 5478.0, 61, 5, 0, 0, ' ', ' ', 0.0], 'Jurema':[22, 220553, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4763.0, 16, 3, 1, 1, ' ', ' ', 0.0],
'Júlio Borges':[22, 220552, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 5627.0, 11, 2, 2, 1, ' ', ' ', 0.0], 'Lagoa Alegre':[22, 220555, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 8542.0, 182, 14, 5, 1, ' ', ' ', 1.0], 'Lagoa de São Francisco':[22, 220557, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 6758.0, 48, 5, 2, 1, ' ', ' ', 0.0], 'Lagoa do Barro do Piauí':[22, 220556, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4655.0, 280, 20, 0, 0, ' ', ' ', 0.0],
'Lagoa do Piauí':[22, 220558, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 4064.0, 240, 21, 2, 1, ' ', ' ', 1.0], 'Lagoa do Sítio':[22, 220559, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 5177.0, 19, 2, 2, 1, ' ', ' ', 0.0], 'Lagoinha do Piauí':[22, 220554, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 2845.0, 117, 15, 1, 1, ' ', ' ', 0.0], 'Landri Sales':[22, 220560, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 5295.0, 17, 3, 1, 1, ' ', ' ', 0.0],
'Luzilândia':[22, 220580, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 25486.0, 1523, 94, 26, 2, ' ', ' ', 0.0], 'Luís Correia':[22, 220570, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 30311.0, 335, 21, 13, 2, ' ', ' ', 0.0], 'Madeiro':[22, 220585, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 8310.0, 352, 37, 2, 1, ' ', ' ', 0.0], 'Manoel Emídio':[22, 220590, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 5349.0, 107, 12, 4, 1, ' ', ' ', 0.0],
'Marcolândia':[22, 220595, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 8492.0, 240, 73, 5, 1, ' ', ' ', 0.0], 'Marcos Parente':[22, 220600, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4549.0, 44, 5, 1, 1, ' ', ' ', 0.0], 'Massapê do Piauí':[22, 220605, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6441.0, 4, 1, 0, 0, ' ', ' ', 0.0], 'Matias Olímpio':[22, 220610, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 10936.0, 295, 27, 3, 1, ' ', ' ', 0.0],
'Miguel Alves':[22, 220620, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 33760.0, 933, 42, 11, 1, ' ', ' ', 0.0], 'Miguel Leão':[22, 220630, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 1246.0, 29, 9, 0, 0, ' ', ' ', 1.0], 'Milton Brandão':[22, 220635, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 6613.0, 10, 3, 0, 0, ' ', ' ', 0.0], 'Monsenhor Gil':[22, 220640, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 10564.0, 443, 31, 8, 2, ' ', ' ', 1.0],
'Monsenhor Hipólito':[22, 220650, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 7749.0, 124, 19, 2, 1, ' ', ' ', 0.0], 'Monte Alegre do Piauí':[22, 220660, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 10613.0, 144, 22, 3, 2, ' ', ' ', 0.0], 'Morro Cabeça no Tempo':[22, 220665, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 4532.0, 19, 4, 0, 0, ' ', ' ', 0.0], 'Morro do Chapéu do Piauí':[22, 220667, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 6796.0, 302, 16, 2, 1, ' ', ' ', 0.0],
'Murici dos Portelas':[22, 220669, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 9159.0, 68, 6, 2, 1, ' ', ' ', 0.0], 'Nazaré do Piauí':[22, 220670, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 7339.0, 25, 5, 1, 1, ' ', ' ', 0.0], 'Nazária':[22, 220672, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 8570.0, 84, 11, 7, 1, ' ', ' ', 1.0], 'Nossa Senhora de Nazaré':[22, 220675, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 4870.0, 42, 5, 3, 1, ' ', ' ', 0.0],
'Nossa Senhora dos Remédios':[22, 220680, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 8692.0, 432, 23, 8, 1, ' ', ' ', 0.0], 'Nova Santa Rita':[22, 220795, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4374.0, 23, 6, 0, 0, ' ', ' ', 0.0], 'Novo Oriente do Piauí':[22, 220690, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 6565.0, 39, 9, 2, 1, ' ', ' ', 0.0], 'Novo Santo Antônio':[22, 220695, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 2991.0, 48, 7, 0, 0, ' ', ' ', 0.0],
'Oeiras':[22, 220700, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 37029.0, 1172, 53, 13, 1, ' ', ' ', 0.0], 'Olho DÁgua do Piauí':[22, 220710, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 2459.0, 52, 8, 2, 1, ' ', ' ', 0.0], 'Padre Marcos':[22, 220720, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6868.0, 52, 7, 2, 1, ' ', ' ', 0.0], 'Paes Landim':[22, 220730, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4129.0, 15, 2, 1, 1, ' ', ' ', 0.0],
'Pajeú do Piauí':[22, 220735, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 3389.0, 6, 1, 1, 1, ' ', ' ', 0.0], 'Palmeira do Piauí':[22, 220740, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 5043.0, 64, 9, 1, 1, ' ', ' ', 0.0], 'Palmeirais':[22, 220750, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 14539.0, 168, 16, 3, 1, ' ', ' ', 0.0], 'Paquetá':[22, 220755, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 3945.0, 15, 2, 0, 0, ' ', ' ', 0.0],
'Parnaguá':[22, 220760, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 10791.0, 50, 8, 0, 0, ' ', ' ', 0.0], 'Parnaíba':[22, 220770, 22005, 'PLANICIE LITORANEA', '2020-08-27 00:00:00', 35, 153078.0, 6178, 180, 127, 7, ' ', ' ', 0.0], 'Passagem Franca do Piauí':[22, 220775, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 4313.0, 152, 20, 3, 1, ' ', ' ', 0.0], 'Patos do Piauí':[22, 220777, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6392.0, 36, 5, 0, 0, ' ', ' ', 0.0],
'Pau DArco do Piauí':[22, 220779, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 4045.0, 94, 15, 0, 0, ' ', ' ', 0.0], 'Paulistana':[22, 220780, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 20523.0, 70, 6, 1, 1, ' ', ' ', 0.0], 'Pavussu':[22, 220785, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 3677.0, 56, 12, 1, 1, ' ', ' ', 0.0], 'Pedro II':[22, 220790, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 38742.0, 297, 20, 9, 2, ' ', ' ', 0.0],
'Pedro Laurentino':[22, 220793, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 2536.0, 12, 3, 1, 1, ' ', ' ', 0.0], 'Picos':[22, 220800, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 78222.0, 2711, 144, 48, 3, ' ', ' ', 0.0], 'Pimenteiras':[22, 220810, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 12127.0, 169, 51, 1, 1, ' ', ' ', 0.0], 'Pio IX':[22, 220820, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 18425.0, 162, 13, 1, 1, ' ', ' ', 0.0],
'Piracuruca':[22, 220830, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 28791.0, 361, 21, 12, 1, ' ', ' ', 0.0], 'Piripiri':[22, 220840, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 63742.0, 1726, 57, 24, 2, ' ', ' ', 0.0], 'Porto':[22, 220850, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 12568.0, 198, 35, 9, 2, ' ', ' ', 0.0], 'Porto Alegre do Piauí':[22, 220855, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 2710.0, 129, 24, 1, 1, ' ', ' ', 0.0],
'Prata do Piauí':[22, 220860, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 3151.0, 16, 2, 0, 0, ' ', ' ', 0.0], 'Queimada Nova':[22, 220865, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 8992.0, 171, 52, 2, 1, ' ', ' ', 0.0], 'Redenção do Gurguéia':[22, 220870, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 8778.0, 97, 12, 3, 1, ' ', ' ', 0.0], 'Regeneração':[22, 220880, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 17978.0, 125, 21, 0, 0, ' ', ' ', 0.0],
'Riacho Frio':[22, 220885, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 4312.0, 1, 1, 0, 0, ' ', ' ', 0.0], 'Ribeira do Piauí':[22, 220887, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4477.0, 6, 1, 0, 0, ' ', ' ', 0.0], 'Ribeiro Gonçalves':[22, 220890, 22007, 'TABULEIROS DO ALTO PARNAIBA', '2020-08-27 00:00:00', 35, 7341.0, 214, 24, 5, 1, ' ', ' ', 0.0], 'Rio Grande do Piauí':[22, 220900, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 6432.0, 31, 4, 1, 1, ' ', ' ', 0.0],
'Santa Cruz do Piauí':[22, 220910, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6240.0, 304, 21, 4, 2, ' ', ' ', 0.0], 'Santa Cruz dos Milagres':[22, 220915, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 4019.0, 15, 4, 0, 0, ' ', ' ', 0.0], 'Santa Filomena':[22, 220920, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 6253.0, 30, 9, 2, 1, ' ', ' ', 0.0], 'Santa Luz':[22, 220930, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 5860.0, 90, 15, 2, 1, ' ', ' ', 0.0],
'Santa Rosa do Piauí':[22, 220937, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 5257.0, 33, 5, 1, 1, ' ', ' ', 0.0], 'Santana do Piauí':[22, 220935, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 4634.0, 16, 3, 0, 0, ' ', ' ', 0.0], 'Santo Antônio de Lisboa':[22, 220940, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6415.0, 13, 2, 0, 0, ' ', ' ', 0.0], 'Santo Antônio dos Milagres':[22, 220945, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 2161.0, 42, 10, 1, 1, ' ', ' ', 0.0],
'Santo Inácio do Piauí':[22, 220950, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 3798.0, 45, 6, 1, 1, ' ', ' ', 0.0], 'Sebastião Barros':[22, 221062, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 3469.0, 3, 1, 1, 1, ' ', ' ', 0.0], 'Sebastião Leal':[22, 221063, 22007, 'TABULEIROS DO ALTO PARNAIBA', '2020-08-27 00:00:00', 35, 4294.0, 71, 18, 0, 0, ' ', ' ', 0.0], 'Sigefredo Pacheco':[22, 221065, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 10041.0, 95, 20, 1, 1, ' ', ' ', 0.0],
'Simplício Mendes':[22, 221080, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 12711.0, 144, 15, 1, 1, ' ', ' ', 0.0], 'Simões':[22, 221070, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 14633.0, 184, 8, 1, 1, ' ', ' ', 0.0], 'Socorro do Piauí':[22, 221090, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 4569.0, 20, 5, 1, 1, ' ', ' ', 0.0], 'Sussuapara':[22, 221093, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6730.0, 140, 12, 3, 1, ' ', ' ', 0.0],
'São Braz do Piauí':[22, 220955, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4448.0, 11, 2, 0, 0, ' ', ' ', 0.0], 'São Francisco de Assis do Piauí':[22, 220965, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 5755.0, 6, 2, 0, 0, ' ', ' ', 0.0], 'São Francisco do Piauí':[22, 220970, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 6423.0, 5, 1, 1, 1, ' ', ' ', 0.0], 'São Félix do Piauí':[22, 220960, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 2942.0, 25, 4, 1, 1, ' ', ' ', 0.0],
'São Gonçalo do Gurguéia':[22, 220975, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-08-27 00:00:00', 35, 3041.0, 18, 4, 1, 1, ' ', ' ', 0.0], 'São Gonçalo do Piauí':[22, 220980, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 5015.0, 58, 4, 2, 1, ' ', ' ', 0.0], 'São José do Divino':[22, 221005, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 5346.0, 46, 3, 6, 1, ' ', ' ', 0.0], 'São José do Peixe':[22, 221010, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 3745.0, 13, 4, 0, 0, ' ', ' ', 0.0],
'São José do Piauí':[22, 221020, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6705.0, 31, 6, 0, 0, ' ', ' ', 0.0], 'São João da Canabrava':[22, 220985, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 4608.0, 42, 9, 1, 1, ' ', ' ', 0.0], 'São João da Fronteira':[22, 220987, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 6042.0, 50, 4, 0, 0, ' ', ' ', 0.0], 'São João da Serra':[22, 220990, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 6139.0, 102, 11, 5, 1, ' ', ' ', 0.0],
'São João da Varjota':[22, 220995, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 4840.0, 39, 9, 2, 1, ' ', ' ', 0.0], 'São João do Arraial':[22, 220997, 22003, 'COCAIS', '2020-08-27 00:00:00', 35, 7989.0, 207, 19, 1, 1, ' ', ' ', 0.0], 'São João do Piauí':[22, 221000, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 20601.0, 197, 20, 2, 1, ' ', ' ', 0.0], 'São Julião':[22, 221030, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 6363.0, 80, 11, 1, 1, ' ', ' ', 0.0],
'São Lourenço do Piauí':[22, 221035, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4573.0, 5, 1, 0, 0, ' ', ' ', 0.0], 'São Luis do Piauí':[22, 221037, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 2644.0, 28, 3, 0, 0, ' ', ' ', 0.0], 'São Miguel da Baixa Grande':[22, 221038, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 2452.0, 5, 1, 0, 0, ' ', ' ', 0.0], 'São Miguel do Fidalgo':[22, 221039, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 3039.0, 3, 1, 0, 0, ' ', ' ', 0.0],
'São Miguel do Tapuio':[22, 221040, 22001, 'CARNAUBAIS', '2020-08-27 00:00:00', 35, 17662.0, 122, 11, 1, 1, ' ', ' ', 0.0], 'São Pedro do Piauí':[22, 221050, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 14291.0, 296, 16, 4, 1, ' ', ' ', 0.0], 'São Raimundo Nonato':[22, 221060, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 34710.0, 971, 50, 7, 2, ' ', ' ', 0.0], 'Tamboril do Piauí':[22, 221095, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-08-27 00:00:00', 35, 2919.0, 12, 5, 0, 0, ' ', ' ', 0.0],
'Tanque do Piauí':[22, 221097, 22008, 'VALE DO CANINDE', '2020-08-27 00:00:00', 35, 2765.0, 9, 2, 0, 0, ' ', ' ', 0.0], 'Teresina':[22, 221100, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 864845.0, 24380, 626, 884, 19, ' ', ' ', 1.0], 'União':[22, 221110, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 44485.0, 776, 41, 25, 4, ' ', ' ', 1.0], 'Uruçuí':[22, 221120, 22007, 'TABULEIROS DO ALTO PARNAIBA', '2020-08-27 00:00:00', 35, 21558.0, 1314, 198, 21, 3, ' ', ' ', 0.0],
'Valença do Piauí':[22, 221130, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 20918.0, 511, 47, 6, 2, ' ', ' ', 0.0], 'Vera Mendes':[22, 221150, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 3077.0, 26, 13, 0, 0, ' ', ' ', 0.0], 'Vila Nova do Piauí':[22, 221160, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 2971.0, 92, 46, 0, 0, ' ', ' ', 0.0], 'Várzea Branca':[22, 221135, 22006, 'SERRA DA CAPIVARA', '2020-08-27 00:00:00', 35, 4947.0, 30, 9, 1, 1, ' ', ' ', 0.0],
'Várzea Grande':[22, 221140, 22010, 'VALE DO SAMBITO', '2020-08-27 00:00:00', 35, 4391.0, 27, 5, 0, 0, ' ', ' ', 0.0], 'Wall Ferraz':[22, 221170, 22009, 'VALE DO RIO GUARIBAS', '2020-08-27 00:00:00', 35, 4462.0, 284, 143, 2, 1, ' ', ' ', 0.0], 'Água Branca':[22, 220020, 22004, 'ENTRE RIOS', '2020-08-27 00:00:00', 35, 17411.0, 830, 31, 29, 2, ' ', ' ', 0.0]}

#Término do item k


#QUESTÃO 1, letra l

print(dadosCovidPI['Teresina'])

#Término do item l

#Finalizado
