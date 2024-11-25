from src.embed_generator.embed import Embed


class Message:
    # TODO add file support
    # TODO add sticker support
    # TODO add delete_after support
    # TODO add nonce support
    # TODO add reference support (replies)
    # TODO add view support
    # TODO add silent support

    def __init__(self, text: str = None) -> None:
        """
        #### Creates a Message object
        **text:** text of the message"""
        self.set_text(text)
        self.embeds = []

    # Text Methods
    def set_text(self, text: str) -> None:
        """
        Sets the text of the message\n
        **text:** text of the message"""
        self.text = text

    def clear_text(self) -> None:
        """
        Clears the text of the message"""
        self.text = None

    # TTS methods
    def enable_TTS(self) -> None:
        """
        Enables TTS for the message"""
        self.TTS = True

    def disable_TTS(self) -> None:
        """
        Disables TTS for the message"""
        self.TTS = False

    # Embed Methods
    def add_embed(self, embed, index: int = -1, is_JSON: bool = False) -> None:
        """
        Adds and Embed to the message\n
        **embed:** Embed object being added\n
        **index:** *optional* index of where the embed is added (default -1 = end)\n
        **is_JSON:** *optional* whether embed is JSON code"""
        if is_JSON:
            embed_object = Embed()
            embed_object.from_JSON(embed)
        else:
            embed_object = embed

        if index is -1:
            self.embeds.append(embed_object)
        else:
            self.embeds.insert(index, embed_object)

    def add_embeds(self, embeds: list, is_JSON: bool = False) -> None:
        """
        Adds a list of Embeds to the message\n
        *adds the the end of the other embeds*\n
        **embeds:** list of embeds\n
        **is_JSON:** *optional* whether the list of Embeds are JSON code (must all be same type)
        """
        for embed in embeds:
            self.add_embed(embed, -1, is_JSON)

    def delete_embed(self, embed_name: str, delete_all: bool = True) -> None:
        """
        Removes Embed based on its name from the message\n
        **embed_name:** name of embed being removed\n
        **delete_all:** *optional* whether all embeds of said name are delete (stops after first one if false)
        """
        for embed in self.embeds:
            if not embed_name == embed.name:
                continue
            self.embeds.remove(embed)
            if not delete_all:
                return
    
    def clear_embeds(self) -> None:
        '''
        Removes all of the messages embeds'''
        self.embeds = []

    def disable_embeds(self) -> None:
        '''
        Suppresses the embeds for the message\n
        *message will send without embeds*'''
        self.embeds_enabled = False
    
    def enable_embeds(self) -> None:
        '''
        Un-suppresses the embeds for the message\n
        *message will send with embeds*'''
        self.embeds_enabled = True
