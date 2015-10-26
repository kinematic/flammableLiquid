#!/usr/bin/python3
# -*- coding: utf-8 -*-

auto = int(input('Автомобиль: 1 - Caddy; 2 - Kengoo [1]: ') or 1)
if auto == 1:
  tankVolume = 60
  devision = 16
elif auto == 2:
  tankVolume = 50
  devision = 12
  
odoStart = int(input('Одометр при выезде, км: ') or '115262')
odoStop = int(input('Одометр при заезде, км: ') or '115336')
planOdo = int(input('Планируемый пробег до гаража, км [4]: ') or '4')
tankStart = int(input('Уровень в баке при выезде, л: ') or '50')
tankStop = float(input('Стрелка уровня в баке при заезде, делений: ') or '12.5')
charges = input('Заправки через пробел, л [0]: ') or '0'
charges = charges.split()
k = 0
for i in charges:
  k = k + float(i)
charges = k
tankCharge = tankStart + charges

planConsumption = float(input('Планируемый расход, л/100 км [9.5]:') or 9.5)

#print(str(charges))

# Рассчитаем пробег
diffOdo = odoStop - odoStart + planOdo
print('Пробег: ' + str(diffOdo) + ' км')
# Рассчитаем затраты топлива
tankStop = tankStop * tankVolume / devision
  
def tankResults(tankStop, tankCharge = tankCharge, diffOdo = diffOdo):
  output = '\n'
  output = output + 'Рассчет для топлива в баке: ' + str(round(tankStop)) + ' л\n'
  # Затраченное топливо
  diffVolume = tankCharge - tankStop
  output = output + 'Затрачено топлива: ' + str(round(diffVolume)) + ' л\n'

  # Рассчитаем расход топлива на 100 км
  fuelConsumption = round(100 * diffVolume / diffOdo, 1)
  output = output + 'Расход топлива: ' + str(fuelConsumption) + ' л/100 км\n'

  # Рассчитаем планируемый остаток в баке
  planTankStop = tankCharge - diffOdo*planConsumption/100
  output = output + 'Планируемый остаток в баке: ' + str(round(planTankStop)) + ' л | ' + str(round(planTankStop*devision/tankVolume, 1)) + ' делений\n'

  # Рассчитываем излишки
  diffStopValue = round(tankStop - planTankStop)
  output = output + 'Излишки: ' + str(diffStopValue) + ' л'
  print(output)
  return round(planTankStop)

planTankStop = tankResults(tankStop)
if planTankStop % 5 != 0:
  planTankStop = planTankStop
  planTankStop1 = (planTankStop // 5) * 5
  planTankStop2 = ((planTankStop + 5) // 5) * 5
  diffPlanTankStop1 = planTankStop - planTankStop1
  diffPlanTankStop2 = planTankStop2 - planTankStop
  if planTankStop1 * 2 <= diffPlanTankStop2:
    planTankStop = planTankStop1
  else:
    planTankStop = planTankStop2
  planTankStop = tankResults(planTankStop)