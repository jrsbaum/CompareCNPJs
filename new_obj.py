def create_new_object(process1, process2):
    count_big = 0
    count_neo = 0
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

    # ADD PROCESS
    process_numbers = []
    for process in [process1, process2]:
        if "Result" in process:
            for lawsuit in process["Result"][0]["Lawsuits"]["Lawsuits"]:
                if lawsuit["Number"] not in process_numbers:
                    process_numbers.append(lawsuit["Number"])
                    new_object["Processos"].append(
                        {"NumeroProcesso": lawsuit["Number"], "BigDataCorp": True, "NeoWay": False})

                else:
                    for item in new_object["Processos"]:
                        if item["NumeroProcesso"] == lawsuit["Number"]:
                            item["BigDataCorp"] = True

        if "results" in process:
            for result in process["results"]:
                if result["processo"] not in process_numbers:
                    process_numbers.append(result["processo"])
                    new_object["Processos"].append(
                        {"NumeroProcesso": result["processo"], "BigDataCorp": False, "NeoWay": True})

                else:
                    for item in new_object["Processos"]:
                        if item["NumeroProcesso"] == result["processo"]:
                            item["NeoWay"] = True

    # ADD QUANTIDADE DE CADA DB
    for processo in new_object["Processos"]:
        if processo["BigDataCorp"]:
            count_big += 1
        if processo["NeoWay"]:
            count_neo += 1
    new_object["QtdBigDataCorp"] = count_big
    new_object["QtdNeoway"] = count_neo

    return new_object
