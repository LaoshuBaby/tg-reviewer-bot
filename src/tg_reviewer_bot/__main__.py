import logging

from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from const import TG_BOT_USERNAME, TG_REVIEWER_GROUP, TG_TOKEN
from review import (
    ReviewChoice,
    append_message,
    approve_submission,
    comment_message,
    query_decision,
    reject_reason,
    reject_submission,
    remove_append_message,
    send_custom_rejection_reason,
    withdraw_decision,
)
from submit import submission_handler
from utils import PrefixFilter

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token(TG_TOKEN)
        .get_updates_connect_timeout(60)
        .connect_timeout(60)
        .get_updates_read_timeout(60)
        .read_timeout(60)
        .get_updates_write_timeout(60)
        .write_timeout(60)
        .build()
    )

    application.add_handler(submission_handler)

    application.add_handlers(
        [
            CallbackQueryHandler(
                approve_submission,
                pattern=f"^({ReviewChoice.SFW}|{ReviewChoice.NSFW})",
            ),
            CallbackQueryHandler(
                reject_submission,
                pattern=f"^({ReviewChoice.REJECT}|{ReviewChoice.REJECT_DUPLICATE})",
            ),
            CallbackQueryHandler(
                query_decision, pattern=f"^{ReviewChoice.QUERY}"
            ),
            CallbackQueryHandler(
                withdraw_decision, pattern=f"^{ReviewChoice.WITHDRAW}"
            ),
            CallbackQueryHandler(
                append_message, pattern=f"^{ReviewChoice.APPEND}"
            ),
            CallbackQueryHandler(reject_reason, pattern=f"^REASON"),
            MessageHandler(
                filters.REPLY
                & filters.Chat(chat_id=int(TG_REVIEWER_GROUP))
                & (
                    PrefixFilter("/append ")
                    | PrefixFilter(f"@{TG_BOT_USERNAME} /append ")
                ),
                append_message,
            ),
            MessageHandler(
                filters.REPLY
                & filters.Chat(chat_id=int(TG_REVIEWER_GROUP))
                & (
                    PrefixFilter("/remove_append ")
                    | PrefixFilter(f"@{TG_BOT_USERNAME} /remove_append ")
                ),
                remove_append_message,
            ),
            MessageHandler(
                filters.REPLY
                & filters.Chat(chat_id=int(TG_REVIEWER_GROUP))
                & (
                    PrefixFilter("/comment ")
                    | PrefixFilter(f"@{TG_BOT_USERNAME} /comment ")
                ),
                comment_message,
            ),
            MessageHandler(
                filters.REPLY & filters.Chat(chat_id=int(TG_REVIEWER_GROUP)),
                send_custom_rejection_reason,
            ),
        ]
    )
    application.run_polling()
