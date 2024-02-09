import pickle
import os

instruction = """
---------------------------------------------
|          Gestionnaire de taches           |
|               Thomas DAVID                |
---------------------------------------------
|  a Ranger = nouvelle tache "Ranger"       |
|  s Ranger = supprime la tache "Ranger"    |
|  st = supprime toute les taches           |
|  l = affiche liste de tache               |
|  i = re-affiche ces instructions          |
|  q = quitte l'application et save         |
---------------------------------------------
"""


#Classe gestionnaire de tache de notre programme, il va créer une liste avec toutes nos taches dedans
class TaskManager:
    # Permet de déclarer une liste ou seront stocké les tâches
    def __init__(self):
        self.tasks = []

        if(os.path.exists("save.txt")):
            self.loadData()

    #Permet de sauvegarder la liste dans un fichier txt
    def saveData(self):
        #w pour lire le fichier & b pour dire que c'est du binaire
        with open('save.txt', 'wb') as saveFile:
            pickle.dump(self.tasks, saveFile)

    #Permet de dll cette liste du fichier texte save et devient la liste "active" quand on relance le programme
    def loadData(self):
        #r pour read et b pour dire que c'est du binaire
        with open('save.txt', 'rb') as saveFile:
            self.tasks = pickle.load(saveFile)

    #Permet de créer des taches - On demande un attribut task -> la tache à ajouter
    def createTask(self, task):
        self.tasks.append(Task(task))

#Classe permettant de créer les objets de la class Task cf ci-dessus
class Task:
    def __init__(self, task):
        #on attribut une variable à l'objet = à la variable renseignée
        self.task = task

#On crée un objet de la classe manager
print(instruction)
taskManager = TaskManager()
while True:
    print("")
    prompt = input("Action : ")

    #Ajouter une tache
    if(prompt[:2] == "a "):
        newtask = prompt[2:]
        print("Ajouter la tache '" + newtask + "' ? (oui/non)")
        prompt = input()
        if(prompt =="oui"):
            #Lance la création de mon objet
            taskManager.createTask(newtask)

    #Suppression d'une tache
    elif(prompt[:2] == "s "):
        taskToDel = prompt[2:]
        taskToDelObject = None
    #On fait une boucle sur tous nos objets tasks et si chaque objet == tache à suppr ,on suppr l'objet
        for element in taskManager.tasks:
            if(element.task == taskToDel):
                taskToDelObject = element
        if(taskToDelObject == None):
            #Permet de savoir si aucun objet n'a été trouvé cela reste à None
            print("Il n'y a pas de tache nommer '" + taskToDel + "'")
        else:
            print("Supprimer la tache '" + taskToDel + "' ? (oui/non)")
            prompt = input()
            if(prompt == "oui"):
                taskManager.tasks.remove(taskToDelObject)

    #Suppression de toutes les taches
    elif(prompt == "st"):
        print("Supprimer toutes les tâches ? (oui/non)")
        prompt = input()
        if (prompt == "oui"):
            taskManager.tasks = []

    #Affiche la liste des taches
    elif(prompt[0] == "l"):
        #On fait une boucle pour parcourir notre liste de tache et les afficher
        for element in taskManager.tasks:
            print(" - " + element.task)

    #Affiche les instructions
    elif(prompt[0] == "i"):
        print(instruction)

    #Quitter l'application + save
    elif(prompt[0] == "q"):
        print("Voulez-vous quitter l'application ? (oui/non)")
        prompt = input()
        if (prompt == "oui"):
            #Lance la sauvegarde
            taskManager.saveData()
            #Quitte le programme
            quit()
