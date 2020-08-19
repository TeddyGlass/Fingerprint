from rdkit import Chem
import numpy as np
import pandas as pd


def mol2bit(MOLS):
    BIT = []
    FP = []
    for i, mol in enumerate(MOLS):
        if mol is not None:
            bit = {}
            fp = Chem.RDKFingerprint(mol, bitInfo=bit)
            BIT.append(bit)
            FP.append(fp)
        else:
            BIT.append(np.nan)
            FP.append(np.nan)
            print(i)
    return BIT


def bit2df(BIT):
    df = pd.DataFrame(np.zeros((len(BIT),2048), dtype=int))
    for i in range(len(BIT)):
        if type(BIT[i])==float:
            df.loc[i,:] = np.nan
        else:
            bit = list(BIT[i].keys())
            df.loc[i,bit] = int(1)
    return df


if __name__ == '__main__':
    path = './data'
    df = pd.read_csv(f"{path}/SMILES.csv")
    SMILES = df['SMILES'].tolist()
    MOLS = [Chem.MolFromSmiles(smi) for smi in SMILES]
    # calculate fingerprint
    BIT = mol2bit(MOLS)
    df_fp = bit2df(BIT)
    df_fp = pd.concat([df['SMILES'], df_fp], axis=1)
    df_fp.to_csv(f'{path}/smiles2fp.csv')