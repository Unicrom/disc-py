class EmbedField:
    def __init__(self, label: str, content: str, inline: bool = True) -> None:
        """
        #### Creates an EmbedField Object
        **label:** name of field\n
        **content:** content of field\n
        **inline:** *optional* whether the field is displayed as inline"""
        self.label = self.set_label(label)
        self.content = self.set_content(content)
        self.inline = inline

    def set_label(self, label: str, raise_error: bool = True) -> None:
        """
        #### Sets the name of the field
        **label:** what the name of the field is set to *256 char max*\n
        **raise_error:** *optional* whether an Error is raised if label exceeds 256 char
        """
        if 256 < len(label) and raise_error:
            raise Exception("Label of Field exceeds 256 char limit")
        self.label = label

    def set_content(self, content: str, raise_error: bool = True) -> None:
        """
        #### Sets the value of the field
        **content:** what the value of the field is set to *1024 char max*\n
        **raise_error:** *optional* whether an Error is raised if content exceeds 1024 char
        """
        if 1024 < len(content) and raise_error:
            raise Exception("content of Field exceeds 1024 char limit")
        self.content = content

    def set_inline(self) -> None:
        """
        #### Sets the Field to be displayed as inline"""
        self.inline = True

    def set_block(self) -> None:
        """
        #### Sets the Field to be displayed as block"""
        self.inline = False

    def to_JSON(self) -> dict:
        """
        #### Returns the three attributes of the Field objet in JSON format"""
        info_JSON = {
            "label": self.label,
            "content": self.content,
            "inline": self.inline,
        }
        return info_JSON
