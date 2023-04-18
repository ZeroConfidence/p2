from PIL import Image       #Imports Image from Pillow
from pathlib import Path    #Imports path from pathlib

def ImageSender(Stock_Number):
    Image = 0               #cleans Image from former uses
    Image_Path_Folder="../stockimages/stock"                            #Image Path subsection, folder location + start of file name
    Image_Path_Number=Stock_Number                                      #Image Path subsection, file number
    Image_Path_Filetype=".png"                                          #Image Path subsection, File extension
    Image_Path=Image_Path_Folder+Image_Path_Number+Image_Path_Filetype  #Image Path subsection, combines the image path subsections

    Image = Path(Image_Path)    #Image is opened with pillow

    return Image    #Return image
    
    