import asyncio
import datetime
import functools
import re
from io import BytesIO
from typing import List

import discord
from discord.ext import commands

import config



async def files_from_message(message: discord.Message) -> list[discord.File]:
    files = []
    for attachment in message.attachments:
        with BytesIO() as fp:
            await attachment.save(fp)
            fp.seek(0)
            new_file = discord.File(fp, filename=attachment.filename)
            files.append(new_file)
    return files


def is_uwu_channel(message: discord.Message):
    return channel_matches(message, config.UWU_PATTERN)


def is_quotes_channel(message: discord.Message):
    return channel_matches(message, config.QUOTES_PATTERN)


def channel_matches(message: discord.Message, pattern: re.Pattern):
    # this will filter guilds for us too
    return message and message.channel \
        and isinstance(message.channel, discord.TextChannel) \
        and pattern.match(message.channel.name)


async def get_implied_message(ctx: commands.Context, default_to_previous: bool = True) -> discord.Message:
    message = ctx.message.reference
    if isinstance(message, discord.MessageReference):
        message = message.resolved
    if isinstance(message, discord.Message):
        return message
    elif isinstance(message, discord.DeletedReferencedMessage):
        raise commands.BadArgument()

    if default_to_previous:
        async for message in ctx.channel.history(limit=1, before=ctx.message):
            return message  # return first message

    raise commands.BadArgument()


def run_in_executor(_func):  # https://stackoverflow.com/a/64506715
    @functools.wraps(_func)
    def _run_in_executor(*args, **kwargs):
        loop = asyncio.get_event_loop()
        func = functools.partial(_func, *args, **kwargs)
        return loop.run_in_executor(executor=None, func=func)
    return _run_in_executor


def is_uri(string: str):
    return string and re.match(r'^https?://', string) is not None


async def try_delete_cmd(ctx: commands.Context) -> bool:
    return await try_delete(ctx.message, ctx)


async def try_delete(msg: discord.Message, send_handle: discord.abc.Messageable = None) -> bool:
    if not send_handle:
        send_handle = msg
    try:
        await msg.delete()
        return True
    except discord.Forbidden:
        # no permissions to delete
        # await send_handle.send(config.NO_PERMISSIONS, delete_after=config.MESSAGE_TIMER)
        pass
    except discord.NotFound:
        pass  # message already deleted
    except discord.HTTPException:
        pass  # deleting message failed
    return False


async def get_nickname(bot, guild: discord.Guild, user_id: int) -> str:
    try:
        user = bot.get_user(user_id) or await bot.fetch_user(user_id)
    except discord.NotFound:
        return '<Deleted User>'

    member = guild.get_member(user.id)
    try:
        name = member.nick or member.name  # if no nick, default to name
    except AttributeError:
        name = f'{user.name}#{user.discriminator}'
    return name
