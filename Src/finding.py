from Src.mongoThings import *


def findThings(array, method = "Users", style = "Position", secret=[], length=3):

    #Seleccionar Database
    if method == "Users":
        db = pickDB()
    if method == "Chats":
        db = pickDB(method = "Chats")

    #Seleccionar detalles adicionales
    if style == "_id":
        selectFilter = "Position"
    if style == "Position":
        selectFilter = "Username"

    #Búsqueda del elemento seleccionado
    result = secret
    try:
        filter = {f"{selectFilter}":array[0]}
        projection = {f"{style}":1}
        limit = 1
        sort = list({'_id': -1}.items())
        users = db.find(filter=filter,limit=limit,projection=projection, sort=sort)
        result.append(users[0][f"{style}"])
        array.remove(array[0])
        findThings(array, method= method, style = style,secret=result,length=length)

    #Creación de nuevo usuario si no existiera
    except IndexError:
        try:
            from Src.create import createUser
            newUser = createUser(array[0])
            result.append(newUser)
            array.remove(array[0])
            findThings(array, method= method, style = style,secret=result,length=length)
        except IndexError:
            #Error de retorno
            return result

    except AttributeError:
        filter = {f"{selectFilter}":array[0]}
        projection = {f"{style}":1}
        limit = 1
        sort = list({'_id': -1}.items())
        chats = db.find(filter=filter,limit=limit,projection=projection, sort=sort)
        result.append(chats[0][f"{style}"])
        return result

  
    return result[-length:]