from telegram.ext import *
import handlers_prof


def main():
    TOKEN = "5869077123:AAGew2WGGHsUT92AxS8x8mJAYaRpaRovIs4"

    dp = Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler("help", handlers_prof.help_command))
    dp.add_handler(CommandHandler("cadastrar_conteudo", handlers_prof.cadastrar_conteudo))
    dp.add_handler(CommandHandler("start", handlers_prof.start))

    dp.add_handler(handlers_prof.enviar_planilha_conversation)
    dp.add_handler(handlers_prof.enviar_plano_conversation)

    print("Bot started. . .\n")
    dp.run_polling()
    print("Bot finished. . .\n")


if __name__ == "__main__":
    main()
