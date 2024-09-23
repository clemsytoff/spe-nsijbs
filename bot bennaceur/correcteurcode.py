import discord
from discord.ext import commands
import io
import textwrap
import contextlib

# Initialisation du bot
intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour lire le contenu des messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Commande pour vérifier le code Python
@bot.command(name='eval')
async def eval_python(ctx, *, code: str):
    # Filtrage du bloc de code
    if code.startswith('```') and code.endswith('```'):
        code = code[3:-3].strip()  # Supprime les balises ``` du bloc de code

    # Rediriger la sortie standard pour capturer les résultats de l'exécution
    str_output = io.StringIO()

    try:
        with contextlib.redirect_stdout(str_output):
            # Exécuter le code en utilisant 'exec' de manière sécurisée
            exec(textwrap.dedent(code))
    except Exception as e:
        # En cas d'erreur, capturer l'exception
        output = f"Erreur : {e}"
    else:
        # Si l'exécution est réussie, renvoyer la sortie capturée
        output = str_output.getvalue()

    # Envoyer le résultat ou l'erreur dans Discord
    if not output:
        output = "Le code n'a rien renvoyé."
    
    # Envoyer la réponse dans Discord (limitée à 2000 caractères)
    await ctx.send(f"Résultat :\n```{output[:1990]}```")

# Lancer le bot avec votre jeton
bot.run('TOKEN')
