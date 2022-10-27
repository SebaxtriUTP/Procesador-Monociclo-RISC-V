#programa que recibe lenguaje ensamblador risc v y devuelve su hex
#vector 32 positions 
#$ python3 assembler.py    
#Path: Monociclo\assembler.py
import os
from re import T
import string
from turtle import clear
from unicodedata import name
from xmlrpc.client import Boolean


archivo = open(r'C:\Users\245-G8\Documents\Semestre 2022-2\Arquitectura De computadores\Monociclo\instrucciones.txt')
lineas = archivo.readlines()
#transformar = lineas[0]

nombre_tiket = []
valor_tiket = []

def transformar_lista(transformar,address):
    print('transformar: ',transformar)
    instr = []
    rd = []
    rs1 = []
    rs2 = []
    imm = []
    
    negative = Boolean
    #ignorador de los espacios y 

    for i in range(len(transformar)):
        if transformar[i] == ' ' or transformar[i] == '' or transformar[i] == '\t':
            continue
        else:
            l = i
            break
    print('Numero de espacios ignorados : ',l)



    #asignacion de la instruccion 
    for(i) in range(l,len(transformar)):
        instr.append(transformar[i])
        if transformar[i] == ' ':
            j = i
            break
        elif transformar[i] == ':':
            print('simbolo terminal etiqueta: ',instr)
            instr = []
            return(transformar_lista(transformar[i+1:],i))
            
    

            

    instr = ''.join(instr)[:-1]
    if instr[0] == ' ': 
        print('me mame un espacio')
        instr = instr[1:] #pura fuerza bruta
    print('Instruccion : ',instr)
#Tipo R
    if instr == 'add' or instr == 'sub' or instr == 'and' or instr == 'or' or instr == 'xor' or instr == 'sll' or instr == 'srl' or instr == 'slt' or instr == 'sltu':
        for(i) in range(j+1,len(transformar)):
            rd.append(transformar[i])
            if transformar[i] == ',':
                k = i
                break

        for(i) in range(k+1,len(transformar)):
            rs1.append(transformar[i])
            if transformar[i] == ',':
                l = i
                break

        for(i) in range(l+1,len(transformar)):
            rs2.append(transformar[i])
            if transformar[i] == ' ':
                break

        rd = ''.join(rd)[:-1]
        rs1 = ''.join(rs1)[:-1]
        rs2 = ''.join(rs2)[:-1]

        if instr == 'add':
            OpCode = '0110011'
            funct3 = '000'
            funct7 = '0000000'
        elif instr == 'sub':
            OpCode = '0110011'
            funct3 = '000'
            funct7 = '0100000'
        elif instr == 'sll':
            OpCode = '0110011'
            funct3 = '001'
            funct7 = '0000000'
        elif instr == 'slt':
            OpCode = '0110011'
            funct3 = '010'
            funct7 = '0000000'
        elif instr == 'sltu':
            OpCode = '0110011'
            funct3 = '011'
            funct7 = '0000000'
        elif instr == 'xor':
            OpCode = '0110011'
            funct3 = '100'
            funct7 = '0000000'
        elif instr == 'srl':
            OpCode = '0110011'
            funct3 = '101'
            funct7 = '0000000'
        elif instr == 'or':
            OpCode = '0110011'
            funct3 = '110'
            funct7 = '0000000'
        elif instr == 'and':
            OpCode = '0110011'
            funct3 = '111'
            funct7 = '0000000'
        #valores separados para convertir a binario
        rd = int(rd[1:])
        rs1 = int(rs1[1:])
        rs2 = int(rs2[1:])
        
        rd = binarizar(rd)
        rs1 = binarizar(rs1)
        rs2 = binarizar(rs2)
        #completar con ceros
        rd = rd.zfill(5)
        rs1 = rs1.zfill(5)
        rs2 = rs2.zfill(5)
        print('funct7: ',funct7, 'rs2: ',rs2, 'rs1: ',rs1, 'funct3: ',funct3, 'rd: ',rd, 'OpCode: ',OpCode)
        
        result = funct7+rs2+rs1+funct3+rd+OpCode
        print(binario_a_hexa(result))
        #result = binario_a_hexa(result)

        return result
