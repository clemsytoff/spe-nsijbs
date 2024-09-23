import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Assurez-vous que les intents des membres sont activés si nécessaire

client = discord.Client(intents=intents)

# Au lancement
@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name="Python")
    await client.change_presence(status=discord.Status.dnd, activity=activity)

    # dnd = ne pas déranger, idle = lune, offline = hors ligne, online = en ligne
    print("Bot lancé avec succès!")

# Commandes
@client.event
async def on_message(message):
    # Ne pas répondre aux messages du bot
    if message.author == client.user:
        return
    
    if message.content.lower() == "ping":
        print("pong")
        await message.channel.send("Pong. *(Pourquoi tu fais cette commande même ?)*")

    # Détecter si le message contient le mot "cours"
    if "cours" in message.content.lower():
        print("cours")
        await message.reply("Le cours est disponible sur Github à l'adresse suivante : https://github.com/clemsytoff/spe-nsijbs/tree/main \n **C'est que de la logique.**")
    
        # Détecter si le message contient le mot "gg"
    if "gg" in message.content.lower():
        print("gg")
        await message.reply("Ouais je sais je suis le goat, de toutes façons **__c'est que de la logique__.**")

            # Détecter si le message contient le mot "zizi"
    if "zizi" in message.content.lower():
        print("zizi")
        await message.reply("<@827967775851020308> je sais que c'est toi... **Arrête ou je te met -1 au controle**.")
    
            #Detecter si on ping le bot
    if "<@929681733799018516>" in message.content.lower():
        print("ping bot")
        await message.reply("# Tu refais ça je te met -1 au controle ! \n *De toutes façons c'est que de la logique...*")

        #decter si on ping bharat
    
    if "<@827967775851020308>" in message.content.lower():
        print("ping bharat")
        await message.channel.send("Oh non... Pas Bharat...")

        #detecter si whallah + pardon
    
    if "wallah" in message.content.lower() and "pardon" in message.content.lower():
        print("pardon")
        await message.reply("Excuses acceptées,** __tu n'as pas la logique !__**")
    
        #decter si carré
    
    if "carré" in message.content.lower() or "carre" in message.content.lower():
        print("carré")
        await message.channel.send("*Non, rond...*")

        #detecter si naceur
    
    if "<@923271055156584490>" in message.content.lower():
        print("ping naceur")
        await message.reply("Lâche mon collègue ou je te met **moins 1 !!!!!**")




#MODERATION


#auto mod
    insultes = ["fdp","fils de pute","connard","enculé","niquez","salope","sale pute","sale salope"]
    for i in insultes:
         if i in message.content.lower():
            print("[AUTOMOD] : " + str(message.author) + " a été censuré suite à son message : " + str(message.content))
            await message.delete()  
            await message.channel.send(message.author.mention + " **Oh collègue calme toi où je te vire du cours !**") 

    #on envoie dans un chanel auto mod

            await client.get_channel(1284189874588487762).send("**[AUTOMOD]** : " + str(message.author) + " a été censuré suite à son message : " + str(message.content))


#clear
    if message.content.startswith("!clear"):
        # Diviser le message pour obtenir le nombre de messages à supprimer
        parts = message.content.split()
        if len(parts) != 2:
            await message.channel.send("*Tu n'as pas la logique...* On fait : **!clear [nombre]**")
            return

        try:
            amount = int(parts[1])
        except ValueError:
            await message.channel.send("Tu dois choisir un nombre entre 1 et 100 ! **C'est de la logique!**")
            return

        # Vérifier que l'utilisateur a la permission de gérer les messages
        if not message.author.guild_permissions.manage_messages:
            await message.channel.send("Tu n'as pas la permission de supprimer des messages, **-1 au controle !**.")
            return

        # Vérifier que la valeur de `amount` est valide (entre 1 et 100)
        if amount < 1 or amount > 100:
            await message.channel.send("Tu dois choisir un nombre entre 1 et 100 ! **C'est de la logique!**")
            return

        # Essayer de supprimer les messages
        try:
            deleted = await message.channel.purge(limit=amount)
            # Envoyer un message confirmant combien de messages ont été supprimés
            confirmation_message = await message.channel.send(f"{len(deleted)} messages supprimés. *Tu as enfin la logique !*")
            await confirmation_message.delete(delay=5)  # Supprimer le message de confirmation après 5 secondes
        except discord.Forbidden:
            await message.channel.send("Je n'ai pas la permission de gérer les messages dans ce canal, *pourtant je suis le prof ?*")
        except discord.HTTPException as e:
            await message.channel.send(f"Une erreur est survenue : {e}")




# Sans commandes - bienvenue

@client.event
async def on_member_join(member):
    channel_bienvenue = client.get_channel(1284136613823123549)
    await channel_bienvenue.send("# Bienvenue sur le serveur " + str(member.mention) + ", je t'ai mis le rôle **Etudiant**. *J'éspère que tu as la logique...*")

     # ID du rôle à attribuer
    role_id = 1284129159743799368
    # Obtenir le rôle par son ID
    role = discord.utils.get(member.guild.roles, id=role_id)
    
    if role:
        try:
            # Ajouter le rôle au membre
            await member.add_roles(role)
            print(f"Le rôle {role.name} a été attribué à {member.display_name}.")
        except discord.Forbidden:
            print("Le bot n'a pas la permission d'attribuer des rôles.")
        except discord.HTTPException as e:
            print(f"Une erreur est survenue : {e}")
    else:
        print(f"Le rôle avec l'ID {role_id} n'a pas été trouvé.")





client.run("TOKEN")
