## TheDragonWarriorBot Example plugin format
```python3
from Natsuki.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="Natsuki")
@disableable_dec("Natsuki")
async def _(message):
    j = "Hello there my name is Dragon Warrior"
    await message.reply(j)
    

__help__ = """
<b>Hi</b>
- /hi: Hello there my name is Dragon Warrior
"""
__mod_name__ = "Dragon Warrior"
```
