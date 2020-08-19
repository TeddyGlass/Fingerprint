# Fingerprint
## Enviornment
・Python 3.7.7  
・rdkit 020.03.3.0  
・numpy 1.18.1  
・pandas 1.0.4  
## Usage
*smiles2fp.py*  
smilesが格納されたcsvファイルからRDkit-Fingerprintを計算。 
結果は./data/smiles2fp.csvに保存

*読み込み用csvファイルフォーマット*  
ファイル名: SMILES.csv  
場所: ./data/  
列名: SMILES  
