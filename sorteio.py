# -*- coding: utf-8 -*-

# Copyright (c) 2012, Francisco Souza
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#   * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


'''
Script de sorteio utilizado no Dev in Cachu 2012.

Para executar este script, passe a lista de inscritos como primeiro argumento na
linha de comando. Um arquivo chamado "sorteados.txt" será criado, e a cada
sorteio o nome sorteado irá para esse arquivo, garantindo que nenhum nome é
sorteado duas vezes.
'''

import random
import sys

limpa_nl = lambda arq: [l.strip('\n') for l in arq.readlines()]


def main():
    if len(sys.argv) != 2:
        print "Você deve informar o arquivo com inscritos!"
        sys.exit(2)
    nome_arquivo = sys.argv[1]
    arquivo = None
    arquivo_sorteados = open("sorteados.txt", "a+")
    arquivo_sorteados.seek(0)
    sorteados = limpa_nl(arquivo_sorteados)
    try:
        arquivo = open(nome_arquivo)
        inscritos = limpa_nl(arquivo)
        sorteado = random.choice(inscritos)
        while sorteado in sorteados:
            sorteado = random.choice(inscritos)
        arquivo_sorteados.write("%s\n" % sorteado)
        print sorteado
    except IOError:
        print "Arquivo %s não existe!" % nome_arquivo
    finally:
        if arquivo is not None:
            arquivo.close()
        arquivo_sorteados.close()

if __name__ == '__main__':
    main()
