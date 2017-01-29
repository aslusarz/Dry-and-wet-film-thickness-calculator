#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: aslusarz

# FROM ZERO TO PYTHON HERO series
# Script No#4: Calculator of Dry and Wet Film Thickness due to paint parameters and technicks of painting

# Note that its only a calculations and practical results may be different as shown in results!

# File created: 29.01.17
# Last modified: 00.01.17
# Version: P.4.001-A [P:Prototype, F:Final]

import os

PAINTS = {  1:['Temalac SC 50', 61],
            2:['XPP 40003', 41],
            3:['Delfleet F333', 60],
            4:['Temadur SC 80', 65],
            5:['SW Enamel', 38],
            6:['Nitro 90', 20],
            7:['POLREN 90', 48]}

ROUGHNESS = {   10:[0,50],
                35:[51,100],
                60:[101,150],
                125:[151,300]}

SURPLUS = {     1:['Conventional, simple shape', 5],
                2:['Conventional, complex shape', 10],
                3:['Conventional, complex shape & preliminary painting', 15],
                4:['Spraying, simple shape', 20],
                5:['Spraying, complex shape', 40],
                6:['Spraying, complex shape & preliminary painting', 60]}

APP_LOSS = {    1:['Closed area, ventilated', 5],
                2:['Opean area, windless', 10],
                3:['Opean area, gentle wind', 20]}


def theoretical_yield(s_content, DFT, roughness):
    t_use = (s_content * 10) / (DFT + roughness)
    return round(t_use, 2) #m2/dm3

def theoretical_coverage(t_use, surplus, app_loss):
    t_coverage = t_use - (t_use * surplus / 100) - (t_use * app_loss / 100)
    return t_coverage

def prnt_nom_thick():
    key = ''
    while True:
        key = input('Specify a nominal DFT coating thichness [um]: ')
        if key.isdigit() and int(key) > 0 and int(key) <= 1000:
            break
    return int(key)

def select_paint():
    key = ''
    counter = 0
    print ('Select paint from list below or specify a volume solids content by giving percent sign first: ')
    for paints in PAINTS:
        print ('[{0}] - {1}'.format(paints, PAINTS[paints][0]))
        counter += 1
    while True:
        key = input('Your choise: ')
        if key.isdigit() and int(key) > 0 and int(key) <= counter:
            return PAINTS[int(key)][1]
            break
        elif key[0] == '%':
            key = key[1:]
            if key.isdigit() and int(key) > 0 and int(key) < 100:
                return int(key)
                break
            else:
                continue
        else:
            continue
    return int(key)

def select_roughness():
    key = ''
    print ('Specify /Ra/ roughness of material surface as integer number in microns: ')
    while True:
        key = input('From 0 up to 300 [um]: ')
        if key.isdigit() and int(key) >= 0 and int(key) <= 300:
            break
    for rough in ROUGHNESS:
        if ROUGHNESS[rough][0] <= int(key) <= ROUGHNESS[rough][1]:
            return int(rough)
            break

def select_surplus():
    key = ''
    counter = 0
    print ('Select the most similar method of painting and character of shape from list below: ')
    for splus in SURPLUS:
        print ('[{0}] - {1}'.format(splus, SURPLUS[splus][0]))
        counter += 1
    while True:
        key = input('Your choise: ')
        if key.isdigit() and int(key) in range(1,counter):
            return SURPLUS[int(key)][1]
            break

def select_lost():
    key = ''
    counter = 0
    print ('Select envirnoment of painting from list below: ')
    for lost in APP_LOSS:
        print ('[{0}] - {1}'.format(lost, APP_LOSS[lost][0]))
        counter += 1
    while True:
        key = input('Your choise: ')
        if key.isdigit() and int(key) in range(1,counter):
            return APP_LOSS[int(key)][1]
            break

def calculate_WFT(DFT, s_content):
    wet = (DFT / (s_content / 100)) / (1 + 0.1)
    return round(wet)

def main():
    os.system('clear')
    print ('Paint Film Thickness Calculator')
    DFT = prnt_nom_thick()
    s_content = select_paint()
    roughness = select_roughness()
    theor_yield = theoretical_yield(s_content, DFT, roughness)
    surplus = select_surplus()
    lost = select_lost()
    theor_cover = theoretical_coverage(theor_yield, surplus, lost)
    WFT = calculate_WFT(DFT, s_content)
    os.system('clear')
    print ('Summary:')
    print ('Dry Film Thickness: {0} [um]'.format(DFT))
    print ('Wet Film Thickness: {0} [um] (with 10% of reducer)'.format(WFT))
    print ('Theoretical yield: {0} [m2/dm3]'.format(theor_yield))
    print ('Calculated coverage: {0} [m2/dm3]'.format(round(theor_cover, 1)))
main()