#Tipo I
    if instr == 'addi' or instr == 'andi' or instr == 'ori' or instr == 'xori' or instr == 'slli' or instr == 'srli' or instr == 'slti' or instr == 'sltiu':
        for(i) in range(j+1,len(transformar)):
            rd.append(transformar[i])
            if transformar[i] == ',':
                k = i
                break
        print('rd: ',rd)
        for(i) in range(k+1,len(transformar)):
            rs1.append(transformar[i])
            if transformar[i] == ',':
                l = i
                break

        for(i) in range(l+1,len(transformar)):
            if transformar[i] == ' ':
                break
            if transformar[i] == '-':
                negative = True
                continue
            
            imm.append(transformar[i])

        rd = ''.join(rd)[:-1]
        rs1 = ''.join(rs1)[:-1]
        imm = ''.join(imm)
        print('rd: ',rd)
        print('rs1: ',rs1)
        print('imm: ',imm)

        if instr == 'addi':
            OpCode = '0010011'
            funct3 = '000'
        elif instr == 'slli':
            OpCode = '0010011'
            funct3 = '001'
        elif instr == 'slti':
            OpCode = '0010011'
            funct3 = '010'
        elif instr == 'sltiu':
            OpCode = '0010011'
            funct3 = '011'
        elif instr == 'xori':
            OpCode = '0010011'
            funct3 = '100'
        elif instr == 'srli':
            OpCode = '0010011'
            funct3 = '101'
        elif instr == 'ori':
            OpCode = '0010011'
            funct3 = '110'
        elif instr == 'andi':
            OpCode = '0010011'
            funct3 = '111'
        #valores separados para convertir a binario
        rd = int(rd[1:])
        rs1 = int(rs1[1:])
        imm = int(imm)

        #binarizar
        rd = binarizar(rd)
        rs1 = binarizar(rs1)
        imm = binarizar(imm)
        
        #completar con ceros
        rd = rd.zfill(5)
        rs1 = rs1.zfill(5)
        imm = imm.zfill(12)

        if negative == True: #Si el inmediato es negativo lo negamos y le sumamos 1 
            imm = negate(imm)
            print('Inmediato negativo')
        else:
            print('Inmediato positivo')
            pass

        
        print('imm: ',imm, 'rs1: ',rs1, 'funct3: ',funct3, 'rd: ',rd, 'OpCode: ',OpCode)
        result = imm+rs1+funct3+rd+OpCode
        #result = binario_a_hexa(result)
        return result
#Tipo S
    if instr == 'lb' or instr == 'lh' or instr == 'lw' or instr == 'lbu' or instr == 'lhu' or instr == 'jalr':
        #asignar el valor rd
        for(i) in range(j+1,len(transformar)):
            rd.append(transformar[i])
            if transformar[i] == ',':
                j_1 = i
                break
        print('rd: ',rd)
        for(i) in range(j_1+1,len(transformar)):
            if transformar[i] == '(':
                k = i
                print('k: ',k)
                break
            if transformar[i] == '-':
                negative = True
                continue
            imm.append(transformar[i])

        for(i) in range(k+1,len(transformar)):
            rs1.append(transformar[i])
            if transformar[i] == ')':
                break

        rd = ''.join(rd)[:-1]
        imm = ''.join(imm)
        rs1 = ''.join(rs1)[:-1]
        
        print('rd: ',rd)
        print('imm: ',imm)
        print('rs1: ',rs1)

        if instr == 'lb':
            OpCode = '0000011'
            funct3 = '000'
        elif instr == 'lh':
            OpCode = '0000011'
            funct3 = '001'
        elif instr == 'lw':
            OpCode = '0000011'
            funct3 = '010'
        elif instr == 'lbu':
            OpCode = '0000011'
            funct3 = '100'
        elif instr == 'lhu':
            OpCode = '0000011'
            funct3 = '101'
        elif instr == 'jalr':
            OpCode = '1100111'
            funct3 = '000'
        #valores separados para convertir a binario
        rd = int(rd[1:])
        if rs1 == 'sp':
            rs1 = '00010'
        else:
            rs1 = int(rs1[1:])
            print('rs1: ',rs1, 'type: ',type(rs1))
        imm = int(imm)

        if rs1 != '00010':
            rs1 = binarizar(rs1)
            rs1 = rs1.zfill(5)
            print('rs1: ',rs1)
        #binarizar
        rd = binarizar(rd)
        imm = binarizar(imm)
        
        #completar con ceros
        rd = rd.zfill(5)
        imm = imm.zfill(12)

        print('imm: ',imm, 'rs1: ',rs1, 'funct3: ',funct3, 'rd: ',rd, 'OpCode: ',OpCode)

        result = imm+rs1+funct3+rd+OpCode
        
        #result = binario_a_hexa(result)

        return result
