import argparse
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Visualize Hole Vectors')
    parser.add_argument('hv_csv', default=None, metavar='HV_csv', type=argparse.FileType('r'), help="Path to the hole vector csv file")
    parser.add_argument('index', default=None, metavar='INDEX', type=int, help="sample choice")
    args = parser.parse_args()
    
    df = pd.read_csv(args.hv_csv)

    print(df.describe())
    print('')
    print(df.head(5))
    print('')
    
    HV = df.iloc[:, 0:400]

    image = np.array(HV.loc[[args.index]]).astype(np.float32).reshape(20,20)
    title = "Hole Vector sample "+f'{args.index}'
    
    k = plt.figure()
    plt.imshow(image)
    plt.title(title)
    #plt.show()
    k.savefig(title+'.jpg', dpi=300)
    print("generated")

if __name__ == '__main__':
    main()