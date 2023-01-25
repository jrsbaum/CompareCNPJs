import db
from cfg import COLLECTION_NAME1, COLLECTION_NAME2, NEW_COLLECTION_NAME
from new_obj import create_new_object


def main():
    i = 0
    while i != 1:
        i = input("Pressione 1 pra continuar: ")
        processes1_collection = db.get_database1()[COLLECTION_NAME1]
        print("ok1")
        processes2_collection = db.get_database2()[COLLECTION_NAME2]
        print("ok2")
        processes1 = list(processes1_collection.find())
        print("ok3")
        processes2 = list(processes2_collection.find())
        print("ok4")
        new_objects = []
        print("ok5")
        for process1 in processes1:
            for process2 in processes2:
                if "CNPJ" in process1 and "CNPJ" in process2:
                    if process1["CNPJ"] == process2["CNPJ"]:
                        new_objects.append(create_new_object(process1, process2))
        new_database = db.get_new_database()
        new_collection = new_database[NEW_COLLECTION_NAME]
        new_collection.insert_many(new_objects)
        print("New objects created and inserted into the new collection.")


if __name__ == "__main__":
    main()


