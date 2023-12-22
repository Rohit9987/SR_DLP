def runTree(filename):
    print('-'*99)
    print(filename)

    ds = pydicom.dcmread(filename)
    ds.decode()
    recursive_tree(ds)

def recursive_tree(dataset):
    global val 
    for data_element in dataset:
        if data_element.VR == "SQ":
            for i, element in enumerate(data_element.value):
                try:
                    el = element[0x0008, 0x0100].value
                    if "Gy.cm" in el:
                        print(el)
                        print(val)
                except:
                    pass

                try:
                    val = element[0x0040, 0x0a30a].value
                except:
                    pass

                recursive_tree(element)

usage = "Usage: python dicomtree.py dicom_filename"
    
if __name__ == "__main__":
    import sys
    import pydicom
    import os
    os.system('clear')

    if len(sys.argv) != 2:
        print(usage)
        sys.exit(-1)
    runTree(sys.argv[1])


