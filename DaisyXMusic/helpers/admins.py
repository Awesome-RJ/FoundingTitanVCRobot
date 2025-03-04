# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from typing import List

from pyrogram.types import Chat, User

from DaisyXMusic.function.admins import get as gett
from DaisyXMusic.function.admins import set


async def get_administrators(chat: Chat) -> List[User]:
    if get := gett(chat.id):
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [administrator.user.id for administrator in administrators]

    set(chat.id, to_set)
    return await get_administrators(chat)
