chave = '45ae189936973612cdaefca127f7664257081a3794c84c28213d395f5e3cf46910bafb6f1d89a0e2466c5dc35481a9acde1be4506cf55ff356a0404052529cdd'
chave_2 = '45ae189936973612cdaefca127f7664257081a3794c84c28213d395f5e3cf46910bafb6f1d89a0e2466c5dc35481a9acde1be4506cf55ff356a0404052529cdd'
if chave == chave_2:
    print("As chaves são iguais.")
else:
    print("As chaves são diferentes.")

#download
#sacar e guardar chave sha-512
#guardar código gerado: 45ae189936973612cdaefca127f7664257081a3794c84c28213d395f5e3cf46910bafb6f1d89a0e2466c5dc35481a9acde1be4506cf55ff356a0404052529cdd  Apache-NetBeans-18-bin-macosx.dmg
#quando abrir o terminal arrastar a pasta para assumir o directório
#comando para terminal (mac): shasum -a 512 Apache-NetBeans-18-bin-macosx.dmg
#resultado terminal: 45ae189936973612cdaefca127f7664257081a3794c84c28213d395f5e3cf46910bafb6f1d89a0e2466c5dc35481a9acde1be4506cf55ff356a0404052529cdd
#script python comparação
