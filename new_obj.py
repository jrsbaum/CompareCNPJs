def create_new_object(process1, process2):
    new_object = {
        "CNPJ": "",
        "Processos": [
            {
                "NumeroProcesso": process1["NumeroProcesso"],
                "NeoWay": process1["NeoWay"],
                "BigDataCorp": process2["BigDataCorp"]
            },
            {
                "NumeroProcesso": process2["NumeroProcesso"],
                "NeoWay": process2["NeoWay"],
                "BigDataCorp": process2["BigDataCorp"]
            }
        ],
        "QtdNeoway": 1,
        "QtdBigDataCorp": 2,
        "QtdBigDataCorpSemNeoWay": 1,
        "QtdNeoWaySemBigDataCorp": 0
    }
    return new_object

