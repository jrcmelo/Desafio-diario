'''
"Uma função com dois parâmetros, uma com texto e outra com um subtexto, essa função deve extrair o subtexto do texto. 
Por exemplo, Texto = "o cria beijou a sua mãe" sub-texto = "a sua mãe", o resultado nesse caso deverá ser "o cria beijou"."
'''

import re

txtOri = str(input('Informe o primeiro texto: '))
Edi = str(input('Informe o segundo texto: '))

txtEdi = re.sub(Edi, '', txtOri)

print(txtEdi)