#Tipo SB
    if instr == 'sb' or instr == 'sh' or instr == 'sw':
        for(i) in range(j+1,len(transformar)):
            rs2.append(transformar[i])
            if transformar[i] == ',':
                j = i
                break

        for(i) in range(j+1,len(transformar)):
            if transformar[i] == '(':
                k = i
                break
            if transformar[i] == '-':
                negative = True
                continue
            imm.append(transformar[i])

        for(i) in range(k+1,len(transformar)):
            rs1.append(transformar[i])
            if transformar[i] == ')':
                break

        rs1 = ''.join(rs1)[:-1]
        rs2 = ''.join(rs2)[:-1]
        imm = ''.join(imm)
        
        if instr == 'sb':
            OpCode = '0100011'
            funct3 = '000'
        elif instr == 'sh':
            OpCode = '0100011'
            funct3 = '001'
        elif instr == 'sw':
            OpCode = '0100011'
            funct3 = '010'

        #valores separados para convertir a binario
        if rs1 == 'sp':
            rs1 = '00010'
        rs2 = int(rs2[1:]) #se quita el X del registro
        imm = int(imm)

        print('rs1: ',rs1)
        print('rs2: ',rs2)
        print('imm: ',imm)

        #binarizar
        rs2 = binarizar(rs2)
        imm = binarizar(imm)
        
        #completar con ceros
        rs2 = rs2.zfill(5)
        imm = imm.zfill(12)

        print('imm: ',imm[0:7], 'rs2: ',rs2,'rs1: ',rs1, 'funct3: ',funct3,'imm:  ',imm[7:12], 'OpCode: ',OpCode)
        result = imm[0:7]+rs2+rs1+funct3+imm[7:12]+OpCode
        #result = binario_a_hexa(result)

        return result
#Tipo U
    if instr == 'bge' or instr == 'blt' or instr == 'bgeu' or instr == 'bltu' or instr == 'beq' or instr == 'bne':
        for(i) in range(j+1,len(transformar)):
            rs1.append(transformar[i])
            if transformar[i] == ',':
                j = i
                break

        for(i) in range(j+1,len(transformar)):
            rs2.append(transformar[i])
            if transformar[i] == ',':
                k = i
                break

        for(i) in range(k+1,len(transformar)):
            if transformar[i] == '-':
                negative = True
                print('Inmediato negativo')
                continue
            imm.append(transformar[i])
            if transformar[i] == ' ':
                break

        rs1 = ''.join(rs1)[:-1]
        rs2 = ''.join(rs2)[:-1]
        imm = ''.join(imm)[:-1]

        print('rs1: ',rs1)
        print('rs2: ',rs2)
        print('imm: ',imm)
        
        if instr == 'bge':
            OpCode = '1100011'
            funct3 = '101'
        elif instr == 'blt':
            OpCode = '1100011'
            funct3 = '100'
        elif instr == 'bgeu':
            OpCode = '1100011'
            funct3 = '111'
        elif instr == 'bltu':
            OpCode = '1100011'
            funct3 = '110'
        elif instr == 'beq':
            OpCode = '1100011'
            funct3 = '000'
        elif instr == 'bne':
            OpCode = '1100011'
            funct3 = '001'

        #buscar el inmediato en nombre_tiket
        for i in range(len(nombre_tiket)):
            if nombre_tiket[i] == imm:
                imm = valor_tiket[i]
                imm = imm - address*4
                print('imm encontrado: ',imm, 'nombre: ',nombre_tiket[i])
                if imm < 0:
                    negative = True
                    imm = imm * -1
                    print('quitado signo: ',imm)
                break
        
        #valores separados para convertir a binario
        if rs1 == 'sp':
            rs1 = '00010'
        if rs2 == 'sp':
            rs2 = '00010'
        rs1 = int(rs1[1:])
        rs2 = int(rs2[1:])
        imm = int(imm)

        #binarizar
        rs1 = binarizar(rs1)
        rs2 = binarizar(rs2)
        imm = binarizar(imm)
        #completar con ceros
        rs1 = rs1.zfill(5)
        rs2 = rs2.zfill(5)
        imm = imm.zfill(12)

        if negative == True:
            imm = negate(imm)
            print('imm invertido: ',imm)
        


        print('imm: ',imm[0], 'imm[1:7]: ',imm[1:7], 'rs2: ',rs2,'rs1: ',rs1, 'funct3: ',funct3,'imm[9:11]: ',imm[7:11], 'imm[1]: ',imm[1], 'OpCode: ',OpCode)
        result = imm[0]+imm[1:7]+rs2+rs1+funct3+imm[7:11]+imm[1]+OpCode

        #result = binario_a_hexa(result)
        print('result: ',result)
        return result
