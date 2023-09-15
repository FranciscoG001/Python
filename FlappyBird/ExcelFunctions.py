import openpyxl
import pygame

def createExcelFile():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    return sheet, workbook

def addCollunsToExcel(sheet):
    sheet["A1"] = "BirdYPosition"
    sheet["B1"] = "DistanceToFirstCornerUpPipe"
    sheet["C1"] = "DistanceToFirstCornerDownPipe"
    sheet["D1"] = "DistanceToSecondCornerUpPipe"
    sheet["E1"] = "DistanceToSecondCornerDownPipe"
    return sheet

def addCollunsToExcel2(sheet):
    sheet["A1"] = "Tick"
    sheet["B1"] = "Lost"
    sheet["C1"] = "CenterXBird"
    sheet["D1"] = "CenterYBird"
    sheet["E1"] = "WidthBird"
    sheet["F1"] = "HeightBird"
    sheet["G1"] = "ValLeftXFirstPipe"
    sheet["H1"] = "ValRightXFirstPipe"
    sheet["I1"] = "ValYFirstUpPipe"
    sheet["J1"] = "ValYFirstDownPipe"
    sheet["K1"] = "ValLeftXSecondPipe"
    sheet["L1"] = "ValRightXSecondPipe"
    sheet["M1"] = "ValYSecondUpPipe"
    sheet["N1"] = "ValYSecondDownPipe"
    sheet["O1"] = "Jump"
    return sheet

def addValuesToExcel2(valuesToExcel, sheet):
    row = sheet.max_row + 1
    sheet[f"A{row}"] = valuesToExcel[0]
    sheet[f"B{row}"] = valuesToExcel[1]
    sheet[f"C{row}"] = valuesToExcel[2]
    sheet[f"D{row}"] = valuesToExcel[3]
    sheet[f"E{row}"] = valuesToExcel[4]
    sheet[f"F{row}"] = valuesToExcel[5]
    sheet[f"G{row}"] = valuesToExcel[6]
    sheet[f"H{row}"] = valuesToExcel[7]
    sheet[f"I{row}"] = valuesToExcel[8]
    sheet[f"J{row}"] = valuesToExcel[9]
    sheet[f"K{row}"] = valuesToExcel[10]
    sheet[f"L{row}"] = valuesToExcel[11]
    sheet[f"M{row}"] = valuesToExcel[12]
    sheet[f"N{row}"] = valuesToExcel[13]
    sheet[f"O{row}"] = valuesToExcel[14]

def saveAndCloseExcel(workbook):
    workbook.save("FlappyBirdData.xlsx")
    workbook.close()

def touchPipes(bird_x,bird_y,birdResizeImage,pipePos_x,pipePos_x2,upPipPos_y,upPipPos_y2,width,height,start):
    # Touch Pipes
    bird_rect = pygame.Rect(bird_x+13, bird_y+20, birdResizeImage.get_width()-23, birdResizeImage.get_height()-39)
    up_pipe_rect = pygame.Rect(pipePos_x, 0, width/7, upPipPos_y+720)
    down_pipe_rect = pygame.Rect(pipePos_x, upPipPos_y + 890, width/7, height)
    up_pipe_rect2 = pygame.Rect(pipePos_x2, 0, width/7, upPipPos_y2+720)
    down_pipe_rect2 = pygame.Rect(pipePos_x2, upPipPos_y2 + 890, width/7, height)

    # Pipes 1
    if bird_rect.colliderect(up_pipe_rect) or bird_rect.colliderect(down_pipe_rect):
        start = False
    # Pipes 2
    if bird_rect.colliderect(up_pipe_rect2) or bird_rect.colliderect(down_pipe_rect2):
        start = False
    
    return start, bird_rect, up_pipe_rect, up_pipe_rect2, down_pipe_rect, down_pipe_rect2
