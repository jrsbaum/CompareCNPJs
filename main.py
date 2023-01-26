import db
from cfg import COLLECTION_NAME1, COLLECTION_NAME2, NEW_COLLECTION_NAME
from new_obj import create_new_object


def main():
    input("Pressione alguma tecla pra continuar: ")
    processes1_collection = db.get_database1()[COLLECTION_NAME1]
    processes2_collection = db.get_database2()[COLLECTION_NAME2]
    processes1 = list(processes1_collection.find())
    processes2 = list(processes2_collection.find())
    new_objects = []

    for process1 in processes1:
        for process2 in processes2:
            if "CNPJ" in process1 and "CNPJ" in process2:
                if process1["CNPJ"] == process2["CNPJ"]:
                    new_objects.append(create_new_object(process1, process2))

    new_database = db.get_new_database()
    new_collection = new_database[NEW_COLLECTION_NAME]
    new_collection.insert_many(new_objects)
    print("Novos objetos criados e inseridos na noca collection!")


if __name__ == "__main__":
    main()