#Tipo U J
    if instr == 'jal':
        for(i) in range(j+1,len(transformar)):
            rd.append(transformar[i])
            if transformar[i] == ',':
                j = i
                break

        for(i) in range(j+1,len(transformar)):
            if transformar[i] == '-':
                negative = True
                print('Inmediato negativo')
                continue
            imm.append(transformar[i])
            if transformar[i] == ' ':
                break

        rd = ''.join(rd)[:-1]
        imm = ''.join(imm)[:-1]

        print('rd: ',rd)
        print('imm: ',imm)
        
        if instr == 'jal':
            OpCode = '1100111'
            funct3 = '000'

        #buscar el inmediato en nombre_tiket
        for i in range(len(nombre_tiket)):
            if nombre_tiket[i] == imm:
                imm = valor_tiket[i]
                imm = imm - address*4
                print('imm encontrado: ',imm, 'nombre: ',nombre_tiket[i])
                if imm < 0:
                    negative = True
                    imm = imm * -1
                    print('quitado signo: ',imm)
                break
        
        #valores separados para convertir a binario
        rd = int(rd[1:])
        imm = int(imm)

        #binarizar
        rd = binarizar(rd)
        imm = binarizar(imm)
        #completar con ceros
        rd = rd.zfill(5)
        imm = imm.zfill(21)

        if negative == True:
            imm = negate(imm)
            print('imm invertido: ',imm)

        #separar en partes
        print('len1: ',len(imm))
        print('imm[0]: ',imm[0], 'imm[10:19]: ',imm[10:20], 'imm[9]: ',imm[9],'imm[1:8]',imm[1:9],'rd: ',rd,'OpCode: ',OpCode)
        result = imm[0]+imm[10:20]+imm[9]+imm[1:9]+rd+OpCode
        #result = binario_a_hexa(result)
        print('result: ',result,'len: ',len(result))
        return result
        

    

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    

#binary to hex ech 4 bits
def binario_a_hexa(binario):
    hexa = ''
    for i in range(0,len(binario),4):
        if binario[i:i+4] == '0000':
            hexa += '0'
        elif binario[i:i+4] == '0001':
            hexa += '1'
        elif binario[i:i+4] == '0010':
            hexa += '2'
        elif binario[i:i+4] == '0011':
            hexa += '3'
        elif binario[i:i+4] == '0100':
            hexa += '4'
        elif binario[i:i+4] == '0101':
            hexa += '5'
        elif binario[i:i+4] == '0110':
            hexa += '6'
        elif binario[i:i+4] == '0111':
            hexa += '7'
        elif binario[i:i+4] == '1000':
            hexa += '8'
        elif binario[i:i+4] == '1001':
            hexa += '9'
        elif binario[i:i+4] == '1010':
            hexa += 'A'
        elif binario[i:i+4] == '1011':
            hexa += 'B'
        elif binario[i:i+4] == '1100':
            hexa += 'C'
        elif binario[i:i+4] == '1101':
            hexa += 'D'
        elif binario[i:i+4] == '1110':
            hexa += 'E'
        elif binario[i:i+4] == '1111':
            hexa += 'F'
    return hexa

#negate binary number and add 1 list
def negate(binario):
    binario = list(binario)
    for i in range(len(binario)):
        if binario[i] == '1':
            binario[i] = '0'
        else:
            binario[i] = '1'
    binario = ''.join(binario)
    binario = int(binario,2)
    binario += 1
    binario = binarizar(binario)
    return binario

def buscador_etiquetas(etiqueta,posicion):
    for i in range(len(etiqueta)):
        if transformar[i] == ' ' or transformar[i] == '':
            continue
        else:
            l = i
            break

    for i in range (l,len(etiqueta)):
        if etiqueta[i] == ':':
            nombre_tiket.append(etiqueta[l:i])
            valor_tiket.append(posicion*4)
            break
    

    


for i in range(len(lineas)):
    transformar = lineas[i]
    buscador_etiquetas(transformar,i)
    
print('etiquetas encontradas: ', nombre_tiket)
print('valores de las etiquetas: ', valor_tiket) 

#bucle for para todas las lineas
fichero = open('instruction_memory.txt','w')
fichero2 = open('instruction_memory2.txt','w')
for i in range(len(lineas)):
    transformar = lineas[i]
    print('linea: ',transformar)
    guardar = transformar_lista(transformar,i)
    print('guardar: ',guardar)
    largo = int(len(guardar))
    cuadrupla = int(largo/4)
    print('largo: ',largo)
    fichero2.writelines(f'{binario_a_hexa(guardar)}\n')
    fichero.writelines(f'{guardar[largo-cuadrupla*4:largo-cuadrupla*3]}\n')
    fichero.writelines(f'{guardar[largo-cuadrupla*3:largo-cuadrupla*2]}\n')
    fichero.writelines(f'{guardar[largo-cuadrupla*2:largo-cuadrupla]}\n')
    fichero.writelines(f'{guardar[largo-cuadrupla:largo]}\n')

fichero.close()
fichero2.close()

    



