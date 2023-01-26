def create_new_object(process1, process2):
    new_object = {
        "CNPJ": "",
        "Processos": [],
        "QtdBigDataCorp": "",
        "QtdNeoway": "",
        "QtdBigDataCorpSemNeoWay": "",
        "QtdNeoWaySemBigDataCorp": ""

    }
    # ADD CNPJ
    if "CNPJ" in process1 == "CNPJ" in process2:
        new_object["CNPJ"] = process1["CNPJ"] + process2["CNPJ"]
    elif "CNPJ" in process1:
        new_object["CNPJ"] = process1["CNPJ"]
    elif "CNPJ" in process2:
        new_object["CNPJ"] = process2["CNPJ"]

    # ADD QUANTIDADE DE CADA DB
    if "Result" in process1:
        new_object["QtdBigDataCorp"] = process1["Result"][0]["Lawsuits"]["TotalLawsuits"]
    if "results" in process2:
        new_object["QtdNeoway"] = process2["total"]

    # ADD PROCESS
    for i, process in enumerate([process1, process2]):
        if "Result" in process:
            for lawsuit in process["Result"][0]["Lawsuits"]["Lawsuits"]:
                new_object["Processos"].append({"NumeroProcesso": lawsuit["Number"]})
        if "results" in process:
            for result in process["results"]:
                new_object["Processos"].append({"NumeroProcesso": result["processo"]})

    return new_object
