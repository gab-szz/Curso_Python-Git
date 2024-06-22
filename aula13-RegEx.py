###########
#  REGEX  #
###########

import re

txt = "O Gabriel é lindo"

# Verificar se a string começa com O e termina com "lindo".

re.search("^O.*Miguel$", txt)

re.findall("Gabriel", txt)
# Retorna uma lista com todos os "Gabriel" do texto.

re.sub("\s", "space", txt)
# Substitui os espaços por 'space'
