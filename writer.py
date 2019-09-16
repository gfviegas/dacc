#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import pandas as pd

# Formata o nome das pessoas
def formatName(name):
    parts = name.split(' ')
    parts = list(map(lambda p: p.capitalize(), parts))
    return ' '.join(parts)

# Formata o cpf das pessoas
def formatCPF(cpf):
    i = str(cpf).zfill(11)
    return '{}.{}.{}-{}'.format(i[:3], i[3:6], i[6:9], i[-2:])

# Carregando os dados das inscrições
df = pd.read_csv('dados.csv', squeeze=True, encoding='utf8')
df.columns = ['date', 'name', 'cpf', 'type']
df.name = df.name.apply(formatName)
df.cpf = df.cpf.apply(formatCPF)

# Imagem Base
base = cv2.imread('./base.png', 1)
base_rgb = cv2.cvtColor(base, cv2.COLOR_BGR2RGB)

# Carregando Fontes
font_name = ImageFont.truetype('Assistant-Bold.otf', 32)
font_type = ImageFont.truetype('Assistant-Bold.otf', 14)

# Gera o crachá da pessoa
def generateImage(person):
    base_copy = cv2.cvtColor(base.copy(), cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(base_copy)
    draw = ImageDraw.Draw(pil_img)

    # Escreve os dados
    draw.text((140, 770), person['name'], font=font_name, fill=(0,0,0))
    draw.text((550, 830), person['type'], font=font_type, fill=(0,0,0))
    draw.text((150, 830), '{}'.format(person['cpf']), font=font_type, fill=(0,0,0))

    # Processa e salva
    processed = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    cv2.imwrite('images/{}.png'.format(person['cpf']), processed)

    return '.'


if __name__ == '__main__':
    for i, row in df.iterrows():
        generateImage(row)
