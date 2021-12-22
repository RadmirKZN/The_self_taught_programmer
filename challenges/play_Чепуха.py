import re
text = """Жирафы любят таскать 
различные _СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ_
целый день на пролёт. Жирафы 
славятсся тем, что поедают 
прекрасные _СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ_, но
после этого у них часто
болит _ЧАСТЬ_ТЕЛА_. Если же 
жирафы находят _ЧИСЛО_
_СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ, у 
них моментально отваливается _ЧАСТЬ ТЕЛА_.
"""

def mad_libs(mls):
    """
    :param mls:
    :return:
    """
    hints = re.findall("_.*?_", mls)

    if hints is not None:
        for word in hints:
            q = "Введите {}".format(word)
            new = input (q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else: print("Ошибка ввода")

mad_libs(text)
