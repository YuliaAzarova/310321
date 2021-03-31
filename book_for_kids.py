from random import *

name_pril = ['синий', 'голодный', 'лысый',
             'маленький', 'рогатый',
             'щекастый', 'лохматый']
name_sush = ['кит', 'пёс', 'дедушка',
             'мышонок',
             'олень', 'хомяк', 'птенец']
glagol = ['плывёт', 'плетётся', 'смотрит',
          'бежит', 'бредёт', 'движется',
          'катится']
obstoyatelstvo = ['на юг', 'по холму',
                  'под гору', 'в нору',
                  'в лес',
                  'к хижине', 'вдоль берега']

shuffle(name_sush)
shuffle(name_pril)
shuffle(glagol)
shuffle(obstoyatelstvo)
print(name_pril[0], name_sush[0], glagol[0],
      obstoyatelstvo[0])